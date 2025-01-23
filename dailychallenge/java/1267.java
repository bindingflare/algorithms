import java.util.AbstractMap.SimpleEntry;

class Solution {
    public int countServers(int[][] grid) {
        int[] rowServerCount = new int[grid.length];
        int[] colServerCount = new int[grid[0].length];

        Deque<SimpleEntry<Integer, Integer>> queue = new ArrayDeque<>();

        int total = 0;
        for(int i = 0; i < grid.length; i++) {
            int lastFoundInRow = 0;
            for(int j = 0; j < grid[0].length; j++) {
                if(grid[i][j] == 1) {
                    rowServerCount[i] += grid[i][j];
                    colServerCount[j] += grid[i][j];
                    lastFoundInRow = j;
                }
            }

            if(rowServerCount[i] == 1)
                queue.addLast(new SimpleEntry<Integer, Integer>(i, lastFoundInRow));

            total += rowServerCount[i];
        }

        // Print server counts
        // for(int i = 0; i < grid.length; i++) {
        //     System.out.print(rowServerCount[i] + " ");
        // }
        // System.out.println();
        // for(int i = 0; i < grid.length; i++) {
        //     System.out.print(colServerCount[i] + " ");
        // }
        // System.out.println();

        // Test isolation
        int isolateCount = 0;
        while(!queue.isEmpty()) {
            SimpleEntry<Integer, Integer> entry = queue.pop();
            if(rowServerCount[entry.getKey()] == 1 && colServerCount[entry.getValue()] == 1)
                isolateCount++;
        }

        return total - isolateCount;
    }
}