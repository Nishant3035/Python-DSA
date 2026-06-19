# LeetCode Journal — Nishant Chaurasia

> Started: May 2026 | Goal: 200+ problems by December 2026
> Rule: Attempt → Hint if stuck → Code myself → Document

---

## Progress Tracker

| No  | Problem                 | Difficulty | Pattern                | Hint? | Date   |
| --- | ----------------------- | ---------- | ---------------------- | ----- | ------ |
| 283 | Move Zeroes             | Easy       | Array                  | No    | May 8  |
| 9   | Palindrome Number       | Easy       | Math                   | No    | May 8  |
| 268 | Missing Number          | Easy       | Math                   | Yes   | May 9  |
| 217 | Contains Duplicate      | Easy       | Hash — Set             | No    | May 9  |
| 66  | Plus One                | Easy       | Array — Loop           | No    | May 10 |
| 485 | Max Consecutive Ones    | Easy       | Array — Counter        | No    | May 10 |
| 136 | Single Number           | Easy       | Bit — XOR              | No    | May 11 |
| 14  | Longest Common Prefix   | Easy       | String — Prefix        | Yes   | May 13 |
| 242 | Valid Anagram           | Easy       | Hash — Dictionary      | No    | May 13 |
| 13  | Roman to Integer        | Easy       | Hash — SubtractiveRule | Yes   | May 13 |
| 26  | Remove Duplicate Sorted | Easy       | Array — Two Pointer    | No    | May 13 |
| 1   | Two Sum                 | Easy       | Hash — Complement      | No    | May 13 |
| 169 | Majority Element        | Easy       | Hash — Dictionary      | No    | May 15 |
| 344 | Reverse String          | Easy       | Array — Built-in       | No    | May 15 |
| 412 | Fizz Buzz               | Easy       | String — Loop          | No    | May 16 |
| 1480| Running Sum of 1D Array | Easy       | Array — Prefix Sum     | No    | May 17 |
| 383 | Ransom Note             | Easy       | Hash — Dictionary      | No    | May 17 |
| 387 | First Unique Character  | Easy       | Hash — Dictionary      | Yes   | May 17 |
| 2114| Maximum Words in Sentences| Easy     | Array — String Split   | Yes   | May 18 |
| 1431| Kids With Greatest Candies| Easy     | Array — Max tracking   | No    | May 19 |
| 167 | Two Sum II - Sorted Array| Medium    | Two Pointer            | Yes   | May 19 |
| 1470| Shuffle the Array       | Easy       | Array — Interleaving   | Yes   | May 20 |
| 704 | Binary Search           | Easy       | Binary Search          | No    | May 20 |
| 1768| Merge Strings Alternately | Easy     | String — Two Pointer   | Yes   | May 21 |
| 153 | Find Min in Rotated Array | Medium   | Binary Search          | Yes   | May 21 |
| 1672| Richest Customer Wealth | Easy       | Array                  | Yes   | May 22 |
| 2235| Add Two Integers        | Easy       | Math                   | No    | May 23 |
| 2011| Final Value After Operations | Easy  | Array — String Check   | No    | May 24 |
| 2469| Convert the Temperature | Easy       | Math                   | No    | May 25 |
| 125 | Valid Palindrome        | Easy       | String — Two Pointer   | Yes   | May 26 |
| 27  | Remove Element          | Easy       | Array — Two Pointer    | No    | May 27 |
| 1929| Concatenation of Array  | Easy       | Array                  | No    | May 28 |
| 1108| Defanging an IP Address | Easy       | String Manipulation    | No    | May 29 |
| 70  | Climbing Stairs         | Easy       | DP — Fibonacci         | Yes   | May 30 |
| 1342| Number of Steps to Reduce a Number to Zero| Easy|Math — Simulation|No | May 31 |
| 509 | Fibonacci Number        | Easy       | DP — Fibonacci         | Yes   | June 1 |
| 231 | Power of Two            | Easy       | Recursion - Math       | No    | June 2 |
| 50  | Pow(x, n)            | Medium | Recursion—Binary Exponentiation | Yes | June 2 |
| 326 | Power of Three          | Easy       | Math — Repeated Division |  No | June 2 |
| 338 | Counting Bits           | Easy   | Bit Manipulation—Brute Force | Yes | June 3 |
| 342 | Power of Four           | Easy       |Math — Repeated Division  | No  | June 3 |
| 75  | Sort Colors         | Medium |Three Pointer — Dutch National Flag| No | June 3 |
| 912 | Sort an Array           | Medium     |Divide&Conquer — Merge Sort| Yes | Jun 4 |
| 88  | Merge Sorted Array      | Easy       |Two Pointer — Reverse Merge| Yes | Jun 4 |
| 56  | Merge Intervals         | Medium    |Sorting + Greedy + Intervals| Yes | Jun 4 |
| 2236| Root Equals Sum of Children | Easy   | Binary Tree — Basic Check | No  | Jun 5 |
| 80  | Remove Duplicates from Sorted Array II | Medium | Two Pointer    | No  | Jun 7 |
| 189 | Rotate Array            | Medium     | Array — Rotation         | Yes  | Jun 8 |
| 905 | Sort Array By Parity    | Easy  | Two Pointers — Partition Array | No | Jun 10 |
| 121 | Best Time to Buy and Sell Stock | Easy | Sliding Window / Greedy | No | Jun 11 |
| 152 | Maximum Product Subarray|Medium|DynamicProgramming/KadaneVariant| Yes | Jun 19 |

**Total solved: 50 | Easy: 41 | Medium: 9 | Hard: 0**
``` 🚀

---

## LC 283 – Move Zeroes

**Date:** May 8, 2026
**Difficulty:** Easy
**Pattern:** Array — Two Pointer
**Hint needed:** No

**Approach:**
Two pointer — one pointer (insert_pos) tracks where to place
the next non-zero element. Loop through array, when num != 0
place it at insert_pos and increment. After loop, fill
remaining positions with 0.

**Solution:**

```python
def moveZeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|-------------------------|----------------------------------------------------|
| `while insert_pos < len(nums)` | Loop until a condition is met |
| `len(nums)` | Returns length of list |
| In-place modification | Changing array without creating a new one — O(1) space |
| Two pointer technique | Two variables pointing to different positions in array |

**Time:** O(n) | **Space:** O(1)

---

## LC 9 – Palindrome Number

**Date:** May 8, 2026
**Difficulty:** Easy
**Pattern:** Math — Digit Reversal
**Hint needed:** No

**Approach:**
Reverse the number mathematically using modulo and integer
division. Compare reversed number with original.
Negative numbers are never palindromes.

**Solution:**

```python
def isPalindrome(x):
    if x < 0:
        return False
    original = x
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    return original == reversed_num
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|--------------------|---------------------------------------------------------|
| `x % 10` | Modulo — gives last digit of number |
| `x //= 10` | Floor division — removes last digit |
| `reversed * 10 + digit` | Builds reversed number digit by digit |
| `if x < 0` | Negative numbers can never be palindromes |

**Time:** O(log n) | **Space:** O(1)

---

## LC 268 – Missing Number

**Date:** May 9, 2026
**Difficulty:** Easy
**Pattern:** Math — Gaussian Sum
**Hint needed:** Yes — approach only

**Approach:**
Gaussian sum formula. Expected sum of 0 to n = n\*(n+1)/2.
Subtract actual array sum from expected sum.
The difference is the missing number.

**Solution:**

```python
def missingNumber(nums):
    n = len(nums)
    expected = n * (n + 1) // 2
    return expected - sum(nums)
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|--------------------|---------------------------------------------------------|
| `sum(nums)` | Inbuilt — returns sum of all elements in list |
| `n * (n+1) // 2` | Gaussian sum formula for sum of 0 to n |
| `//` | Floor division — returns integer, not float |
| Alternative | Can also solve with XOR of all indices and values |

**Time:** O(n) | **Space:** O(1)

---

## LC 217 – Contains Duplicate

**Date:** May 9, 2026
**Difficulty:** Easy
**Pattern:** Hash — Set
**Hint needed:** No

**Approach:**
Add elements to a set. If element already exists in set
it's a duplicate — return True. If loop completes
with no duplicates found — return False.

**Solution:**

```python
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|--------------------|---------------------------------------------------------|
| `set()` | Creates empty set — stores unique elements only |
| `seen.add(num)` | Adds element to set |
| `if num in seen` | O(1) lookup in set — faster than list O(n) |
| `return False` | Outside loop — only reached if no duplicate found |
| One liner version | `return len(nums) != len(set(nums))` |

**Time:** O(n) | **Space:** O(n)

---

## LC 66 – Plus One

**Date:** May 10, 2026
**Difficulty:** Easy
**Pattern:** Array — Loop
**Hint needed:** No

**Approach:**
Loop from last digit to first. If digit < 9 add 1 and return.
If digit is 9 set it to 0 and carry over to next digit.
If all digits were 9 insert 1 at beginning.

**Solution:**

```python
def plusOne(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|-------------------------------|------------------------------------------------|
| `range(len(digits)-1, -1, -1)`| Loop backwards — start, stop, step |
| `digits[i] += 1` | Increment element at index i |
| `[1] + digits` | Prepend 1 to list — handles all 9s case |
| Reverse loop | Processing array from right to left |

**Time:** O(n) | **Space:** O(1)

---

## LC 485 – Max Consecutive Ones

**Date:** May 10, 2026
**Difficulty:** Easy
**Pattern:** Array — Counter
**Hint needed:** No

**Approach:**
Single pass with counter. If num == 1 increment count
and update max_count. If num == 0 reset count to 0.
Return max_count at end.

**Solution:**

```python
def findMaxConsecutiveOnes(nums):
    count = 0
    max_count = 0
    for num in nums:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|---------------------------|----------------------------------------------------|
| `max(a, b)` | Inbuilt — returns larger of two values |
| `count = 0` reset | Resetting counter when streak breaks |
| `else: count = 0` | Key insight — what to do when condition fails |
| Running maximum pattern | Track best answer seen so far inside loop |

**Time:** O(n) | **Space:** O(1)

---

## LC 136 – Single Number

**Date:** May 11, 2026
**Difficulty:** Easy
**Pattern:** Bit Manipulation — XOR
**Hint needed:** No

**Approach:**
XOR all numbers together. Any number XORed with itself = 0.
Any number XORed with 0 = itself. So all duplicates cancel
out and only the single number remains.

**Solution:**

```python
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|--------------------|---------------------------------------------------------|
| `^=` | XOR assignment operator |
| `a ^ a = 0` | Any number XORed with itself equals 0 |
| `a ^ 0 = a` | Any number XORed with 0 equals itself |
| XOR is commutative | Order doesn't matter — a^b^a = b |
| One liner | `return reduce(lambda a,b: a^b, nums)` using functools |

**Time:** O(n) | **Space:** O(1)

---

## LC 14 – Longest Common Prefix

**Date:** May 13, 2026
**Difficulty:** Easy
**Pattern:** String — Shrinking Prefix
**Hint needed:** Yes — full explanation

**Approach:**
Take first word as starting prefix. Loop through every word.
While current word does not start with prefix — shrink prefix
by removing last character. After all words checked — return prefix.

**Solution:**

```python
def longestCommonPrefix(strs):
    prefix = strs[0]
    for word in strs:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
    return prefix
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|-----------------------------|----------------------------------------------------|
| `word.startswith(prefix)` | Returns True if word begins with prefix |
| `prefix[:-1]` | Remove last character from string |
| `not` | Flips True to False and False to True |
| `while` inside `for` | Inner loop keeps running until condition is met |
| `[]` vs `()` | Square brackets for slicing, round for function call |

**Time:** O(n\*m) | **Space:** O(1)

---

## LC 242 – Valid Anagram

**Date:** May 13, 2026
**Difficulty:** Easy
**Pattern:** Hash — Dictionary
**Hint needed:** No

**Approach:**
Build two frequency dicts — one per string using dict.get().
Early exit if lengths differ. Compare both dicts at end.

**Solution:**
...
```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    hash_map1 = dict()
    hash_map2 = dict()
    n = len(s)
    for i in range(0, n):
        hash_map1[s[i]] = hash_map1.get(s[i], 0) + 1
        hash_map2[t[i]] = hash_map2.get(t[i], 0) + 1
    return hash_map1 == hash_map2
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|-------------------------------|---------------------------------------------------------|
| `dict()` | Creates empty dictionary |
| `hash_map.get(key, 0)` | Returns value for key, returns 0 if key doesn't exist |
| `hash_map.get(key, 0) + 1` | Safe way to increment frequency count |
| `hash_map1 == hash_map2` | Compares two dicts — True if same keys and values |
| `if len(s) != len(t)` | Early exit — anagrams must have same length |

**Time:** O(n) | **Space:** O(n)

---

## LC 13 – Roman to Integer

**Date:** May 13, 2026
**Difficulty:** Easy
**Pattern:** Hash — Subtractive Rule
**Hint needed:** Yes — subtractive rule logic

**Approach:**
Build dict mapping Roman numerals to values.
Loop through string except last character.
If current value < next value → subtract (e.g. IV=4, IX=9).
Else → add. Always add last character separately.

**Solution:**

```python
def romanToInt(s):
    roman = {
        "I": 1, "V": 5,  "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    total = 0
    n = len(s)
    for i in range(n - 1):
        if roman[s[i]] < roman[s[i + 1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    total += roman[s[-1]]
    return total
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|---------------------------|---------------------------------------------------------|
| `roman[s[i]]` | Access dict value using character as key |
| `s[i + 1]` | Access next character in string |
| `range(n - 1)` | Loop stops before last element |
| `s[-1]` | Last character of string |
| Subtractive rule | IV=4, IX=9, XL=40 — smaller before larger = subtract |

**Time:** O(n) | **Space:** O(1)

---

## LC 26 – Remove Duplicates from Sorted Array

**Date:** May 13, 2026
**Difficulty:** Easy
**Pattern:** Array — Two Pointer
**Hint needed:** No

**Approach:**
Slow pointer tracks last unique position.
Fast pointer scans ahead. When unique found — increment slow,
copy value. Return slow + 1 as count of unique elements.

**Solution:**

```python
def removeDuplicates(nums):
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|----------------------------|----------------------------------------------------|
| `range(1, len(nums))` | Start fast pointer from index 1 |
| `nums[fast] != nums[slow]` | Compare current with last unique element |
| `slow += 1` | Move slow pointer when unique element found |
| `return slow + 1` | Count of unique elements |
| Slow/Fast pointer pattern | Classic for sorted array in-place problems |

**Time:** O(n) | **Space:** O(1)

---

## LC 1 – Two Sum

**Date:** May 13, 2026
**Difficulty:** Easy
**Pattern:** Hash — Complement
**Hint needed:** No

**Approach:**
For each number calculate complement = target - num.
Check if complement already in hashmap.
If yes — return both indices. Store num:index as you go.

**Solution:**

```python
def twoSum(nums, target):
    seen = {}
    n = len(nums)
    for i in range(0, n):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        seen[nums[i]] = i
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|---------------------------|----------------------------------------------------|
| `seen = {}` | Empty dict — stores num:index pairs |
| `target - nums[i]` | Complement — the number needed to reach target |
| `if complement in seen` | O(1) dict lookup |
| `seen[nums[i]] = i` | Store value as key, index as value |
| One pass hashmap | Check complement BEFORE storing — handles duplicates|

**Time:** O(n) | **Space:** O(n)

---

## LC 169 – Majority Element

**Date:** May 15, 2026
**Difficulty:** Easy
**Pattern:** Hash — Dictionary
**Hint needed:** No

**Approach:**
Build frequency dict using dict.get(). Loop through all keys.
Return the key whose count is greater than n/2.
Majority element always exists (guaranteed by problem).

**Solution:**
```python
def majorityElement(nums):
    hash_map = dict()
    n = len(nums)
    for i in range(0, n):
        hash_map[nums[i]] = hash_map.get(nums[i], 0) + 1
    for key in hash_map:
        if hash_map[key] > n / 2:
            return key
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature          | What it means                                           |
|---------------------------|---------------------------------------------------------|
| `hash_map.get(key, 0)+1`  | Safe frequency increment — 0 default if key missing    |
| `for key in hash_map`     | Iterates over all keys in dictionary                    |
| `hash_map[key]`           | Access value for a key                                  |
| `> n / 2`                 | Majority means appears more than half the time          |
| Alternative               | Boyer-Moore Voting Algorithm — O(1) space               |

**Time:** O(n) | **Space:** O(n)

---

## LC 344 – Reverse String

**Date:** May 15, 2026
**Difficulty:** Easy
**Pattern:** Array — Built-in / Two Pointer
**Hint needed:** No

**Approach:**
Used built-in list .reverse() method which reverses in-place.
Problem asks to modify input array in-place — .reverse() does exactly that.

**Solution:**
```python
def reverseString(s):
    s.reverse()
    return s
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature   | What it means                                           |
|--------------------|---------------------------------------------------------|
| `s.reverse()`      | Inbuilt — reverses list IN-PLACE, returns None          |
| In-place           | Modifies original list — no new list created — O(1) space |
| Alternative 1      | Two pointer: `left, right = 0, len(s)-1` swap until middle |
| Alternative 2      | Slicing: `s[:] = s[::-1]` — also in-place              |
| `s[::-1]`          | Slice with step -1 — returns reversed copy (NOT in-place) |

**Note:** `.reverse()` returns `None` — the `return s` works here
because s is modified in-place. In interviews prefer two pointer
approach to show you understand the underlying logic.

**Time:** O(n) | **Space:** O(1)

---

## LC 412 – Fizz Buzz

**Date:** May 16, 2026
**Difficulty:** Easy
**Pattern:** Array — Loop + Conditionals
**Hint needed:** No

**Approach:**
Loop from 1 to n. Check divisibility using modulo.
Check FizzBuzz (both) FIRST before checking Fizz or Buzz alone.
Append string to result list. Return list.

**Solution:**
```python
def fizzBuzz(n):
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature    | What it means                                           |
|---------------------|---------------------------------------------------------|
| `i % 15 == 0`       | Divisible by both 3 and 5 — check this FIRST           |
| `i % 3 == 0`        | Divisible by 3                                          |
| `i % 5 == 0`        | Divisible by 5                                          |
| `str(i)`            | Convert integer to string                               |
| `result.append(x)`  | Add element to end of list                              |
| `range(1, n + 1)`   | Loop from 1 to n inclusive                             |
| Order matters       | Check % 15 before % 3 and % 5 or FizzBuzz never hits  |

**Time:** O(n) | **Space:** O(n)

---

## LC 1480 – Running Sum of 1D Array
**Date:** May 17, 2026
**Difficulty:** Easy
**Pattern:** Array — Prefix Sum
**Hint needed:** No

**Approach:**
Keep a running total. For each index add current element
to curr_sum and overwrite nums[i] with curr_sum. Return nums.

**Solution:**
```python
def runningSum(nums):
    curr_sum = 0
    n = len(nums)
    for i in range(0, n):
        curr_sum += nums[i]
        nums[i] = curr_sum
    return nums
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature    | What it means                                      |
|---------------------|----------------------------------------------------|
| `curr_sum += nums[i]`| Add current element to running total              |
| `nums[i] = curr_sum` | Overwrite element with running sum — in-place     |
| Prefix sum pattern  | Each index stores sum of all elements before it   |
| In-place            | Modify original array — O(1) space                |

**Time:** O(n) | **Space:** O(1)

---

## LC 383 – Ransom Note
**Date:** May 17, 2026
**Difficulty:** Easy
**Pattern:** Hash — Dictionary
**Hint needed:** No

**Approach:**
Build frequency dict from magazine. Then for each character
in ransomNote check if count > 0. If not — return False.
If yes — reduce count by 1. If all characters found — return True.

**Solution:**
```python
def canConstruct(ransomNote, magazine):
    hash_map = dict()
    for i in magazine:
        hash_map[i] = hash_map.get(i, 0) + 1
    for char in ransomNote:
        if hash_map.get(char, 0) == 0:
            return False
        hash_map[char] -= 1
    return True
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature          | What it means                                      |
|---------------------------|----------------------------------------------------|
| `hash_map.get(char, 0)`   | Returns 0 if char not in dict — safe lookup        |
| `hash_map[char] -= 1`     | Reduce count after using that letter               |
| `== 0` check              | Letter not available — either missing or used up   |
| Two loop pattern          | Build first, then consume — classic hash approach  |

**Time:** O(n) | **Space:** O(n)

---

## LC 387 – First Unique Character in a String
**Date:** May 17, 2026
**Difficulty:** Easy
**Pattern:** Hash — Dictionary
**Hint needed:** Yes — loop structure

**Approach:**
Build frequency dict from string. Then loop through string
using index. First character with count == 1 — return its index.
If none found — return -1.

**Solution:**
```python
def firstUniqChar(s):
    hash_map = dict()
    for i in s:
        hash_map[i] = hash_map.get(i, 0) + 1
    for i in range(len(s)):
        if hash_map[s[i]] == 1:
            return i
    return -1
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature      | What it means                                          |
|-----------------------|--------------------------------------------------------|
| `hash_map[s[i]]`      | Access frequency of character at position i            |
| `range(len(s))`       | Loop using index — needed to return position           |
| `== 1`                | Unique means appears exactly once                      |
| `return -1`           | Outside loop — no unique character found               |
| Why not `for i in s`  | Need index not character — so use range(len(s))        |

**Time:** O(n) | **Space:** O(n)

---

## LC 2114 – Maximum Number of Words Found in Sentences
**Date:** May 18, 2026
**Difficulty:** Easy
**Pattern:** Array — String Split
**Hint needed:** Yes — split() method hint

**Approach:**
Loop through each sentence. Split each sentence by spaces
to get list of words. Count words using len(). Track maximum
count using comparison. Return max at end.

**Solution:**
```python
def mostWordsFound(sentences):
    max_sen = 0
    for i in sentences:
        sen = len(i.split())
        if sen > max_sen:
            max_sen = sen
    return max_sen
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature      | What it means                                           |
|-----------------------|---------------------------------------------------------|
| `i.split()`           | Splits string by spaces — returns list of words         |
| `len(i.split())`      | Count of words in sentence                              |
| `for i in sentences`  | i is the sentence string directly — NOT an index        |
| Common mistake        | `sentences[i]` fails — i is already the element        |
| `if sen > max_sen`    | Track running maximum without max() function            |

**Time:** O(n*m) | **Space:** O(1)

---

## LC 1431 – Kids With the Greatest Number of Candies
**Date:** May 19, 2026
**Difficulty:** Easy
**Pattern:** Array — Max Tracking
**Hint needed:** No

**Approach:**
Find maximum candy count in array first.
Then for each kid check if their candies + extra >= maximum.
Append True or False to result list accordingly.

**Solution:**
```python
def kidsWithCandies(candies, extraCandies):
    result = []
    highest_candy = 0
    for i in candies:
        if i > highest_candy:
            highest_candy = i
    for candy in candies:
        if candy + extraCandies >= highest_candy:
            result.append(True)
        else:
            result.append(False)
    return result
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature       | What it means                                           |
|------------------------|---------------------------------------------------------|
| `for i in candies`     | i IS the value directly — not the index                 |
| `result.append(True)`  | Append boolean directly to list                         |
| `>= highest_candy`     | Greater OR equal — kid can also match the highest       |
| Two loop pattern       | First find max, then use max in second loop             |
| Alternative            | `max(candies)` gives highest in one line                |

**Time:** O(n) | **Space:** O(n)

---

## LC 167 – Two Sum II Input Array Is Sorted
**Date:** May 19, 2026
**Difficulty:** Medium ⭐ First Medium Solved!
**Pattern:** Two Pointer
**Hint needed:** Yes — while loop structure

**Approach:**
Array is sorted — use two pointers left and right.
If sum == target — return both indexes (1-indexed).
If sum > target — move right pointer left (reduce sum).
If sum < target — move left pointer right (increase sum).

**Solution:**
```python
def twoSum(numbers, target):
    n = len(numbers)
    left = 0
    right = n - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return left + 1, right + 1
        if numbers[left] + numbers[right] > target:
            right -= 1
        else:
            left += 1
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature           | What it means                                           |
|----------------------------|---------------------------------------------------------|
| `while left < right`       | Loop until pointers meet — O(n) not O(n²)              |
| `right -= 1`               | Move right pointer left — reduces sum                   |
| `left += 1`                | Move left pointer right — increases sum                 |
| `left + 1, right + 1`      | Problem uses 1-indexed — add 1 to both                 |
| Why sorted array matters   | Can predict if sum is too big or too small              |
| Two pointer vs nested loop | O(n) vs O(n²) — always prefer two pointer on sorted    |

**Time:** O(n) | **Space:** O(1)

---

## LC 1470 – Shuffle the Array
**Date:** May 20, 2026
**Difficulty:** Easy
**Pattern:** Array — Interleaving
**Hint needed:** Yes — approach hint

**Approach:**
Loop n times. Each iteration append nums[i] (first half)
then nums[i+n] (second half). Returns interleaved result.

**Solution:**
```python
def shuffle(nums, n):
    result = []
    for i in range(n):
        result.append(nums[i])
        result.append(nums[i + n])
    return result
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature     | What it means                                           |
|----------------------|---------------------------------------------------------|
| `range(n)`           | Loop exactly n times — 0 to n-1                        |
| `nums[i + n]`        | Access second half element — offset by n               |
| Interleaving pattern | Take one from first half, one from second half          |
| `result.append(x)`   | Add element to end of list                             |

**Time:** O(n) | **Space:** O(n)

---

## LC 704 – Binary Search
**Date:** May 20, 2026
**Difficulty:** Easy
**Pattern:** Binary Search
**Hint needed:** No

**Approach:**
Classic binary search. Set low and high pointers.
Find mid. If target == nums[mid] return mid.
If target < mid go left (high = mid-1).
If target > mid go right (low = mid+1).
Return -1 if not found.

**Solution:**
```python
def search(nums, target):
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature       | What it means                                           |
|------------------------|---------------------------------------------------------|
| `low, high = 0, n-1`   | Multiple assignment in one line                        |
| `(low + high) // 2`    | Floor division — gives integer mid index               |
| `while low <= high`    | Keep searching while valid range exists                 |
| `high = mid - 1`       | Discard right half — target is smaller                 |
| `low = mid + 1`        | Discard left half — target is larger                   |
| `return -1`            | Outside loop — target not found                        |

**Time:** O(log n) | **Space:** O(1)

---

## LC 1768 – Merge Strings Alternately
**Date:** May 21, 2026
**Difficulty:** Easy
**Pattern:** String — Interleaving
**Hint needed:** Yes — loop structure

**Approach:**
Loop using index up to max length of both strings.
If index valid for word1 — add word1[i].
If index valid for word2 — add word2[i].
Handles unequal lengths automatically.

**Solution:**
```python
def mergeAlternately(word1, word2):
    merged = ""
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            merged += word1[i]
        if i < len(word2):
            merged += word2[i]
    return merged
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature            | What it means                                           |
|-----------------------------|---------------------------------------------------------|
| `max(len(word1), len(word2))`| Loop up to longer string's length                     |
| `if i < len(word1)`         | Guard — don't access index beyond string length        |
| `merged += word1[i]`        | String concatenation using +=                          |
| `range` vs `for x in str`  | Use range when you need index to access multiple lists  |
| Common mistake              | `word1[i]` when i is already char — use range instead  |

**Time:** O(n) | **Space:** O(n)

---

## LC 153 – Find Minimum in Rotated Sorted Array
**Date:** May 21, 2026
**Difficulty:** Medium
**Pattern:** Binary Search — Rotated Array
**Hint needed:** Yes — full help
**⚠️ REVISE THIS IN 3 DAYS**

**Approach:**
Binary Search on rotated array. Compare mid with right.
If nums[mid] > nums[right] — minimum is in RIGHT half
(left side is sorted, min must be after mid).
Else — minimum is in LEFT half including mid.
When left == right — found the minimum.

**Solution:**
```python
def findMin(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        middle = (left + right) // 2
        if nums[middle] > nums[right]:
            left = middle + 1
        else:
            right = middle
    return nums[left]
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature          | What it means                                           |
|---------------------------|---------------------------------------------------------|
| `nums[middle] > nums[right]`| Key comparison — tells which half is unsorted        |
| `left = middle + 1`       | Min is in right half — discard left including mid      |
| `right = middle`          | Min could be mid itself — don't discard it             |
| `while left < right`      | Stop when pointers meet — that's the answer            |
| `return nums[left]`       | left == right at this point — both point to minimum    |
| Why compare with right?   | Right side tells us if rotation happened in left half  |

**Key insight:**
If mid > right — the left half is sorted normally,
rotation happened in right half, minimum is there.
If mid <= right — right half is sorted, minimum is in left half.

**Time:** O(log n) | **Space:** O(1)

---

## LC 1672 – Richest Customer Wealth
**Date:** 22 May 2026
**Difficulty:** Easy
**Pattern:** Array Counter
**Hint needed:** Yes

**Approach:**
Loop through every customer (row) in the 2D array.
Find the sum of each customer's bank accounts using `sum()`.
Keep track of the maximum wealth found.

**Solution:**
```python
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        maximum = 0

        for customer in accounts:

            wealth = sum(customer)

            maximum = max(maximum, wealth)

        return maximum
```

**Syntax & Inbuilt Features Learned:**

| Syntax / Feature           | What it means                  |
|----------------------------|--------------------------------|
| `sum(customer)`            | Adds all elements in a list    |
| `max(a,b)`                 | Returns larger value           |
| `for customer in accounts` | Traverses each row in 2D array |
| `List[List[int]]`          | 2D integer array               |

**Time:** O(n * m) | **Space:** O(1)

---

## LC 2235 – Add Two Integers
**Date:** May 23, 2026
**Difficulty:** Easy
**Pattern:** Math
**Hint needed:** No

**Approach:**
Simply return the sum of both integers.
One line solution.

**Solution:**
```python
def sum(num1, num2):
    return num1 + num2
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature  | What it means                                      |
|-------------------|----------------------------------------------------|
| `return a + b`    | Direct return without storing in variable          |
| One liner         | Simple problems don't need complex solutions       |

**Time:** O(1) | **Space:** O(1)

---

## LC 2011 – Final Value of Variable After Performing Operations
**Date:** May 24, 2026
**Difficulty:** Easy
**Pattern:** Array — String Check
**Hint needed:** No

**Approach:**
Loop through operations. Check each string.
If contains "--" subtract 1. If contains "++" add 1.
Return final value of x.

**Solution:**
```python
def finalValueAfterOperations(operations):
    x = 0
    for operation in operations:
        if operation == "--X":
            x -= 1
        elif operation == "X--":
            x -= 1
        elif operation == "X++":
            x += 1
        else:
            x += 1
    return x
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature      | What it means                                      |
|-----------------------|----------------------------------------------------|
| `x -= 1`              | Decrement x by 1                                   |
| `x += 1`              | Increment x by 1                                   |
| String comparison     | `==` checks exact string match                     |
| Smarter alternative   | Check `"+"` in operation — covers both X++ and ++X |

**Smarter solution:**
```python
def finalValueAfterOperations(operations):
    x = 0
    for op in operations:
        x += 1 if "+" in op else -1
    return x
```

**Time:** O(n) | **Space:** O(1)

---

## LC 2469 – Convert the Temperature
**Date:** May 25, 2026
**Difficulty:** Easy
**Pattern:** Math
**Hint needed:** No

**Approach:**
Apply temperature conversion formulas directly.
Kelvin = celsius + 273.15
Fahrenheit = celsius * 1.80 + 32.00
Return both in a list.

**Solution:**
```python
def convertTemperature(celsius):
    kelvin = celsius + 273.15
    fahrenheit = (celsius * 1.80) + 32.00
    return [kelvin, fahrenheit]
```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature     | What it means                                      |
|----------------------|----------------------------------------------------|
| `float`              | Decimal number type — used for precise calculations|
| `return [a, b]`      | Return multiple values as a list                   |
| Direct formula       | Some problems just need math — no loops needed     |

**Time:** O(1) | **Space:** O(1)

---

## LC 125 – Valid Palindrome
**Date:** 26 May 2026
**Difficulty:** Easy
**Pattern:** String — Two Pointer
**Hint needed:** Yes

**Approach:**
Create a cleaned lowercase string containing only alphanumeric characters.
Use two pointers:
- one from start
- one from end

Compare both characters:
- if mismatch → return False
- otherwise move inward

If all characters match, return True.

**Solution:**
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = ""

        for ch in s:

            if ch.isalnum():
                clean += ch.lower()

        left = 0
        right = len(clean) - 1

        while left < right:

            if clean[left] != clean[right]:
                return False

            left += 1
            right -= 1

        return True
```

**Syntax & Inbuilt Features Learned:**

| Syntax / Feature | What it means                             |
|------------------|-------------------------------------------|
| `isalnum()`      | Checks if character is alphabet or number |
| `lower()`        | Converts character to lowercase           |
| `clean += ch`    | Appends character to string               |
| `left < right`   | Two pointer traversal condition           |
| `len(clean)-1`   | Last index of string                      |

**Time:** O(n) | **Space:** O(n)

---

## LC 27 – Remove Element
**Date:** 26 May 2026  
**Difficulty:** Easy  
**Pattern:** Array — Two Pointer  
**Hint needed:** No
 

## Approach

Use two pointers:
- `right` traverses the array
- `left` stores valid elements

If current element is not equal to `val`:
- place it at `left`
- move `left` ahead

Finally return `left` as the new length.


## Solution

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left = 0

        for right in range(len(nums)):

            if nums[right] != val:

                nums[left] = nums[right]
                left += 1

        return left
```


## Syntax & Inbuilt Features Learned

| Syntax / Feature           | Meaning                                           |
|----------------------------|---------------------------------------------------|
| `range(len(nums))`         | Traverses array indices                           |
| `nums[left] = nums[right]` | Replaces value in-place                           |
| `!=`                       | Checks inequality                                 |
| `left += 1`                | Moves pointer forward                             |
| Two Pointer                | One pointer traverses, another stores valid values|


## Complexity

**Time:** O(n)  
**Space:** O(1)

---

## LC 1929 – Concatenation of Array
**Date:** 26 May 2026  
**Difficulty:** Easy  
**Pattern:** Array  
**Hint needed:** No  


## Approach

Return the array concatenated with itself.

Use the `+` operator to join:
- original array
- original array again

---

## Solution

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        return nums + nums
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `nums + nums` | Concatenates two lists |
| `return` | Returns final list |
| `List[int]` | Integer array type hint |

---

## Complexity

**Time:** O(n)  
**Space:** O(n)

---

## LC 1108 – Defanging an IP Address
**Date:** 29 May 2026
**Difficulty:** Easy
**Pattern:** String Manipulation
**Hint needed:** No

---

## Approach

Replace every "." with "[.]".

---

## Solution

```python
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `replace(old, new)` | Replaces all occurrences of old string with new string |
| `return` | Returns final string |

---

## Complexity

**Time:** O(n)
**Space:** O(n)

---

## LC 70 – Climbing Stairs
**Date:** 30 May 2026  
**Difficulty:** Easy  
**Pattern:** Dynamic Programming — Fibonacci  
**Hint needed:** Yes  


## Approach

To reach stair `n`:

- From stair `n-1`, take 1 step
- From stair `n-2`, take 2 steps

Therefore:

Ways to reach stair `n` = Ways to reach stair `n-1` + Ways to reach stair `n-2`

This follows the Fibonacci pattern.

Instead of recursion, store only the previous two values and build the answer iteratively.

---

## Solution

```python
class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        if n == 2:
            return 2

        prev_prev = 1
        prev = 2

        for i in range(3, n + 1):

            current = prev + prev_prev

            prev_prev = prev

            prev = current

        return current
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `range(3, n + 1)` | Loops from stair 3 to stair n |
| `current = prev + prev_prev` | Fibonacci recurrence relation |
| `prev_prev = prev` | Shift previous values forward |
| `prev = current` | Update latest computed value |
| Dynamic Programming | Build solution from previously computed answers |

---

## Complexity

**Time:** O(n)  
**Space:** O(1)

---

## LC 1342 – Number of Steps to Reduce a Number to Zero
**Date:** 31 May 2026
**Difficulty:** Easy
**Pattern:** Math — Simulation
**Hint needed:** No

---

## Approach

Keep reducing the number until it becomes 0.

- If number is even, divide by 2.
- If number is odd, subtract 1.

Count each operation.

---

## Solution

```python
class Solution:
    def numberOfSteps(self, num: int) -> int:

        steps = 0

        while num > 0:

            if num % 2 == 0:
                num = num // 2

            else:
                num -= 1

            steps += 1

        return steps
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `num % 2 == 0` | Checks if number is even |
| `num // 2` | Integer division |
| `num -= 1` | Subtracts 1 from number |
| `while num > 0` | Runs until number becomes 0 |

---

## Complexity

**Time:** O(log n)
**Space:** O(1)

---

## LC 509 – Fibonacci Number
**Date:** 1 June 2026
**Difficulty:** Easy
**Pattern:** Dynamic Programming — Fibonacci
**Hint needed:** Yes

---

## Approach

Use the Fibonacci recurrence relation:

F(n) = F(n-1) + F(n-2)

Store only the previous two Fibonacci numbers and build the answer iteratively.

---

## Solution

```python
class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0

        if n == 1:
            return 1

        prev_prev = 0
        prev = 1

        for i in range(2, n + 1):

            current = prev + prev_prev

            prev_prev = prev
            prev = current

        return current
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `range(2, n + 1)` | Loops from 2 to n |
| `current = prev + prev_prev` | Fibonacci recurrence |
| `prev_prev = prev` | Shifts previous value |
| `prev = current` | Updates latest Fibonacci number |
| Dynamic Programming | Uses previous results to compute next result |

---

## Complexity

**Time:** O(n)
**Space:** O(1)

---

## LC 231 - Power of Two
**Date:** 2 June 2026
**Difficulty:** Easy
**Pattern:** Recursion/Math
**Hint needed:** No 

---

## Approach

**Use the loop** : You used a loop checking pow(2, x) for x in 0–30. Correct but longer. The bit trick is the cleaner way.

**Key Insight** — Powers of 2 in binary always have exactly one 1 bit. So n & (n-1) clears that bit → result is 0. Non-powers won't give 0.

## Solution

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        for x in range(0,31):
            if n == pow(2,x):
                return True
        return False
```
`**Without Loop Solution**`
```python
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return n & (n - 1) == 0
```
---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `pow(2, x)` | Built-in power function |
| `n & (n-1) == 0` | Bit trick — clears lowest set bit, 0 means power of 2 |
| `n <= 0` | Edge case check — powers of 2 are always positive |

---

## Complexity

**Time:** O(1)
**Space:** O(1)


## LC 50 – Pow(x, n)
**Date:** 2 june 2026  
**Difficulty:** Medium  
**Pattern:** Recursion — Binary Exponentiation  
**Hint needed:** Yes  

---

## Approach

Use Divide & Conquer.

Instead of multiplying `x` by itself `n` times:

- Compute `x^(n//2)` once
- Store it in `half`
- Reuse the result

For even powers:

xⁿ = (xⁿᐟ²)²

For odd powers:

xⁿ = x × (xⁿᐟ²)²

For negative powers:

x⁻ⁿ = 1 / xⁿ

This reduces the problem size by half at every recursive call.

---

## Solution

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            return 1 / self.myPow(x, -n)

        half = self.myPow(x, n // 2)

        if n % 2 == 0:
            return half * half

        else:
            return x * half * half
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `n // 2` | Integer division by 2 |
| `self.myPow()` | Recursive function call |
| `n % 2 == 0` | Checks if exponent is even |
| `1 / self.myPow(x, -n)` | Handles negative powers |
| `half = ...` | Stores recursive result to avoid recomputation |
| Binary Exponentiation | Reduces exponent by half every step |
| Divide & Conquer | Solves smaller subproblems recursively |

---

## Complexity

**Time:** O(log n)  
**Space:** O(log n)

## LC 326 – Power of Three
**Date:** 2 June 2026  
**Difficulty:** Easy  
**Pattern:** Math — Repeated Division  
**Hint needed:** Yes  

---

## Approach

A number is a power of 3 if it can be repeatedly divided by 3 and eventually becomes 1.

- If `n <= 0`, return `False`
- While `n` is divisible by 3:
  - divide it by 3
- After the loop:
  - if `n == 1` → power of 3
  - otherwise → not a power of 3

---

## Solution

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n <= 0:
            return False

        while n % 3 == 0:
            n = n // 3

        return n == 1
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `n % 3 == 0` | Checks divisibility by 3 |
| `n // 3` | Integer division |
| `while` | Repeats until condition fails |
| `return n == 1` | Returns True if n became 1 |
| Repeated Division | Common pattern for power-check problems |

---

## Complexity

**Time:** O(log₃ n)  
**Space:** O(1)

## LC 338 – Counting Bits
**Date:** June 3 2026
**Difficulty:** Easy
**Pattern:** Bit Manipulation — Brute Force
**Hint needed:** Yes

---

## Approach

For every number from `0` to `n`:

- Convert number to binary using `bin()`
- Count the number of `'1'` characters
- Store the count in the result array

---

## Solution

```python
class Solution:
    def countBits(self, n: int) -> List[int]:

        result = []

        for i in range(n + 1):
            result.append(bin(i).count('1'))

        return result
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `bin(i)` | Converts integer to binary string |
| `.count('1')` | Counts occurrences of character '1' |
| `range(n + 1)` | Loops from 0 to n inclusive |
| `result.append()` | Adds element to list |
| Bit Representation | Binary form of a number |

---

## Complexity

**Time:** O(n log n)
**Space:** O(n)

## LC 342 – Power of Four
**Date:** June 3 2026
**Difficulty:** Easy
**Pattern:** Math — Repeated Division
**Hint needed:** Yes

---

## Approach

A number is a power of 4 if it can be repeatedly divided by 4 and eventually becomes 1.

- If `n <= 0`, return False
- While divisible by 4:
  - divide by 4
- If final value is 1:
  - return True
- Otherwise:
  - return False

---

## Solution

```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n <= 0:
            return False

        while n % 4 == 0:
            n = n // 4

        return n == 1
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `n % 4 == 0` | Checks divisibility by 4 |
| `n // 4` | Integer division |
| `while` | Repeats while condition is true |
| `return n == 1` | Returns boolean result |
| Repeated Division | Common pattern for power-check problems |

---

## Complexity

**Time:** O(log₄ n)
**Space:** O(1)

## LC 75 – Sort Colors
**Date:** June 3 2026  
**Difficulty:** Medium  
**Pattern:** Three Pointer — Dutch National Flag
**Hint needed:** Yes  

---

## Approach

Maintain three pointers:

- `low` → position for next 0
- `mid` → current element being processed
- `high` → position for next 2

Rules:

- If `nums[mid] == 0`
  - swap with `low`
  - increment `low` and `mid`

- If `nums[mid] == 1`
  - increment `mid`

- If `nums[mid] == 2`
  - swap with `high`
  - decrement `high`

Continue until `mid > high`.

This sorts the array in one pass.

---

## Solution

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:

            if nums[mid] == 0:

                nums[low], nums[mid] = nums[mid], nums[low]

                low += 1
                mid += 1

            elif nums[mid] == 1:

                mid += 1

            else:

                nums[mid], nums[high] = nums[high], nums[mid]

                high -= 1
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `low, mid, high = ...` | Multiple variable assignment |
| `nums[a], nums[b] = nums[b], nums[a]` | Python swap |
| `while mid <= high` | Process until all elements are classified |
| Three Pointers | Track 0s, current element, and 2s |
| Dutch National Flag | One-pass partitioning algorithm |

---

## Complexity

**Time:** O(n)  
**Space:** O(1)


## LC 912 – Sort an Array
**Date:** June 4 2026  
**Difficulty:** Medium  
**Pattern:** Divide & Conquer — Merge Sort
**Hint needed:** Yes  

---

## Approach

Use Merge Sort.

1. Divide the array into two halves.
2. Recursively sort the left half.
3. Recursively sort the right half.
4. Merge the two sorted halves.

The merge step compares elements from both halves and builds a sorted array.

---

## Solution

```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge_arr(left, right)

    def merge_arr(self, left, right):

        i, j = 0, 0
        result = []

        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1

            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `nums[:mid]` | Left half of array |
| `nums[mid:]` | Right half of array |
| `self.sortArray()` | Recursive function call |
| `self.merge_arr()` | Calls helper method inside class |
| `result.extend(arr)` | Adds all remaining elements of a list |
| Divide & Conquer | Break problem into smaller subproblems |
| Merge Sort | Recursively sort and merge arrays |

---

## Complexity

**Time:** O(n log n)  
**Space:** O(n)


## LC 88 – Merge Sorted Array
**Date:** 4 Jun 2026
**Difficulty:** Easy
**Pattern:** Two Pointer — Reverse Merge
**Hint needed:** Yes

---

## Approach

Since `nums1` already has extra space at the end, start merging from the back.

Maintain three pointers:

- `i` → last valid element in `nums1`
- `j` → last element in `nums2`
- `k` → last position in `nums1`

Compare `nums1[i]` and `nums2[j]`.

Place the larger element at `nums1[k]` and move pointers accordingly.

After the main loop, copy any remaining elements from `nums2`.

---

## Solution

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:

                nums1[k] = nums1[i]
                i -= 1

            else:

                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:

            nums1[k] = nums2[j]
            j -= 1
            k -= 1
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `m - 1` | Last valid index of nums1 |
| `n - 1` | Last index of nums2 |
| `m + n - 1` | Last position of merged array |
| `while i >= 0 and j >= 0` | Compare elements from both arrays |
| `nums1[k] = ...` | Place larger element at correct position |
| Two Pointer | Track positions in both arrays |
| Reverse Merge | Merge from end to avoid overwriting values |

---

## Complexity

**Time:** O(m + n)  
**Space:** O(1)

## LC 56 – Merge Intervals
**Date:** 4 Jun 2026
**Difficulty:** Medium
**Pattern:** Sorting + Greedy + Intervals
**Hint needed:** Yes

---

## Approach

First sort the intervals based on their starting values.

Maintain a result array:

- Add the first interval.
- Compare each interval with the last interval in the result.
- If they overlap:
  - Merge them by updating the ending value.
- Otherwise:
  - Add the current interval to the result.

Two intervals overlap when:

```python
last[1] >= current[0]
```

---

## Solution

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        result = [intervals[0]]

        for i in range(1, len(intervals)):

            current = intervals[i]
            last = result[-1]

            if last[1] >= current[0]:

                last[1] = max(last[1], current[1])

            else:

                result.append(current)

        return result
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `intervals.sort()` | Sort intervals by starting value |
| `result[-1]` | Access last interval in result |
| `max(a, b)` | Returns larger value |
| `result.append()` | Add interval to result |
| Greedy | Make locally optimal merge decisions |
| Interval Overlap | Check if intervals intersect |

---

## Complexity

**Time:** O(n log n)  
**Space:** O(n)


## LC 2236 – Root Equals Sum of Children
**Date:** 5 Jun 2026
**Difficulty:** Easy
**Pattern:** Binary Tree — Basic Traversal
**Hint needed:** No

---

## Approach

Check whether the value of the root node is equal to the sum of its left and right child.

Return the comparison result directly.

---

## Solution

```python
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:

        return root.val == root.left.val + root.right.val
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `root.val` | Access current node value |
| `root.left.val` | Access left child value |
| `root.right.val` | Access right child value |
| `==` | Equality comparison |
| Binary Tree Node Access | Read values from tree nodes |

---

## Complexity

**Time:** O(1)  
**Space:** O(1)


## LC 80 – Remove Duplicates from Sorted Array II
**Date:** 7 Jun 2026
**Difficulty:** Medium
**Pattern:** Two Pointer
**Hint needed:** Yes

---

## Approach

Since the array is sorted, duplicates appear together.

Allow at most 2 occurrences of each number.

- The first two elements are always valid.
- Use:
  - `left` → position to write next valid element
  - `right` → current element being checked
- If current element is different from `nums[left - 2]`,
  it means we have not already stored two copies.
- Copy it to `nums[left]` and move `left`.

Return `left` as the new length.

---

## Solution

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return len(nums)

        left = 2

        for right in range(2, len(nums)):

            if nums[right] != nums[left - 2]:

                nums[left] = nums[right]
                left += 1

        return left
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `left = 2` | First two elements are always valid |
| `for right in range(...)` | Read pointer |
| `nums[left - 2]` | Check if two copies already exist |
| `nums[left] = nums[right]` | Store valid element |
| `left += 1` | Move write pointer |
| Two Pointer | Separate read and write positions |
| In-place Modification | Modify array without extra space |

---

## Complexity

**Time:** O(n)  
**Space:** O(1)


## LC 189 – Rotate Array
**Date:** 8 Jun 2026
**Difficulty:** Medium
**Pattern:** Array — Rotation
**Hint needed:** Yes

---

## Approach

Rotate the array to the right by `k` positions.

First reduce unnecessary rotations:

```python
k %= len(nums)
```

Then:

- Take the last `k` elements
- Place them at the front
- Append the remaining elements

Modify the original array in-place using slicing.

---

## Solution

```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k %= len(nums)

        nums[:] = nums[-k:] + nums[:-k]
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `k %= len(nums)` | Reduce extra rotations |
| `nums[-k:]` | Last k elements |
| `nums[:-k]` | Elements before last k |
| `+` | Concatenate lists |
| `nums[:] = ...` | Modify original list in-place |
| Array Rotation | Move elements cyclically |

---

## Complexity

**Time:** O(n)  
**Space:** O(n)


First Occurence 

## LC 905 – Sort Array By Parity
**Date:** 10 Jun 2026
**Difficulty:** Easy
**Pattern:** Two Pointers — Partition Array
**Hint needed:** No

---

## Approach

Move all even numbers to the beginning of the array and all odd numbers to the end.

Use two pointers:

- `left` starts from the beginning.
- `right` starts from the end.

If the left side contains an odd number and the right side contains an even number, swap them.

Then:

- Move `left` forward if it points to an even number.
- Move `right` backward if it points to an odd number.

Continue until both pointers meet.

---

## Solution

```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] % 2 == 0:
                left += 1

            if nums[right] % 2 == 1:
                right -= 1

        return nums
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `num % 2 == 0` | Check if number is even |
| `num % 2 == 1` | Check if number is odd |
| `nums[i], nums[j] = nums[j], nums[i]` | Swap two elements |
| Two Pointers | Process array from both ends |
| In-place Swapping | Rearrange without extra space |

---

## Complexity

**Time:** O(n)

**Space:** O(1)

---

## Key Learning

- Two pointers can partition an array efficiently.
- Swapping is only required when elements are on the wrong side.
- This pattern is useful for segregation and partitioning problems.

## LC 121 – Best Time to Buy and Sell Stock
**Date:** 11 Jun 2026
**Difficulty:** Easy
**Pattern:** Sliding Window / Two Pointers / Greedy
**Hint needed:** No

---

## Approach

Use two pointers:

- `left` → buying day
- `right` → selling day

If the selling price is greater than the buying price:

- Calculate profit
- Update maximum profit

If a cheaper price is found:

- Move `left` to that position
- This gives a better buying opportunity

Continue until all days are processed.

---

## Solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left = 0
        right = 1

        max_profit = 0

        while right < len(prices):

            if prices[right] > prices[left]:

                profit = prices[right] - prices[left]

                max_profit = max(max_profit, profit)

            else:

                left = right

            right += 1

        return max_profit
```

---

## Syntax & Inbuilt Features Learned

| Syntax / Feature | Meaning |
|------------------|----------|
| `left = 0` | Buy day pointer |
| `right = 1` | Sell day pointer |
| `prices[right] > prices[left]` | Check if profit is possible |
| `profit = prices[right] - prices[left]` | Calculate profit |
| `max(max_profit, profit)` | Keep highest profit seen so far |
| `left = right` | Update buy day when cheaper price found |
| Two Pointers | Track buy and sell positions |
| Greedy | Always keep the best buying price |

---

## Complexity

**Time:** O(n)

**Space:** O(1)

---

## Key Learning

- Buy before selling.
- A lower price is always a better buying opportunity.
- Two pointers can efficiently track the best buy/sell pair.
- This problem introduces the Sliding Window / Greedy pattern.


## LC 152 – Maximum Product Subarray

**Date:** June 19, 2026
**Difficulty:** Medium
**Pattern:** Dynamic Programming — Kadane Variant
**Hint needed:** Yes

**Approach:**
Maintain two variables:

* `cur_max` = maximum product ending at current index
* `cur_min` = minimum product ending at current index

A negative number can turn the minimum product into the maximum product and vice versa, so whenever the current number is negative, swap `cur_max` and `cur_min`.

Update both values at each step and keep track of the global maximum product.

**Solution:**

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(nums[i], cur_max * nums[i])
            cur_min = min(nums[i], cur_min * nums[i])

            ans = max(ans, cur_max)

        return ans
```

**Syntax & Inbuilt Features Learned:**

| Syntax / Feature                      | What it means                                          |
| ------------------------------------- | ------------------------------------------------------ |
| `float("-inf")`                       | Represents negative infinity                           |
| `max(a, b)`                           | Returns the larger value                               |
| `min(a, b)`                           | Returns the smaller value                              |
| `cur_max, cur_min = cur_min, cur_max` | Python tuple unpacking used to swap variables          |
| `nums[i] < 0`                         | Check if current number is negative                    |
| `max(nums[i], cur_max * nums[i])`     | Either start a new subarray or extend the existing one |
| `min(nums[i], cur_min * nums[i])`     | Track smallest product for future sign flips           |

**Time:** O(n) | **Space:** O(1)

**Key Learning:**
For product subarray problems, tracking only the maximum product is not enough. A negative number can convert the minimum product into the maximum product, so both must be maintained.


## Template — copy for every new problem

````
## LC [number] – [Problem Name]
**Date:**
**Difficulty:** Easy / Medium / Hard
**Pattern:**
**Hint needed:** Yes / No

**Approach:**

**Solution:**
```python

````

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|------------------|---------------|
| | |

**Time:** O( ) | **Space:** O( )

```

---

## Patterns Reference

| Pattern              | Use when                                              |
|----------------------|-------------------------------------------------------|
| Two Pointer          | Sorted array, pairs, in-place modification            |
| Hash / Set           | O(1) lookup, duplicates, unique elements              |
| Hash / Dict          | Frequency count, store index, complement search       |
| Math                 | Digit operations, formulas, number properties         |
| XOR / Bit            | Find unique, toggle bits, cancel duplicates           |
| Array Counter        | Streak, running count, sliding window preview         |
| Reverse Loop         | Process array from right to left                      |
| Shrinking Prefix     | String matching, reduce until condition met           |


```
