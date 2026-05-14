# DSA — Python
> Data Structures & Algorithms in Python  
> Started: May 2026 | Target: 200+ problems by December 2026  
> Following: Code & Debug YouTube Playlist + LeetCode

---

## Stats
![Problems Solved] - 12
![Easy] - 12
![Medium] - 0
![Hard] - 0

---

## Playlist Progress — Code & Debug

| Part | Topic                                      | Status   | Key Code Written                        |
|------|--------------------------------------------|----------|-----------------------------------------|
| 1    | DSA Python Course Intro                    | ✅ Done | —                                       |
| 2    | Time & Space Complexity                    | ✅ Done | complexity_notes.md                     |
| 3    | What is TLE Error                          | ✅ Done | —                                       |
| 4    | Time Complexity of Python Operations       | ✅ Done | python_operation_costs.md               |
| 5    | Extraction of Digits Using Loops           | ✅ Done | digit_extraction.py                     |
| 6    | Count Number of Digits in Integer          | ✅ Done | count_digits.py                         |
| 7    | Check if Number is Palindrome              | ✅ Done | palindrome_number.py                    |
| 8    | Armstrong Number                           | ✅ Done | armstrong.py                            |
| 9    | Print All Factors of Given Number          | ✅ Done | all_factors.py                          |
| 10   | Store Frequency in Dictionary              | ✅ Done | frequency_counter.py                    |
| 11   | Introduction to Hashing in Python          | ✅ Done | two_sum.py                    |
---

## Concepts Learned from Playlist

### Part 2 — Time & Space Complexity
- Big O notation: O(1), O(n), O(n²), O(log n)
- Space complexity vs time complexity
- How to analyze any code's complexity

### Part 4 — Python Operation Costs
| Operation           | Time Complexity |
|---------------------|-----------------|
| `list.append()`     | O(1)            |
| `list.insert(0, x)` | O(n)            |
| `dict[key]`         | O(1)            |
| `x in list`         | O(n)            |
| `x in set`          | O(1)            |
| `sorted()`          | O(n log n)      |
| `list.sort()`       | O(n log n)      |

### Part 5 — Digit Extraction
```python
# Extract all digits from a number
from math import sqrt

def extract_digits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return digits
```
**Learned:** `% 10` extracts last digit | `// 10` removes last digit

### Part 6 — Count Digits
```python
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
```
**Learned:** Keep dividing by 10 until number becomes 0

### Part 7 — Palindrome Number
```python
def is_palindrome(num):
    original = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return original == reversed_num
```
**Learned:** Reverse number mathematically | Negative = never palindrome

### Part 8 — Armstrong Number
```python
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    n = len(digits)
    return sum(d**n for d in digits) == num
```
**Learned:** Armstrong = sum of each digit raised to power of digit count
Example: 153 = 1³ + 5³ + 3³ = 153 ✅

### Part 9 — All Factors
```python
from math import sqrt

def all_factors(num):
    result = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            result.append(i)
            if num // i != i:
                result.append(num // i)
    result.sort()
    return result
```
**Learned:** `from math import sqrt` | Only loop to √n for efficiency | O(√n) vs O(n)

### Part 10 — Frequency Counter (Hashing)
```python
nums = [5, 6, 7, 7, 1, 9, 10, 1, 1, 5]
hash_map = dict()
for num in nums:
    hash_map[num] = hash_map.get(num, 0) + 1
print(hash_map)
# {5: 2, 6: 1, 7: 2, 1: 3, 9: 1, 10: 1}
```
**Learned:** `dict.get(key, 0)` — safe way to get value with default | Foundation of hashing

---

## Problem Tracker

| No  | Problem                       | Difficulty | Pattern                   | File                                                    |
|-----|-------------------------------|------------|---------------------------|---------------------------------------------------------|
| 283 | Move Zeroes                   | Easy       | Array — Two Pointer       | [link](./01_Arrays/move_zeroes.py)                      |
| 9   | Palindrome Number             | Easy       | Math — Digit Reversal     | [link](./01_Arrays/palindrome_number.py)                |
| 268 | Missing Number                | Easy       | Math — Gaussian Sum       | [link](./01_Arrays/missing_number.py)                   |
| 217 | Contains Duplicate            | Easy       | Hash — Set                | [link](./03_Hashing/contains_duplicate.py)              |
| 66  | Plus One                      | Easy       | Array — Reverse Loop      | [link](./01_Arrays/plus_one.py)                         |
| 485 | Max Consecutive Ones          | Easy       | Array — Counter           | [link](./01_Arrays/max_consecutive_ones.py)             |
| 136 | Single Number                 | Easy       | Bit — XOR                 | [link](./01_Arrays/single_number.py)                    |
| 14  | Longest Common Prefix         | Easy       | String — Shrinking Prefix | [link](./02_Strings/longest_common_prefix.py)           |
| 242 | Valid Anagram                 | Easy       | Hash — Dictionary         | [link](./02_Strings/valid_anagram.py)                   |
| 13  | Roman to Integer              | Easy       | Hash — Subtractive Rule   | [link](./02_Strings/roman_to_integer.py)                |
| 26  | Remove Duplicates Sorted Array| Easy       | Array — Two Pointer       | [link](./01_Arrays/remove_duplicates_sorted.py)         |
| 1   | Two Sum                       | Easy       | Hash — Complement         | [link](./03_Hashing/two_sum.py)                         |

---

## Inbuilt Functions Used So Far

| Function / Syntax       | What it does                                      | First used in  |
|-------------------------|---------------------------------------------------|----------------|
| `len(x)`                | Length of list/string                             | LC 283         |
| `sum(nums)`             | Sum of all elements in list                       | LC 268         |
| `max(a, b)`             | Returns larger of two values                      | LC 485         |
| `set()`                 | Creates set — unique elements, O(1) lookup        | LC 217         |
| `set.add(x)`            | Adds element to set                               | LC 217         |
| `dict()`                | Creates empty dictionary                          | LC 242         |
| `dict.get(key, default)`| Get value safely with fallback default            | LC 242         |
| `str.startswith(prefix)`| True if string starts with given prefix           | LC 14          |
| `sorted()`              | Returns new sorted list                           | Playlist P4    |
| `range(a, b, step)`     | Generate sequence with start, stop, step          | LC 66          |
| `from math import sqrt` | Square root function                              | Playlist P9    |
| `int(sqrt(num))`        | Convert float sqrt to integer                     | Playlist P9    |

---

## Connect
- GitHub: [github.com/Nishant3035](https://github.com/Nishant3035)
- LinkedIn: [Nishant Chaurasia](https://linkedin.com/in/nishant-chaurasia)
- LeetCode Journal: [progress/leetcode_journal.md](./progress/leetcode_journal.md)