import java.lang.Character;

class SqueakyClean {
    static String clean(String identifier) {
        char[] word = identifier.toCharArray();
        String cleanWord = "";
        for (int i=0; i< word.length;i++){
            if (Character.isWhitespace(word[i])) {
                word[i] = '_';
                cleanWord += word[i];
            }
            else if (word[i] == '-'){
                i++;
                word[i] = Character.toUpperCase(word[i]);
            }  
            else if (word[i] == '4') {word[i] = 'a';}
            else if (word[i] == '3') {word[i] = 'e';}
            else if (word[i] == '0') {word[i] = 'o';}
            else if (word[i] == '1') {word[i]= 'l';}
            else if (word[i] == '7') {word[i] = 't';}
            if (Character.isLetter(word[i])) {cleanWord += word[i];}
        }
        return cleanWord;    
    }
}
