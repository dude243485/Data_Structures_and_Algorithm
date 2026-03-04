#include <vector>
#include <iterator>

using namespace std;
class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();

        int temp = -1;
        int dummy_data = 1e6;

        for (int i =1 ; i <= n; i++) {
            if (nums[i - 1] >= 1 && nums[i - 1] <= n) {
                if (nums[i-1] == i){
                    nums[i-1] = dummy_data;
                    continue;
                }
                if(nums[nums[i-1] - 1] == dummy_data){
                    nums[i-1] = -1;
                    continue;
                }

                temp = nums[nums[i-1] -1];
                nums[nums[i-1] -1] = dummy_data;
                nums[i-1] = temp;
                i --;
            } else if(nums[i-1] != dummy_data) nums[i-1] = -1;
        }
        int ans = 1;
        for (ans = 1; ans <= n; ans++){
            if (nums[ans-1] != dummy_data) break;
        }

        return ans;
    }
};