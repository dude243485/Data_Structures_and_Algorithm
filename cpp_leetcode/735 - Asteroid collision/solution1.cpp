#include <vector>
#include <cmath>
#include <iostream>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        int n = asteroids.size();
        stack<int> stk;
        stk.push(asteroids[0]);

        for (int i = 1; i < n; i++) {
            bool destroyed = false;

            while (!stk.empty() && stk.top() > 0 && asteroids[i] < 0) {
                int absNew = -asteroids[i];
                int absTop = stk.top();

                if (absNew > absTop) {
                    stk.pop(); // incoming destroys stack top, keep checking
                } else if (absNew == absTop) {
                    stk.pop(); // mutual destruction
                    destroyed = true;
                    break;
                } else {
                    destroyed = true; // stack top survives
                    break;
                }
            }

            if (!destroyed) {
                stk.push(asteroids[i]);
            }
        }

        vector<int> ans;
        while (!stk.empty()) {
            ans.push_back(stk.top());
            stk.pop();
        }
        reverse(ans.begin(), ans.end());

        return ans;
    }
};