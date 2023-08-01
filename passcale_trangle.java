
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>();
        
        for (int i = 0; i < numRows; i++) {
            List<Integer> row = new ArrayList<>();
            
            for (int j = 0; j <= i; j++) {
                int element = pascalTriangle(i, j);
                row.add(element);
            }
            
            triangle.add(row);
        }
        
        return triangle;
    }

    // Calculate the element at position (r, c) in Pascal's Triangle using combination formula.
    public static int pascalTriangle(int r, int c) {
        long res = 1;
        
        // calculating nCr:
        for (int i = 0; i < c; i++) {
            res = res * (r - i);
            res = res / (i + 1);
        }
        
        return (int) res;
    }
}
