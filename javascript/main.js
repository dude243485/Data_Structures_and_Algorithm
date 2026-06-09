/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let hashMap = new Map();

    for (let i = 0; i < nums.length; i += 1){

        let num = nums[i];
        if (hashMap.has(-(num - target))){
            return [hashMap.get(-(num - target)), i];
        }
        
        hashMap.set(num, i);
    }
};