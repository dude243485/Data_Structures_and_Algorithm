import java.util.HashMap;
class two_sum {
    public int[] twoSum(int[] nums, int target) {
        //create a new hashmap
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int key = target - nums[i];
            if (map.containsKey(key)){
                return new int[] {map.get(key), i};
            }
            map.put(nums[i], i);
            
        }
        return new int[] {0, 0};
    }
    public static void main(String[] args) {

        //testing the algorithm/function
        int[] nums = {2,7,11,15};
        int target = 9;
        two_sum test = new two_sum();
        int[] solution = test.twoSum( nums, target);

        //displaying the array
        for (int i : solution){
            System.out.print(i);
        }System.out.println();

    }
}