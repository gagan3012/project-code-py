# project-code-py
GPT-2 Model for Python Questions 
#### Demo

https://share.streamlit.io/gagan3012/project-code-py/app.py

#### Model

```
from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("gagan3012/project-code-py")

model = AutoModelWithLMHead.from_pretrained("gagan3012/project-code-py")
```

#### Question:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#### Answer:

```
Example 1:
Input: nums = [2,3,1,1,2,5]
Output: 4
Explanation: The two numbers add up to 4 because of the following rules:

1. If the target is 1, then the two numbers are equal.
2. If the target is 2, then the two numbers are equal.
3. If the target is 5, then the two numbers are equal.
4. If the target is 1, then the two numbers are equal.

Note:

1 <= nums.length <= 50000
-10000 <= nums[i] <= 10000
-10000 <= nums[i] <= 10000
"""
from typing import List
from collections import defaultdict


class Solution:
    def twoSum(self, nums: List[int]) -> int:
        """
        Let F[i] be the sum of the two sums
        F[i-1] = F[i-2] + F[i-3]
        """
        F = defaultdict(lambda: defaultdict(int))
        for i in range(len(nums)):
            F[i] = F[i-1] + F[i-2]
        return F[-1]
        
   ```
