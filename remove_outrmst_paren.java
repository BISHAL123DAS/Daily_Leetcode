class Solution {
    public String removeOuterParentheses(String s) {
        Stack<Character> st = new Stack<>();
        String ans="" ;
        int i=0;
        int n=s.length();
        for(i=0;i<n;i++){
            if(s.charAt(i)=='('){
                if(st.size()>0){
                    ans+=s.charAt(i);
                }
                st.push(s.charAt(i));
            }
            else{
                st.pop();
                if(st.size()>0){
                    ans+=s.charAt(i);
                }
            }
        }
       return ans; 
    }
}