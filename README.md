**Unit Test Assignment**
**Project Structure**

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

**Assignment Algorithms**
1. Funny String
Determines whether a string is Funny or Not Funny by comparing the list of absolute ASCII differences between consecutive characters against those of its reversed version.

Input: s = "acxz" → Output: Funny
Input: s = "ivvkj" → Output: Not Funny

2. Alternating Characters
Calculates the minimum number of deletions required so that no two consecutive characters are identical (only A and B).

Input: s = "AABAAB" → Output: 2

3. Caesar Cipher
Encrypts a string by shifting each letter by k positions down the alphabet, wrapping around as needed, while preserving case and non-alphabetic characters.

Input: s = "middle-Outz", k = 2 → Output: "okffng-Qwvb"

4. Two Characters
Finds the length of the longest sub-string that can be formed using only two distinct characters that strictly alternate.

Input: s = "beabeefeab" → Output: 5

5. Grid Challenge
Determines whether rows of a character grid can each be sorted individually so that every column is also sorted in ascending alphabetical order.

Input: grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"] → Output: YES

Getting Started
Install dependencies
<pre>pip install coverage nose2<pre>
Run the CLI
<pre>python main.py<pre>

Running Tests
Run all tests with verbose output
<pre>coverage run -m nose2 -v<pre>
Generate HTML coverage repor
<pre>coverage html<pre>
Then open htmlcov/index.html in a browser to inspect coverage.
