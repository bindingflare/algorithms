class Solution {
    public int maxAscendingSum(int[] nums) {
        if(nums.length == 1)
            return nums[0];

        int maxSum = nums[0];
        int sum = nums[0];

        for(int i = 1; i < nums.length; i++) {
            if(nums[i] > nums[i-1]) {
                sum += nums[i];
            }
            else {
                if(maxSum < sum)
                    maxSum = sum;
                
                sum = nums[i];
            }
        }

        if(maxSum < sum) // test one last time
            maxSum = sum;

        return maxSum;
    }
}