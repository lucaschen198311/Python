"""
  Acronyms
  Create a function that, given a string, returns the string’s acronym 
  (first letter of each word capitalized). 
  Do it with .split first if you need to, then try to do it without
*/

const str1 = " there's no free lunch - gotta pay yer way. ";
const expected1 = "TNFL-GPYW";

const str2 = "Live from New York, it's Saturday Night!";
const expected2 = "LFNYISN";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The given str converted into an acronym.
 */
function acronymize(str) {}

// **************************************************************************

"""
def acronymize(str):
    arr = str.split(" ")
    str1 = ""
    for i in range(len(arr)):
        if arr[i]:
            str1 += arr[i][0].upper()
    return str1

def acronymize_1(str):
    str1  = str[0].upper() if str[0]!=" " else ""
    for i in range(1,len(str)):
        if str[i-1] == " ":
            str1 += str[i].upper()
    return str1




"""
/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {}

module.exports = { reverseString };\

"""
def reverseString(str):
    return str[::-1]