class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i=0; i<nums.length; i++)
        {
            map.put(nums[i], i);
        }

        for(int i=0; i<nums.length; i++)
        {
            int difference = target - nums[i];
            if (map.get(difference) != null && map.get(difference) != i)
            {
                return new int[]{i, map.get(difference)};
            }
        }

        return new int[2];
    }
}
