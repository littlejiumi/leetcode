class Solution {
    public char firstUniqChar(String s) {
        HashMap<Character, Boolean> map = new HashMap<>();
        char[] charString = s.toCharArray();
        for(char c : charString){
            map.put(c, !map.containsKey(c));
        }
        for(char c : charString){
            if(map.get(c)) return c;
        }
        return ' ';
    }
}
