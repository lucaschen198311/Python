
/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
 
let sum = 0;
function sumArr(nums){
    if(nums.length==0){
        return sum;
    }
    let a = nums.pop();
    sum += a;
    return sumArr(nums);
}

console.log(sumArr([1, 2, 3]));

// ******************************************************************************
// ******************************************************************************
// ******************************************************************************

/* 
  Recursive Sigma
  Input: integer
  Output: sum of integers from 1 to Input integer
*/

const num10 = 5;
const expected10 = 15;
// Explanation: (1+2+3+4+5)

const num11 = 2.5;
const expected11 = 3;
// Explanation: (1+2)

const num12 = -1;
const expected12 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
let sum =0;
function recursiveSigma(num) {
    if(num<0){
        return sum;
    }
    if(Number.isInteger(num)!==true){
        return Math.ceil(num);
    }
    
    sum += num;
    return recursiveSigma(num-1);
}
console.log(recursiveSigma(5));