



/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {

    //string sorter function
    function stringSorter(s){
        return s.split("").sort().join("");
    }

    let hashMap = new Map();
    for (let i = 0; i < strs.length ; i+= 1){
        let sorted = stringSorter(strs[i]);
        if(hashMap.has(sorted)){
            hashMap.set(sorted,[...hashMap.get(sorted), strs[i]] );
        } else {
            hashMap.set(sorted, [strs[i]]);
        }
    }
    return [...hashMap.values()];
    
};



strs = ["eat","tea","tan","ate","nat","bat"]
console.log(groupAnagrams(strs));