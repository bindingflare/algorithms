import java.util.AbstractMap.SimpleEntry;

class Solution {
    public int[][] highestPeak(int[][] isWater) {
        int rows = isWater.length;
        int cols = isWater[0].length;

        int[][] peakMap = new int[rows][cols];
        // Utilize queue mechanism since update/ increment order is important
        Deque<SimpleEntry<Integer, Integer>> queue = new ArrayDeque<>();

        for(int i = 0; i < rows; i++) {
            for(int j = 0; j < cols; j++) {
                if(isWater[i][j] == 1) {
                    queue.addLast(new SimpleEntry<Integer, Integer>(i, j));
                    peakMap[i][j] = 0;
                }
                else
                    peakMap[i][j] = -1; // set to unset value
            }
        }

        while (!queue.isEmpty()) {
            Map.Entry<Integer, Integer> entry = queue.pop();
            int row = entry.getKey();
            int col = entry.getValue();

            int incVal = peakMap[row][col] + 1;

            // System.out.println("Checking " + row + "," + col + ": val is " + incVal);

            // Increment nearby cells
            if(row < rows - 1) {
                // System.out.println(" - " + (row + 1) + "," + col); 
                if(peakMap[row + 1][col] == -1)
                {
                    peakMap[row + 1][col] = incVal;
                    queue.addLast(new SimpleEntry<Integer, Integer>(row + 1, col));
                    
                }
            }
            if(col < cols - 1) {
                // System.out.println(" - " + row + "," + (col + 1)); 
                if(peakMap[row][col + 1] == -1) {
                    peakMap[row][col + 1] = incVal;
                    queue.addLast(new SimpleEntry<Integer, Integer>(row, col + 1));
                }
            }
            if(row != 0) {
                // System.out.println(" - " + (row - 1) + "," + col); 
                if(peakMap[row - 1][col] == -1) {
                    peakMap[row - 1][col] = incVal;
                    queue.addLast(new SimpleEntry<Integer, Integer>(row - 1, col));
                }
            }
            if(col != 0) {
                // System.out.println(" - " + row + "," + (col - 1)); 
                if(peakMap[row][col - 1] == -1) {
                    peakMap[row][col - 1] = incVal;
                    queue.addLast(new SimpleEntry<Integer, Integer>(row, col - 1));
                }
            }
        }

        return peakMap;
    }
}