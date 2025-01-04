class Solution {
    public int countPalindromicSubsequence(String s) {
        int CHAR_COUNT = 26;
        // int[] counts = new int[CHAR_COUNT];
        int[] first = new int[CHAR_COUNT];
        int[] last = new int[CHAR_COUNT];

        for (int i = 0; i < 26; i++) {
            first[i] = -1;
        }

        // Count occurance of each char
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            
            // if (c >= 'a' && c <= 'z') {
                int index = c - 'a';
                // counts[c - 'a']++;

                // Set the first occurrence if it's the first time
                if (first[index] == -1) {
                    first[index] = i;
                }
                
                // Update the last occurrence every time
                last[index] = i;
            // }
        }

        // int hits = 0;
        // for (int i = 0; i < CHAR_COUNT; i++) {
        //     if (counts[i] > 1) {
        //         for (int j = 0; j < CHAR_COUNT; j++) {
        //             if (counts[j] > 0) {
        //                 hits++;
        //             }
        //         }
        //     }
        // }

        int hits = 0;
        for (int i = 0; i < CHAR_COUNT; i++) {
            if (last[i] != 0) {
                HashSet<Character> uniqueChars = new HashSet<>();

                // Iterate over the substring between the specified indexes
                for (int j = first[i] + 1; j < last[i]; j++) {
                    char c = s.charAt(j);
                    // if (c >= 'a' && c <= 'z') {  // Only consider 'a' to 'z'
                        uniqueChars.add(c);
                    // }
                }

                hits += uniqueChars.size();
            }
        }

        return hits;
    }
}