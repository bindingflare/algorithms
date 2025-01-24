import java.util.HashMap;

class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        Deque<Integer> queue = new ArrayDeque<>();
        HashMap<Integer, List<Integer>> parents = new HashMap<>();
        int[] adjacency = new int[graph.length];
        
        for(int i = 0; i < graph.length; i++) {
            parents.put(i, new ArrayList<Integer>());
            int childCount = graph[i].length;

            if(childCount == 0)
                queue.addLast(i);
            else
                adjacency[i] += childCount;
        }

        for(int i = 0; i < graph.length; i++) {
            for(int j : graph[i]) {
                parents.get(j).add(i);   
            }
        }

        // Print values
        // for (Map.Entry<Integer, ArrayList<Integer>> entry : parents.entrySet()) {
        //     System.out.print("Key: " + entry.getKey() + ", Value: ");
        //     for (int val : entry.getValue()) {
        //         System.out.print(val + " ");
        //     }
        //     System.out.println();
        // }

        boolean[] safe = new boolean[graph.length];
        while(!queue.isEmpty()) {
            int index = queue.pop();
            safe[index] = true;

            for(int i : parents.get(index)) {
                adjacency[i]--;

                if(adjacency[i] == 0) {
                    queue.addLast(i);
                }
            }

            // Print visited status
            // System.out.print("Visited check: ");
            // for(int i : visited) {
            //     System.out.print(i + "");
            // }
            // System.out.println();
        }

        List<Integer> safeList = new ArrayList<>();
        for (int i = 0; i < graph.length; i++) {
            if(safe[i])
                safeList.add(i);
        }

        return safeList;
    }
}