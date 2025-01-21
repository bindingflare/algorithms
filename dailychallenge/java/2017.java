class Solution {
    public long gridGame(int[][] grid) {
        int size = grid[0].length;
        if(size == 1)
            return 0;

        long[][] prefixSum = new long[2][size];

        long sum = 0;
        long sum2 = 0;
        for(int i = 0; i < size; i++) {
            sum += grid[1][i];
            sum2 += grid[0][size - i - 1];
            
            prefixSum[1][i] = sum;
            prefixSum[0][size - i - 1] = sum2;
        }

        // Print values
        // for(int i = 0; i < size; i++) {
        //     System.out.print(prefixSum[0][i] + " ");
        // }
        // System.out.println();
        
        // for(int i = 0; i < size; i++) {
        //     System.out.print(prefixSum[1][i] + " ");
        // }
        // System.out.println();

        long newMaxCost = Math.min(prefixSum[0][1], prefixSum[1][size - 2]);
        // System.out.println("Best bot 2 can do here is " + newMaxCost);

        // Check availalble choices for robot 2
        for(int i = 1; i < size - 1; i++) {
            long maxCost = Math.max(prefixSum[0][i + 1], prefixSum[1][i - 1]);

            // System.out.println("Best bot 2 can do here is " + maxCost);

            if(newMaxCost > maxCost)
                newMaxCost = maxCost;
        }

        return newMaxCost;
    }
}