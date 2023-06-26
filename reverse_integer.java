class Solution {
    public int reverse(int x) {
        int sum=0;
        while(x!=0){
            int rem=x%10;
            if((sum>Intiger.INT_MAX/10)||(sum>Intiger.INT_MAX/10)){ //this line check for given the value is range of the interger.
              return 0;
            }
            sum=sum*10+rem;
            x=x/10;

        }
        
    }
}

