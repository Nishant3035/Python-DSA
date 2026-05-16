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

**Total solved: 15 | Easy: 15 | Medium: 0 | Hard: 0**

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
