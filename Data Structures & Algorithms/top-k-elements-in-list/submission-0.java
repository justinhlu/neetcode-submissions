class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums)
        {
            freqMap.putIfAbsent(num, 0);
            freqMap.put(num, freqMap.get(num) + 1);
        }

        List<int[]> arr = new ArrayList<>();
        for (Map.Entry<Integer,Integer> entry : freqMap.entrySet())
        {
            arr.add(new int[] {entry.getValue(), entry.getKey()});
        }
        arr.sort((a,b) -> b[0] - a[0]);

        int[] kList = new int[k];

        for (int i = 0; i < k; i++)
        {
            kList[i] = arr.get(i)[1];
        }
        return kList;
    }
}
