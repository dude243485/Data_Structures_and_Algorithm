#include <vector>
#include <iostream>
#include <string>
using namespace std;

class Solution {
    public:
        vector<string> cellsInRange(string s) {
            vector<string> res ;

            for (char col = s[0]; col < s[3]; col++){
                for (char row = s[1]; row <= s[4]; row++){
                    string cell = "";
                    cell += col;
                    cell += row;
                    res.push_back(cell);
                }
            }

            return res;
            
        }
};