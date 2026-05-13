# LeetCode Journal — Nishant Chaurasia
> Started: May 2026 | Goal: 200+ problems by December 2026
> Rule: Attempt → Hint if stuck → Code myself → Document

---

## Progress Tracker

| No  | Problem                 | Difficulty | Pattern               | Hint? | Date     |
|-----|-------------------------|------------|-----------------------|-------|----------|
| 283 | Move Zeroes             | Easy       | Array                 | No    | May 8    |
| 9   | Palindrome Number       | Easy       | Math                  | No    | May 8    |
| 268 | Missing Number          | Easy       | Math                  | Yes   | May 9    |
| 217 | Contains Duplicate      | Easy       | Hash — Set            | No    | May 9    |
| 66  | Plus One                | Easy       | Array — Loop          | No    | May 10   |
| 485 | Max Consecutive Ones    | Easy       | Array — Counter       | No    | May 10   |
| 136 | Single Number           | Easy       | Bit — XOR             | No    | May 11   |
| 14  | Longest Common Prefix   | Easy       | String — Prefix       | Yes   | May 13   |

**Total solved: 8 | Easy: 8 | Medium: 0 | Hard: 0**

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
| Syntax / Feature        | What it means                                      |
|-------------------------|----------------------------------------------------|
| `while insert_pos < len(nums)` | Loop until a condition is met              |
| `len(nums)`             | Returns length of list                             |
| In-place modification   | Changing array without creating a new one — O(1) space |
| Two pointer technique   | Two variables pointing to different positions in array |

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
| Syntax / Feature   | What it means                                           |
|--------------------|---------------------------------------------------------|
| `x % 10`           | Modulo — gives last digit of number                    |
| `x //= 10`         | Floor division — removes last digit                    |
| `reversed * 10 + digit` | Builds reversed number digit by digit             |
| `if x < 0`         | Negative numbers can never be palindromes              |

**Time:** O(log n) | **Space:** O(1)

---

## LC 268 – Missing Number
**Date:** May 9, 2026
**Difficulty:** Easy
**Pattern:** Math — Gaussian Sum
**Hint needed:** Yes — approach only

**Approach:**
Gaussian sum formula. Expected sum of 0 to n = n*(n+1)/2.
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
| Syntax / Feature   | What it means                                           |
|--------------------|---------------------------------------------------------|
| `sum(nums)`        | Inbuilt — returns sum of all elements in list          |
| `n * (n+1) // 2`   | Gaussian sum formula for sum of 0 to n                 |
| `//`               | Floor division — returns integer, not float            |
| Alternative        | Can also solve with XOR of all indices and values      |

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
| Syntax / Feature   | What it means                                           |
|--------------------|---------------------------------------------------------|
| `set()`            | Creates empty set — stores unique elements only        |
| `seen.add(num)`    | Adds element to set                                    |
| `if num in seen`   | O(1) lookup in set — faster than list O(n)             |
| `return False`     | Outside loop — only reached if no duplicate found      |
| One liner version  | `return len(nums) != len(set(nums))`                   |

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
| Syntax / Feature              | What it means                                  |
|-------------------------------|------------------------------------------------|
| `range(len(digits)-1, -1, -1)`| Loop backwards — start, stop, step            |
| `digits[i] += 1`              | Increment element at index i                   |
| `[1] + digits`                | Prepend 1 to list — handles all 9s case       |
| Reverse loop                  | Processing array from right to left            |

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
| Syntax / Feature          | What it means                                      |
|---------------------------|----------------------------------------------------|
| `max(a, b)`               | Inbuilt — returns larger of two values             |
| `count = 0` reset         | Resetting counter when streak breaks               |
| `else: count = 0`         | Key insight — what to do when condition fails      |
| Running maximum pattern   | Track best answer seen so far inside loop          |

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
| Syntax / Feature   | What it means                                           |
|--------------------|---------------------------------------------------------|
| `^=`               | XOR assignment operator                                |
| `a ^ a = 0`        | Any number XORed with itself equals 0                  |
| `a ^ 0 = a`        | Any number XORed with 0 equals itself                  |
| XOR is commutative | Order doesn't matter — a^b^a = b                       |
| One liner          | `return reduce(lambda a,b: a^b, nums)` using functools |

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
| Syntax / Feature            | What it means                                      |
|-----------------------------|----------------------------------------------------|
| `word.startswith(prefix)`   | Returns True if word begins with prefix            |
| `prefix[:-1]`               | Remove last character from string                  |
| `not`                       | Flips True to False and False to True              |
| `while` inside `for`        | Inner loop keeps running until condition is met    |
| `[]` vs `()`                | Square brackets for slicing, round for function call |

**Time:** O(n*m) | **Space:** O(1)

---





## Template — copy this for every new problem

```
## LC [number] – [Problem Name]
**Date:** 
**Difficulty:** Easy / Medium / Hard
**Pattern:** 
**Hint needed:** Yes — approach only / No

**Approach:**

**Solution:**
```python

```

**Syntax & Inbuilt Features Learned:**
| Syntax / Feature | What it means |
|------------------|---------------|
|                  |               |

**Time:** O( ) | **Space:** O( )
```

---

## Patterns Reference

| Pattern            | Use when                                      |
|--------------------|-----------------------------------------------|
| Two Pointer        | Sorted array, pairs, in-place modification    |
| Hash / Set         | O(1) lookup, frequency count, duplicates      |
| Math               | Digit operations, formulas, number properties |
| XOR / Bit          | Find unique element, toggle, swap             |
| Array Counter      | Streak, running count, sliding window preview |
| Reverse Loop       | Process array from right to left              |
