## Tutorial 6
This tutorial will be library how to use regular expression in python 
### Introduction to regular expression
regular expression used to match patern when we want to check user name or password are verify the validation specification or no we use regular expression  
to use regular expression first we need to import `re` module then we can use search to find pattern if it don't exist we will get fulsy value if it exist we will get truthy value  
matching pattern in regular expression :
* `.` any character except a newline
* `*` 0 or more repetitions
* `+` 1 or more repetitions
* `?` 0 or 1 repetition
* `{m}` m repetitions
* `{m,n}` m–n repetitions
* `^` matches the start of the string
* `$` matches the end of the string or just before the newline at the end of the string
* `[]` set of characters
* `[^]` complementing the set
* `\d` decimal digit
* `\D` not a decimal digit
* `\s` whitespace characters
* `\S` not a whitespace character
* `\w` word character … as well as numbers and the underscore
* `\W` not a word character
* `A|B` either A or B
* `(...)` a group
* `(?:...)` non-capturing version
also in our regular expression we can have flags `re.IGNORECASE` `re.MULTILINE` `re.DOTALL`  
others then we can use are `.match()` `.fullmatch()` `.sub()` `.split()` `.findall()`
* re.match(pattern, string, flags=0) If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding Match. Return None if the string does not match the pattern
* re.fullmatch(pattern, string, flags=0) If the whole string matches the regular expression pattern, return a corresponding Match. Return None if the string does not match the pattern;
* re.split(pattern, string, maxsplit=0, flags=0) Split string by the occurrences of pattern. If capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the resulting list. If maxsplit is nonzero, at most maxsplit splits occur, and the remainder of the string is returned as the final element of the list.
* re.findall(pattern, string, flags=0) Return all non-overlapping matches of pattern in string, as a list of strings or tuples. The string is scanned left-to-right, and matches are returned in the order found. Empty matches are included in the result.
* re.sub(pattern, repl, string, count=0, flags=0) Return the string obtained by replacing the leftmost non-overlapping occurrences of pattern in string by the replacement repl. If the pattern isn’t found, string is returned unchanged




