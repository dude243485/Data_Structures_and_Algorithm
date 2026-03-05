#include <vector>
#include <cmath>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int n = arr.size();
        int left = 0;
        int right = n -1;

        while ((right-left + 1) > k) {
            int diffLeft = abs(arr[left] - x);
            int diffRight = abs(arr[right] - x);

            if (diffLeft > diffRight){
                left ++;
            } else {
                right --;
            }
        }

        return vector<int>(arr.begin() + left, arr.begin() + right + 1);
        
    }
};

int main () {

    Solution test ;
    vector<int> input = { 1,1,2,3,4,5};
    vector<int> output = test.findClosestElements(input, 4, -1);

    //output the solution   
    for (int i : output){
        cout << i << ", " ; 
    }
    cout << endl;
    return 0;
}