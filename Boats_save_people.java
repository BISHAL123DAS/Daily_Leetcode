class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int count=0;
        int l=0;int r=people.length-1;
        while(l<=r){
            if(people[l]+people[r]<=limit){
                l+=1;r-=1;
            }
            else{
                r-=1;
            }
            count+=1;
        }
        return count;
    }
}