class MicroBlog {


    /**
     * Truncates the input to at most 5 characters.
     * Counts Unicode code points, so emojis (surrogate pairs) are never cut in half.
     *
     * @param input the post to truncate
     * @return the first 5 code points of the input, or the whole input if it is shorter
     */
    public String truncate(String input) {
        int codePointsToKeep = Math.min(5, input.codePointCount(0, input.length()));
        int endIndex = input.offsetByCodePoints(0, codePointsToKeep);
        return input.substring(0, endIndex);
    }
}
