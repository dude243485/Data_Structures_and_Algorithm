/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let left = 0, right = s.length - 1;
    const isAlphanumeric = char => /^[a-z0-9]+$/i.test(char);

    while (right > left){
        if(!isAlphanumeric(s.charAt(left))){
            left += 1
            continue;
        }

        if (!isAlphanumeric(s.charAt(right))){
            right -= 1
            continue;
        }

        if(s.charAt(left).toLowerCase() !== s.charAt(right).toLowerCase()){
            return false;
        }
        right -= 1;
        left += 1;
    }
    return true;
};