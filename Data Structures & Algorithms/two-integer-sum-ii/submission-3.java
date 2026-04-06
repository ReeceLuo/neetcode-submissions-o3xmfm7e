class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int lower = 0, upper = numbers.length - 1;

        while (lower < upper) {

            if ((numbers[lower] + numbers[upper]) > target) {
                upper--;
            } else if ((numbers[lower] + numbers[upper]) < target) {
                lower++;
            } else {
                return new int[] {lower + 1, upper + 1};
            }
        }
        return new int[0];
    }
}
