
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> usedInteger = new HashSet<>();
       
        while (true) {
            int sum=0;
            while (n >0) {
                int digit = n % 10;
                sum += Math.pow(digit, 2);
                n /= 10;
            }
            if (sum == 1) {
                return true;
            }
            if (usedInteger.contains(sum)) {
                return false;
            }
            usedInteger.add(sum);
            n = sum; // Update n with the new sum
            sum = 0; // Reset sum for the next iteration
        }
    }
}