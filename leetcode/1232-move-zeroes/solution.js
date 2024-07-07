/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    i = 0;
    count = 0;
    
    while (count < nums.length) {
        count++
        if (nums[i] == 0) {
            nums.splice(i, 1);
            nums.push(0);
            continue;
        }
        i++
    }
};

// Runtime: 60 ms, faster than 84.20% of JavaScript online submissions for Move Zeroes.
// Memory Usage: 35.8 MB, less than 57.45% of JavaScript online submissions for Move Zeroes.