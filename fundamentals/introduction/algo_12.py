"""
/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "         ";
const expected2 = "";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
"""
def trim(str):
    if len(str)<1:
        return str
    left = 0
    right = len(str)-1
    while (str[right]==" " or str[left] ==" " ) and right>left:
        if str[right] ==" ":
            right -= 1
        if str[left] == " ":
            left += 1
    return str[left:right+1]

print(trim("   hello world     "))

"""
// ************************************************************************

/* 
  Given an array of integers
  return the first integer from the array that is not repeated anywhere else
  If there are multiple non-repeated integers in the array,
  the "first" one will be the one with the lowest index.
*/

const nums11 = [3, 5, 4, 3, 4, 6, 5];
const expected11 = 6;

const nums12 = [3, 5, 5];
const expected12 = 3;

const nums13 = [3, 3, 5];
const expected13 = 5;

const nums14 = [5];
const expected14 = 5;

const nums15 = [];
const expected15 = null;

const nums16 = [3, 5, 4, 3, 4, 6, 5, 7];
const expected16 = 6;

/**
 * Finds the first int from the given array that has no duplicates. I.e., the
 *    item at the lowest index that doesn't appear again in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number|null} The first int value from the given array that has no
 *    dupes or null if there is none.
 */
"""
def firstNonRepeated(nums):
    if len(nums)<1:
        return None
    letterdict = {}
    for i in range(len(nums)):
        letterdict[nums[i]] = letterdict[nums[i]] + 1 if nums[i] in letterdict else 1
    for i in range(len(nums)):
        if letterdict[nums[i]] == 1:
            return nums[i]
    return None

print(firstNonRepeated([]))
