SET search_path TO kallais;

-- Drop tables if they exist (order matters due to foreign key dependencies)
DROP TABLE IF EXISTS show_instance;
DROP TABLE IF EXISTS show_info;
DROP TABLE IF EXISTS directors;
DROP TABLE IF EXISTS netflix_raw;

-- (Q2) Initial Schema (CREATE TABLE ...)
CREATE TABLE netflix_raw (
    type text,
    title text,
    director text,
    cast_list text,
    production_country text,
    date_added text,
    release_year integer,
    rating text,
    duration text,
    listed_in text,
    description text
);

-- (Q2) Load data into the table (\copy ...)
\copy netflix_raw (type, title, director, cast_list, production_country, date_added, release_year, rating, duration, listed_in, description) FROM 'dataset.csv' CSV HEADER;

-- (Q4) Normalized schemas (CREATE TABLE ...)
CREATE TABLE directors (
    director text PRIMARY KEY,
    production_country text
);

CREATE TABLE show_info (
    title text PRIMARY KEY,
    type text,
    director text,
    cast_list text,
    date_added text,
    release_year integer,
    rating text,
    duration text,
    listed_in text,
    description text
);

CREATE TABLE show_instance (
    show_id serial PRIMARY KEY,
    title text REFERENCES show_info(title)
);

-- (Q5) Loading data from the initial table into the normalized tables  (INSERT INTO ... SELECT ...)
-- Insert distinct directors, replacing missing director values with 'Unknown'
INSERT INTO directors (director, production_country)
SELECT DISTINCT
    CASE WHEN director IS NULL OR director = '' THEN 'Unknown' ELSE director END as director,
    production_country
FROM netflix_raw;

-- Insert show information, ensuring director is not null
INSERT INTO show_info (title, type, director, cast_list, date_added, release_year, rating, duration, listed_in, description)
SELECT DISTINCT
    title,
    type,
    CASE WHEN director IS NULL OR director = '' THEN 'Unknown' ELSE director END as director,
    cast_list,
    date_added,
    release_year,
    rating,
    duration,
    listed_in,
    description
FROM netflix_raw;

-- Insert into show_instance to generate our own show_id
INSERT INTO show_instance (title)
SELECT title FROM show_info;

-- (Q6) Keys and constraints (ALTER TABLE ...)
ALTER TABLE show_info
    ADD CONSTRAINT fk_director FOREIGN KEY (director) REFERENCES directors(director);

ALTER TABLE show_info
    ADD CONSTRAINT check_release_year CHECK (release_year >= 1900 AND release_year <= 2100);

-- (Q7) Interesting Queries (SELECT ...)
-- Query 1: Join between show_instance, show_info, and directors to get show details with director's production country
SELECT si.show_id, si.title, si2.type, si2.date_added, si2.release_year, si2.rating, si2.duration, si2.listed_in, si2.description, d.production_country
FROM show_instance si
JOIN show_info si2 ON si.title = si2.title
JOIN directors d ON si2.director = d.director;

-- Query 2: Top 5 directors by number of shows using a CTE
WITH director_counts AS (
    SELECT director, COUNT(*) as show_count
    FROM show_info
    GROUP BY director
)
SELECT director, show_count
FROM director_counts
ORDER BY show_count DESC
LIMIT 5;

-- Query 3: Aggregate query: Count of shows per rating
SELECT rating, COUNT(*) as num_shows
FROM show_info
GROUP BY rating;

-- (Q8) Indexes and performance tuning (CREATE INDEX ...)
-- Create index on show_info(director) to improve join performance
CREATE INDEX idx_show_info_director ON show_info(director);

-- Create index on show_info(release_year) to accelerate queries filtering by release_year
CREATE INDEX idx_show_info_release_year ON show_info(release_year);
