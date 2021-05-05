"""
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

  const str1 = "aaaabbcddd";
  const expected1 = "a4b2c1d3";
  
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "bbcc";
  const expected4 = "bbcc";
  
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs only if the
   * character occurs more than two time.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
"""
def encodeStr(input):
    if input == None or input == " ":
        return ""
    hashMap = {}
    str1 = ""
    for letter in input:
        if letter not in hashMap:
            hashMap[letter] = 1
        else:
            hashMap[letter] += 1
    for letter in input:
        if letter not in str1:
            str1 += letter
            str1 += str(hashMap[letter])
    return str1 if len(str1) < len(input) else input

print(encodeStr("bbcc"))
print(encodeStr("aaaabbcdddaa")) 
        

"""
//   ***************************************************************************************************************

  /* 
  String Decode  
*/

const str1 = "a3b2c1d3";
const expected1 = "aaabbcddd";

const str2 = "a3b2c12d10";
const expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
 """
def decodeStr(input):
    expected = ""
    begin_index = 0
    end_index = 1
    while end_index < len(input):
        letter = input[begin_index]
        if input[end_index].isnumeric():
            end_index += 1
        else:
            expected += letter * int(input[begin_index+1:end_index])
            begin_index = end_index
            end_index += 1
    expected += input[begin_index] * int(input[begin_index+1:])
    return expected

print(decodeStr("a3b2c12d10"))