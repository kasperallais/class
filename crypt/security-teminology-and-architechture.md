# OSI Security Architecture
- ITU-T X.800 "Security Architecture for OSI"
- Defines a systematic way of defining and providing security requirements
- For us it provides a useful, if abstract, overview of concepts we will study
# Aspects of Security
- Consider 3 aspects of information security
    - Security attack
    - Security Mechanism
    - Security Service
- Terms
    - Threat - A potential for violation of security
    - Vulnerability - A weakness
    - Risk - "Where a threat intersects with a vulnerability, risk is present" - NIST
    - Attack - An assault on system security, a deliberate attempt to evade security services
# Countermeasures
- Means used to deal with security attacks
    - Prevent
    - Detect
    - Recover
- May result in new vulnerabilities
- Will have residual vulnerability
- Goal is to minimize risk given constraints
# Security Functional Requirements
- Technical Measures:
    - Access Control; Identification & Authentication; System & Communication Protection; System & Information Integrity
- Management Controls & Procedures
    - Awareness & Training; Audit & Accountability; Certification, Accreditation & Security Assessments; Contingency Planning; Maintenance; Physical & Environmental Protection; Planning; Personnel Security; Risk Assessment; Systems & Services Acquisition
- Overlapping Technical & Management
    - Configuration Management; Incident Response; Media Protection
# Security Attack
- Passive Attacks
    - A passive attack attempts to learn or make use of information from the system but does not affect system resources
- Active Attacks
    - An active attack attempts to alter system resources or affect their operation
# Two Types of Passive Attacks
- Release of message contents
- Traffic analysis
- Passive attacks are difficult to detect because they do not involve any alteration of the data
- Our main goal is to prevent their success
# Four Types of Active Attacks
- Masquerade
- Replay
- Modification of messages
- Denial of service
- Active attacks are difficult to prevent because of the wide variety of potential physical, software, and network vulnerabilities
- Our main goal is to detect them and to recover from any disruption or delays caused by them
# Security Services
- X.800: 'a service provided by a protocol layer of communicating open systems, which ensures adequate security of the systems or of data transfers'
- RFC 2828: 'a processing or communication service provided by a system to give a specific kind of protection to system resources'
- uses one or more security mechanisms
- often replicates functions normally associated with physical documents
# Security Services (X.800)
- Authentication - assurance that communicating entity is the one claimed
- Access Control - Prevention of the unauthorized use of a resource
- Data Confidentiality - Protection of data from unauthorized disclosure
- Data Integrity - Assurance that data receives is as sent by an authorized entity, no modification, replay, etc.
- Non-Repudiation - Protection against denial by one of the parties in the communication
- Availability - Resource accessible/usable
# Security Mechanisms
- Features designed to prevent, detect, or recover from a security attack
- No single mechanism that will support all services required
- However one particular element underlies many of the security mechanisms in use:
    - Cryptographic techniques
- Hence our focus on this topic
# Security Services (X.800)
- Specific security mechanisms:
    - Encipherment, digital signatures, access controls, data integrity, authentication exchange, traffic padding, routing control, notarization
- Pervasive security mechanisms
    - Trusted functionality, security labels, event detection, security audit trails, security recovery
    - Not specific to any particular OSI security service or protocol layer
# Model for Network Security
- Use this model requires us to
    - Design a suitable algorithm for the security transformation
    - Generate the secret information (keys) used by the algorithm
    - Develop methods to distribute and share the secret information
    - Specify a protocol enabling the principals to use the transformation and secret information for a security service
# Model for Network Access Security
- Using this model requires us to
    - Select appropriate gatekeeper functions to identify users
    - Implement security controls to ensure only authorized users access designated information or resources
