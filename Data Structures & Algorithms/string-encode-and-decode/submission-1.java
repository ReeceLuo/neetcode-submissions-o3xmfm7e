class Solution {

    public String encode(List<String> strs) {
        String encoded = "";
        for (String str : strs) {
            encoded += str;
            encoded += '|';
        }
        return encoded;
    }

    public List<String> decode(String str) {
        List<String> decoded = new ArrayList<>();
        String currString = "";
        for (int i = 0; i < str.length(); ++i) {
            if (str.charAt(i) == '|') {
                decoded.add(currString);
                currString = "";
            } else {
                currString += str.charAt(i);
            }
        }

        return decoded;
    }
}
