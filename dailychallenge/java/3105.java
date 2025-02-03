class Solution {
    public int longestMonotonicSubarray(int[] nums) {
        int longestLength = 2;
        int currentLength = 2;
        byte state; // tri-state variable (0-2)

        if(nums.length == 1)
            return 1;
        else if(nums[1] > nums[0])
            state = 0; // increasing
        else if(nums[1] == nums[0]) {
            state = 1; // stagnant, need to restart state
            longestLength = 1;
            currentLength = 1;
        }
        else
            state = 2; // decreasing

        for(int i = 2; i < nums.length; i++) {
            if(nums[i] > nums[i-1]) { // currently increasing
                if(state == 0) { // prev state was increasing
                    currentLength++;
                }
                else if (state == 1) { // prev state was stagnant
                    if(currentLength > longestLength) { // test on state change
                        longestLength = currentLength;
                    }

                    currentLength = 2;
                }
                else {  // prev state was decreasing
                    if(currentLength > longestLength) { // test on state change
                        longestLength = currentLength;
                    }

                    currentLength = 2;
                }

                state = 0;
            }
            else if(nums[i] == nums[i-1]) { // currently stagnant
                if(currentLength > longestLength) { // test on state change
                    longestLength = currentLength;
                }

                currentLength = 1;
                state = 1;
            }
            else { // currently decreasing
                if(state == 2) { // prev state was decreasing
                    currentLength++;
                }
                else if (state == 1) { // prev state was stagnant
                    if(currentLength > longestLength) // test on state change
                        longestLength = currentLength;

                    currentLength = 2;
                }
                else { // prev state was decreasing
                    if(currentLength > longestLength) // test on state change
                        longestLength = currentLength;

                    currentLength = 2;
                }

                state = 2;
            }
        }

        if(currentLength > longestLength) { // edge case: change on last element
            longestLength = currentLength;
        }

        // return the length of longest
        return longestLength;
    }
}