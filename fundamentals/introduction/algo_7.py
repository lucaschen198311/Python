"""
/* 
  Given a string,
  return a new string with the duplicates excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
 
"""
"""
def stringDedupe(str):
    if len(str)<2:
        return str
    left = 0
    right = 1
    new_str = ""
    while left<right and right<len(str):
        if str[left]!=str[right]:
            new_str += str[left]
            left += 1
            right += 1
        else:
            while str[right]==str[left] and right<len(str):
                right += 1
            left = right-1
    if str[-1]==new_str[-1]:
        return new_str
    else:
        return new_str + str[-1]

print(stringDedupe("helloo"))
        
"""
def stringDedupe(str):
    new_str=""
    new_set = set()
    for letter in str:
        if letter not in new_set:
            new_set.add(letter)
            new_str += letter
    return new_str
print(stringDedupe("helloo"))
