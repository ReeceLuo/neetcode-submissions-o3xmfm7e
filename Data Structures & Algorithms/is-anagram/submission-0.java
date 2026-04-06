class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        HashMap<Character, Integer> hms = new HashMap<>();
        HashMap<Character, Integer> hmt = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            hms.put(s.charAt(i), hms.getOrDefault(s.charAt(i), 0) + 1);
            hmt.put(t.charAt(i), hmt.getOrDefault(t.charAt(i), 0) + 1);

        }

        return hms.equals(hmt);
    }
}
