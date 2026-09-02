class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> anagramMap = new HashMap<>();

        for (String str : strs) {
            int[] count = new int[26];
            char[] strChars = str.toCharArray();
            for (char c : strChars)
            {
                count[c - 'a']++;
            }
            String countStr = Arrays.toString(count);
            anagramMap.putIfAbsent(countStr, new ArrayList<>());
            List<String> anaList = anagramMap.get(countStr);
            anaList.add(str);
        }
        
        List<List<String>> anagrams = new ArrayList<>(anagramMap.values());

        return anagrams;
    }
}
