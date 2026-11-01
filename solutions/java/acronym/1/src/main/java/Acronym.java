/** Builds an acronym; words are split by spaces or hyphens, other punctuation is ignored. */
class Acronym {
    private final String phrase;

    Acronym(String phrase) {
        this.phrase = phrase;
    }

    /** @return the acronym in upper case, e.g. "PNG" */
    String get() {
        String clean = phrase.replaceAll("[^a-zA-Z\\s-]", "").replaceAll("^[\\s-]+", "");
        String[] result = clean.split("[\\s-]+");
        StringBuilder resultString = new StringBuilder();
        for (String res : result){
            resultString.append(res.charAt(0));
        }
        return resultString.toString().toUpperCase();
    }
}
