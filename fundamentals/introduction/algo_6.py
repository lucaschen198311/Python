
"""
/* 
  Parens Valid
    Given an str that has parenthesis in it
    return whether the parenthesis are valid
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the underlined ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing

/**
 * Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the parenthesis are valid.
 */
 
"""

str1 = "Y(3(p)p(3)r)s"
str2 = "N(0(p)3"
str3 = "N(0)t ) 0(k"
str4 = "a(b))(c"
def parensValid(str):
    stack = []
    for item in str:
        if item == "(":
            stack.append(item)
        elif item == ")" and len(stack)>0:
            stack.pop()
        elif item == ")" and len(stack)==0:
            return False
    if len(stack)>0:
        return False
    else:
        return True
    
##print(parensValid(str1))

"""
/* 
  Braces Valid
  Given a string sequence of parentheses, braces and brackets, determine whether it is valid. 
*/

const str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!";
const expected1 = true;

const str2 = "D(i{a}l[ t]o)n{e";
const expected2 = false;

const str3 = "A(1)s[O (n]0{t) 0}k";
const expected3 = false;

/**
 * Determines whether the string's braces, brackets, and parenthesis are valid
 * based on the order and amount of opening and closing pairs.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {boolean} Whether the given strings braces are valid.
 */
"""
def bracesValid(str):
    stack = []
    brace_dict = {")": "(", "]":"[", "}":"{"}
    for i in range(len(str)):
        if str[i] == "(" or str[i] == "[" or str[i] == "{":
            stack.append(str[i])
        elif len(stack)>0 and str[i] in brace_dict and brace_dict[str[i]] == stack[-1]:
            stack.pop()
    if len(stack)>0:
        return False
    else:
        return True

str1 = "W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!"
str2 = "D(i{a}l[ t]o)n{e"
str3 = "A(1)s[O (n]0{t) 0}k"

bracesValid(str1)
bracesValid(str2)
bracesValid(str3)