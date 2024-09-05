# Winning strategy for Steve Ballmer's puzzle

This repository accompanies the article on my blog: **["Steve Ballmer was wrong"](https://gukov.dev/puzzles/math/2024/09/05/steve-ballmer-was-wrong.html)**.

It contains the code for calculating the winning strategy for the Steve Ballmer's [favorite interview question](https://youtu.be/svCYbkS0Sjk?t=35).

## Expected wins

- Average win if Ballmer chooses randomly: **$0.12143596781376992**
- Worst win if Ballmer chooses adversarially: **$0.07224557629493805**

## Winning strategy

```
- With probability 0.2120%: Binary search, first guess is 29. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.0450%: Binary search, first guess is 33. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.2557%: Binary search, first guess is 38. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.6890%: Binary search, first guess is 39. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.2241%: Binary search, first guess is 42. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 2.7210%: Binary search, first guess is 43. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 2.3280%: Binary search, first guess is 45. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 1.9598%: Binary search, first guess is 46. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 1.2043%: Binary search, first guess is 47. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 2.4926%: Binary search, first guess is 49. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 1.8444%: Binary search, first guess is 51. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.4666%: Binary search, first guess is 53. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.2091%: Binary search, first guess is 54. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.4442%: Binary search, first guess is 55. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.6536%: Binary search, first guess is 57. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 2.3314%: Binary search, first guess is 59. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.0521%: Binary search, first guess is 60. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 3.5513%: Binary search, first guess is 61. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 3.7753%: Binary search, first guess is 62. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 1.6710%: Binary search, first guess is 70. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.6910%: Binary search, first guess is 71. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.9843%: Binary search, first guess is 73. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.9843%: Binary search, first guess is 26. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.6910%: Binary search, first guess is 28. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 1.6710%: Binary search, first guess is 29. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 3.7753%: Binary search, first guess is 37. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 3.5513%: Binary search, first guess is 38. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.0521%: Binary search, first guess is 39. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 2.3314%: Binary search, first guess is 40. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.6536%: Binary search, first guess is 42. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.4442%: Binary search, first guess is 44. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.2091%: Binary search, first guess is 45. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.4666%: Binary search, first guess is 46. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 1.8444%: Binary search, first guess is 48. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 2.4926%: Binary search, first guess is 50. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 1.2043%: Binary search, first guess is 52. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 1.9598%: Binary search, first guess is 53. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 2.3280%: Binary search, first guess is 54. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 2.7210%: Binary search, first guess is 56. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.2241%: Binary search, first guess is 57. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.6890%: Binary search, first guess is 60. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.2557%: Binary search, first guess is 61. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.0450%: Binary search, first guess is 66. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.2120%: Binary search, first guess is 70. On each step, guess the middle element in the interval, in case of tie guess the right one.
- With probability 0.9686%: Binary search, first guess is 1. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 0.7134%: Binary search, first guess is 18. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 2.7288%: Binary search, first guess is 46. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 4.1917%: Binary search, first guess is 51. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 2.0657%: Binary search, first guess is 57. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 2.6639%: Binary search, first guess is 58. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 5.2209%: Binary search, first guess is 59. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 2.6411%: Binary search, first guess is 63. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 2.6411%: Binary search, first guess is 36. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 5.2209%: Binary search, first guess is 40. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 2.6639%: Binary search, first guess is 41. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 2.0657%: Binary search, first guess is 42. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 4.1917%: Binary search, first guess is 48. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 2.7288%: Binary search, first guess is 53. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 0.7134%: Binary search, first guess is 81. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 0.9686%: Binary search, first guess is 98. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
```

## Average wins for each number

```
0: $0.0722
1: $0.1692
2: $0.0931
3: $0.2314
4: $0.1192
5: $0.1202
6: $0.1189
7: $0.3720
8: $0.1669
9: $0.0722
10: $0.0722
11: $0.0722
12: $0.0722
13: $0.0722
14: $0.2996
15: $0.3514
16: $0.0722
17: $0.0722
18: $0.0722
19: $0.0814
20: $0.0722
21: $0.0722
22: $0.0722
23: $0.2883
24: $0.0722
25: $0.0722
26: $0.0722
27: $0.0722
28: $0.0722
29: $0.0722
30: $0.0722
31: $0.5090
32: $0.0722
33: $0.0722
34: $0.0722
35: $0.0740
36: $0.0722
37: $0.1143
38: $0.0722
39: $0.1617
40: $0.1864
41: $0.0722
42: $0.0722
43: $0.0722
44: $0.0722
45: $0.0722
46: $0.0722
47: $0.2488
48: $0.1019
49: $0.0967
50: $0.0967
51: $0.1019
52: $0.2488
53: $0.0722
54: $0.0722
55: $0.0722
56: $0.0722
57: $0.0722
58: $0.0722
59: $0.1864
60: $0.1617
61: $0.0722
62: $0.1143
63: $0.0722
64: $0.0740
65: $0.0722
66: $0.0722
67: $0.0722
68: $0.5090
69: $0.0722
70: $0.0722
71: $0.0722
72: $0.0722
73: $0.0722
74: $0.0722
75: $0.0722
76: $0.2883
77: $0.0722
78: $0.0722
79: $0.0722
80: $0.0814
81: $0.0722
82: $0.0722
83: $0.0722
84: $0.3514
85: $0.2996
86: $0.0722
87: $0.0722
88: $0.0722
89: $0.0722
90: $0.0722
91: $0.1669
92: $0.3720
93: $0.1189
94: $0.1202
95: $0.1192
96: $0.2314
97: $0.0931
98: $0.1692
99: $0.0722
```
