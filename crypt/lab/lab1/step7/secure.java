import java.security.SecureRandom;

public class SecureKeyGen {
    public static void main(String[] args) {
        byte[] key = new byte[16];
        SecureRandom secureRandom = new SecureRandom(); // Cryptographically secure PRNG
        secureRandom.nextBytes(key);
        System.out.println(javax.xml.bind.DatatypeConverter.printHexBinary(key));
    }
}

