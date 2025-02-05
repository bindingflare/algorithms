class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        if(Math.abs(s1.length() - s2.length()) > 2)
            return false;

        int firstDiff = -1;
        int nextDiff = -1;

        for(int i = 0; i < s1.length(); i++) {
            char ch1 = s1.charAt(i);
            char ch2 = s2.charAt(i);

            if(ch1 != ch2) {
                if(firstDiff != -1)
                    return false;

                firstDiff = nextDiff;
                nextDiff = i;
            }
        }
        
        if(nextDiff == -1)
            return true;
        else if(firstDiff == -1)
            return false;
        else if(s1.charAt(firstDiff) == s2.charAt(nextDiff) && s1.charAt(nextDiff) == s2.charAt(firstDiff))
            return true;

        return false;
    }
}