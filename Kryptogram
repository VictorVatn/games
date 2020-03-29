import java.util.Scanner;

class kryptogram {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Write your sentence (only characters from the english alphabet will be changed). Then on a new line write 1 if you want to encrypt your sentence and write 2 if you want to decrypt your sentence. Also write how many steps the letters should take, a number between -25 and 25.");
        String sentence = sc.nextLine();
        int encryptDecrypt = sc.nextInt();
        int steps = sc.nextInt();
        System.out.println(sentence);

        while (steps > 25 || steps < -25) {
            System.out.println("A number between -25 and 25 please");
            steps = sc.nextInt();
        }

       
        while (encryptDecrypt != 1 && encryptDecrypt != 2) {
            System.out.println("Write 1 if you want to encrypt and 2 if you want to decrypt");
            encryptDecrypt = sc.nextInt();
            if (encryptDecrypt == 1 || encryptDecrypt == 2) {
                break;
            }
        }

        if (encryptDecrypt == 1) {
            Encrypt(sentence, steps);
        } else if (encryptDecrypt == 2) {
            Decrypt(sentence, steps);
        }
    

        sc.close();
        
    }
    public static void Encrypt (String sentence, int steps) {
        if (steps < 0) {
            steps += 26;
        }
        String encryptedSentence = "";

        for (char character : sentence.toCharArray()) {
            int asciiValue = (int) (character);
            if (90 < asciiValue && asciiValue < 97 || asciiValue > 122 || asciiValue < 65) {
                encryptedSentence += character;
                continue;
            }
            int encryptedAsciiValue = asciiValue + steps;
            if (asciiValue <= 90 && encryptedAsciiValue > 90) {
                encryptedAsciiValue -= 26;
            } else if  (encryptedAsciiValue > 122) {
                encryptedAsciiValue -= 26;
            }
            char encryptedLetter = (char) (encryptedAsciiValue);
            encryptedSentence += encryptedLetter;
        }
        System.out.println(encryptedSentence);
    }
    public static void Decrypt (String sentence, int steps) {
        if (steps < 0) {
            steps += 26;
        }
        String decryptedSentence = "";

        for (char character : sentence.toCharArray()) {
            int asciiValue = (int) (character);
            if (90 < asciiValue && asciiValue < 97 || asciiValue > 122 || asciiValue < 65) {
                decryptedSentence += character;
                continue;
            }
            int decryptedAsciiValue = asciiValue - steps;
            if (asciiValue >= 97 && decryptedAsciiValue < 97) {
                decryptedAsciiValue += 26;
            } else if  (decryptedAsciiValue < 65) {
                decryptedAsciiValue += 26;
            }
            char decryptedLetter = (char) (decryptedAsciiValue);
            decryptedSentence += decryptedLetter;
        }
        System.out.println(decryptedSentence);
    }
}
