class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> hm = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            if (hm.containsValue(nums[i])) {
                return true;
            }
            hm.put(i, nums[i]);
        }
        
        return false;
    }
}