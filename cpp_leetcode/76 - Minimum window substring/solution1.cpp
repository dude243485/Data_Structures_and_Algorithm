#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <limits>

using namespace std;

class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty()) {
            return "";
        }
        //create the hashmaps
        unordered_map<char, int> countT;
        unordered_map<char, int> window;

        for (char c : t){
            if (countT.count(c)){
                countT[c] = countT[c] + 1;
            } else{
                countT[c] = 1;
            }
        }

        //create counter variables
        int have = 0;
        int need = countT.size();;
        vector<int> res = { -1, -1};
        double inf = numeric_limits<double>::infinity();
        double resLen = inf; //infinity
        int l = 0;

        for (int r = 0; r < s.length(); r++){
            char c = s[r];

            if (window.count(c)){
                window[c] = window[c] + 1;
            } else {
                window[c] = 1;
            }

            if (countT.count(c) && window[c] == countT[c]){
                have ++;
            }

            while ( have == need){
                if ((r - l + 1) < resLen) {
                    res = {l, r};
                    resLen = ( r - l + 1 );
                }
                window[s[l]] = window[s[l]] - 1;
                if(countT.count(s[l]) && window[s[l]] < countT[s[l]]){
                    have --;
                }
                l ++;

            }
        }
        l = res[0];
        int r = res[1];
        if (resLen != inf ){
            return s.substr(l, r - l + 1);
        } else{
            return "";
        }   
    }
};