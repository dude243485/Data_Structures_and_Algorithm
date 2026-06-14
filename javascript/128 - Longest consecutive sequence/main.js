/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    if (nums.length === 0){
        return 0;
    }

    let hashSet = new Set(nums);
    let maxCount = 1;

    for (let num of hashSet){
        if (!hashSet.has(num - 1)){
            let count = 1;
            while (hashSet.has(num + count)){
                count += 1;
            }
            maxCount = Math.max(maxCount, count);
        }
    }
    return maxCount;
    
};