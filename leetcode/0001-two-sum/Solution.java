import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
class Solution {

    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        System.out.println(Arrays.toString(twoSum(nums, target)));
    }

    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        int[] result = {-1,-1};
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                result[0] = map.get(complement);
                result[1] = i;
            }
            map.put(nums[i], i);
        }
        return result;
    }
}

// Runtime: 3 ms (faster than 50.43% of online Java submissions)
// Memory: 36.9 MB (less than 99.08% of online Java submissions)