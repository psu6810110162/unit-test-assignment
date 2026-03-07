# Unit Test Assignment

**6810110162 — Teerayut Siri**  
Computer Engineering, Prince of Songkla University  
Course: 240-123 Module Data Structure, Algorithms and Programming 

---

## Project Structure

```
unit-test-assignment/
├── _6810110162/                    # Production code
│   ├── __init__.py
│   ├── funny_string.py
│   ├── alternating_characters.py
│   ├── caesar_cipher.py
│   ├── two_characters.py
│   ├── grid_challenge.py
│   └── result_reporter.py          # Service layer (used for stub testing)
├── tests/                          # Test code
│   ├── __init__.py
│   ├── test_funny_string.py
│   ├── test_alternating_characters.py
│   ├── test_caesar_cipher.py
│   ├── test_two_characters.py
│   ├── test_grid_challenge.py
│   └── test_stubs.py               # Stub / Mock / Spy test doubles
├── main.py                         # Interactive CLI
└── pyproject.toml
```

---

## Assignment Algorithms

### 1. Funny String
Determines whether a string is **Funny** or **Not Funny** by comparing the list of absolute ASCII differences between consecutive characters against those of its reversed version.

- Input: `s = "acxz"` → Output: `Funny`
- Input: `s = "ivvkj"` → Output: `Not Funny`

### 2. Alternating Characters
Calculates the minimum number of deletions required so that no two consecutive characters are identical (only `A` and `B`).

- Input: `s = "AABAAB"` → Output: `2`

### 3. Caesar Cipher
Encrypts a string by shifting each letter by `k` positions down the alphabet, wrapping around as needed, while preserving case and non-alphabetic characters.

- Input: `s = "middle-Outz", k = 2` → Output: `"okffng-Qwvb"`

### 4. Two Characters
Finds the length of the longest sub-string that can be formed using only two distinct characters that strictly alternate.

- Input: `s = "beabeefeab"` → Output: `5`

### 5. Grid Challenge
Determines whether rows of a character grid can each be sorted individually so that every column is also sorted in ascending alphabetical order.

- Input: `grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]` → Output: `YES`

---

## Getting Started

### Install dependencies

```bash
pip install coverage nose2
```

### Run the CLI

```bash
python main.py
```

---

## Running Tests

### Run all tests with verbose output

```bash
coverage run -m nose2 -v
```

### Generate HTML coverage report

```bash
coverage html
```

Then open `htmlcov/index.html` in a browser to inspect coverage.

---

## Test Summary

| Test File | Cases | Coverage |
|---|---|---|
| test_funny_string.py | 13 | 100% |
| test_alternating_characters.py | 14 | 100% |
| test_caesar_cipher.py | 14 | 100% |
| test_two_characters.py | 14 | 100% |
| test_grid_challenge.py | 14 | 100% |
| test_stubs.py | 15 | 100% |
| **Total** | **86** | **99%** |

---

## Test Doubles (Stub / Mock / Spy)

`tests/test_stubs.py` demonstrates three Test Double patterns using `unittest.mock`:

- **Stub** — replaces `open()` with `mock_open` so tests run without touching the real file system
- **Mock** — verifies that `write()` was called with the exact expected value (behaviour verification)
- **Spy** — wraps the real function with `MagicMock(wraps=func)` to record calls while still executing original logic

---

## References

- https://realpython.com/python-testing/
- https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/
- https://docs.python.org/3/library/unittest.mock.html
- https://www.guru99.com/code-coverage.html
