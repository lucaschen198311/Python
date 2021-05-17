"""
/* 
  Balance Index
  Here, a balance point is ON an index, not between indices.
  Return the balance index where sums are equal on either side
  (exclude its own value).
  
  Return -1 if none exist.
  
*/

const nums1 = [-2, 5, 7, 0, 3];
const expected1 = 2;

const nums2 = [9, 9];
const expected2 = -1;

/**
 * Finds the balance index in the given array where the sum to the left of the
 *    index is equal to the sum to the right of the index.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The balance index or -1 if there is none.
 */
"""
def balanceIndex(nums):
    if len(nums)<3:
        return -1
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    for i in range(1, len(nums)-1):
        if nums[i-1] == nums[len(nums)-1] -nums[i]:
            return i
    return -1

print(balanceIndex([-2, 5, 7, 0, 3]))


"""
// **********************************************************************
// **********************************************************************
// **********************************************************************


/* 
  Balance Point
  Write a function that returns whether the given
  array has a balance point BETWEEN indices, 
  where one side’s sum is equal to the other’s. 
*/

const nums1 = [1, 2, 3, 4, 10];
const expected1 = true;
// Explanation: between indices 3 & 4

const nums2 = [1, 2, 4, 2, 1];
const expected2 = false;

/**
 * Determines if there is a balance point BETWEEN indexes where the sum of the
 *    left side is equal to the sum of the right side of the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {boolean} Indicates if a balance point exists.
 */
"""
def balancePoint(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    for i in range(1, len(nums)-1):
        if nums[i] == nums[len(nums)-1] - nums[i]:
            return True
    return False

print(balancePoint( [1, 2, 4, 2, 1]))
