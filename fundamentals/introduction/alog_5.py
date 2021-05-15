"""
keys1 = ["abc", 3, "yo"];
  const vals1 = [42, "wassup", true];
  const expected1 = {
    abc: 42,
    3: "wassup",
    yo: true,
  };
  
  /**
   * Converts the given arrays of keys and values into an object.
   * - Time: O(?).
   * - Space: O(?).
   * @param {Array<string>} keys
   * @param {Array<any>} values
   * @returns {Object} The object with the given keys and values.
   */
"""

def zipArraysIntoMap(keys, values):
    if len(keys)!= len(values):
        return
    dict_zip = {}
    for i in range(len(keys)):
        dict_zip[keys[i]] = values[i]
    return dict_zip


keys = ["abc", 3, "yo"];
values = [42, "wassup", True];
print(zipArraysIntoMap(keys, values))


"""
// **************************************************************************************************************************************************
// **************************************************************************************************************************************************
// **************************************************************************************************************************************************

  /* 
  Invert Hash
  A hash table / hash map is an obj / dictionary
  Given an object / dict,
  return a new object / dict that has the keys and the values swapped so that the keys become the values and the values become the keys
*/

const obj1 = { name: "Zaphod", charm: "high", morals: "dicey" };
const expected1 = { Zaphod: "name", high: "charm", dicey: "morals" };

/**
 * Inverts the given object's key value pairs so that the original values
 * become the keys and the original keys become the values.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Object<string, string>} obj An object with string keys and string values.
 * @return The given object with key value pairs inverted.
 */
"""
def invertObj(obj):
    dict_invert = {}
    for key, value in obj.items():
        dict_invert[value] = key
    return dict_invert
obj1 = { 'name': "Zaphod", 'charm': "high", 'morals': "dicey" }
print(invertObj(obj1))



def convertToDict(arr):
  new_dict = {} 
  for key in arr:
    if key not in new_dict:
      new_dict[key] = 1
    else:
      new_dict[key] += 1
  return new_dict

print(convertToDict(["a", "b", "c", "b", "a"]))
print(convertToDict([]))