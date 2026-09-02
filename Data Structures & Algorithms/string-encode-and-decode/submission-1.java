class Solution {

    public String encode(List<String> strs) {
        if(strs.isEmpty()) return "";
        StringBuilder encodedStr = new StringBuilder();
        for(String str : strs)
        {
            encodedStr.append(Integer.toString(str.length()));
            encodedStr.append('#');
            encodedStr.append(str);
        }

        return encodedStr.toString();
    }

    public List<String> decode(String str) {
        ArrayList<String> decoded = new ArrayList<>();
        int i = 0;
        while (i < str.length())
        {
            int j = i;
            while (str.charAt(j) != '#')
            {
                j++;
            }
            int length = Integer.parseInt(str.substring(i, j));

            i = j+1;
            j = i + length;

            decoded.add(str.substring(i, j));
            i = j;
        }

        return decoded; 
    }
}
