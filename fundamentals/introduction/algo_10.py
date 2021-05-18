"""
(1) find the mid index value in sorted array (left pointer at index =0 , right pointer at index=len-1)
(2) compare its value to target
(3) if mid value == tageget, return true
(4) if mid value > target, right pointer move to mid - 1
(5) if mid value < target, left pointer move to mid + 1
(6) repeat step 1-5 until find target or return False when left pointer>right pointer
/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true;

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true;

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

const nums5 = [1,3,4,5,8,9,11,13,14,15,19,22,26,27,31,35,37]
const searchNum5 = 8;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
"""
def binarySearch(sortedNums, searchNum):
    left = 0
    right = len(sortedNums)-1
    while left<=right:
        mid = (left+right)//2
        if sortedNums[mid] == searchNum:
            l=mid
            r = mid
            while l>=0 and r<len(sortedNums) and (sortedNums[l] == searchNum or sortedNums[r] ==searchNum):
                if sortedNums[l] == searchNum:
                    l -= 1
                if sortedNums[r] ==searchNum:
                    r += 1
            return r-l -1
        elif sortedNums[mid] > searchNum:
            right = mid -1
        else:
            left = mid +1
    return False

print(binarySearch([1, 3, 5, 6], 4))
    

"""
/* 
  Given two arrays, interleave them into one new array.
  The arrays may be different lengths. The extra items should be added to the
  back of the new array.
*/

const arrA1 = [1, 2, 3];
const arrB1 = ["a", "b", "c"];
const expected1 = [1, "a", 2, "b", 3, "c"];

const arrA2 = [1, 3];
const arrB2 = [2, 4, 6, 8];
const expected2 = [1, 2, 3, 4, 6, 8];

const arrA3 = [1, 3, 5, 7];
const arrB3 = [2, 6];
const expected3 = [1, 2, 3, 6, 5, 7];

const arrA4 = [];
const arrB4 = [42, 0, 6];
const expected4 = [42, 0, 6];

/**
 * Interleaves two arrays into a new array. Interleaving means alternating
 * the items starting from the first array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<any>} arr1
 * @param {Array<any>} arr2
 * @returns {Array<any>} A new array of interleaved items.
 */
function interleaveArrays(arr1, arr2) {}

"""