import java.util.HashMap;

class Solution {
    public int[] lexicographicallySmallestArray(int[] nums, int limit) {
        HashMap<Integer, Deque<Integer>> nodes = new HashMap<>();

        // Sort the array
        int[] sorted = nums.clone();
        Arrays.sort(sorted);

        // Construct nodes with pairs (edges)
        for(int i = 0; i < sorted.length; i++) {
            int end = i;

            // Construct all possible values that can be switched with this node (number) with any n number of operations
            Deque<Integer> connectedPairs = new ArrayDeque<>();
            connectedPairs.addLast(sorted[end]);

            if(end != sorted.length - 1) {
                while(Math.abs(sorted[end + 1] - sorted[end]) <= limit)
                {
                    end++;
                    connectedPairs.addLast(sorted[end]);

                    if(end == sorted.length - 1)
                        break;
                }
            }

            for(int j = i; j <= end; j++) {
                nodes.put(sorted[j], connectedPairs);
            }
            i = end;
        }

        // 
        int[] answer = new int[nums.length];
        for(int i = 0; i < nums.length; i++) {
            int number = nums[i];
            Deque<Integer> pairs = nodes.get(number); 
            // System.out.println(number);

            // Find the minimum to remove
            int minNumber = pairs.pollFirst();
            answer[i] = minNumber;
            // System.out.println("Minimum is " + minNumber);
        }

        return answer;
    }
}