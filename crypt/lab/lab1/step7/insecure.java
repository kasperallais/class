import java.util.Random;

public class InsecureKeyGen {
    public static void main(String[] args) {
        byte[] key = new byte[16];
        Random random = new Random(); // Insecure PRNG
        random.nextBytes(key);
        System.out.println(javax.xml.bind.DatatypeConverter.printHexBinary(key));
    }
}

