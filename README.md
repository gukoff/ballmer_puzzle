# Winning strategy for Steve Ballmer's puzzle

This repository accompanies my blog post **["Steve Ballmer was wrong"](https://gukov.dev/puzzles/math/2024/09/05/steve-ballmer-was-wrong.html)** and its **[discussion on Hacker News](https://news.ycombinator.com/item?id=41463330)**.

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
0:  $0.0722 (stdev $1.1909)
1:  $0.1692 (stdev $1.0052)
2:  $0.0931 (stdev $1.0305)
3:  $0.2314 (stdev $0.9708)
4:  $0.1192 (stdev $1.1551)
5:  $0.1202 (stdev $1.0224)
6:  $0.1189 (stdev $1.1094)
7:  $0.3720 (stdev $1.1522)
8:  $0.1669 (stdev $1.1232)
9:  $0.0722 (stdev $1.1521)
10: $0.0722 (stdev $1.1824)
11: $0.0722 (stdev $1.0524)
12: $0.0722 (stdev $1.0822)
13: $0.0722 (stdev $1.0855)
14: $0.2996 (stdev $1.2313)
15: $0.3514 (stdev $1.2692)
16: $0.0722 (stdev $1.1805)
17: $0.0722 (stdev $1.0605)
18: $0.0722 (stdev $1.1636)
19: $0.0814 (stdev $1.1115)
20: $0.0722 (stdev $1.1369)
21: $0.0722 (stdev $1.1671)
22: $0.0722 (stdev $1.1568)
23: $0.2883 (stdev $1.1445)
24: $0.0722 (stdev $1.2184)
25: $0.0722 (stdev $1.1517)
26: $0.0722 (stdev $1.1814)
27: $0.0722 (stdev $1.0677)
28: $0.0722 (stdev $1.1884)
29: $0.0722 (stdev $1.1886)
30: $0.0722 (stdev $1.2442)
31: $0.5090 (stdev $1.3727)
32: $0.0722 (stdev $1.1316)
33: $0.0722 (stdev $1.0962)
34: $0.0722 (stdev $1.1192)
35: $0.0740 (stdev $1.0778)
36: $0.0722 (stdev $1.1974)
37: $0.1143 (stdev $1.1976)
38: $0.0722 (stdev $1.2222)
39: $0.1617 (stdev $1.1836)
40: $0.1864 (stdev $1.3068)
41: $0.0722 (stdev $1.1240)
42: $0.0722 (stdev $1.1877)
43: $0.0722 (stdev $1.1176)
44: $0.0722 (stdev $1.1380)
45: $0.0722 (stdev $1.1927)
46: $0.0722 (stdev $1.2688)
47: $0.2488 (stdev $1.2719)
48: $0.1019 (stdev $1.2546)
49: $0.0967 (stdev $1.1413)
50: $0.0967 (stdev $1.1413)
51: $0.1019 (stdev $1.2546)
52: $0.2488 (stdev $1.2719)
53: $0.0722 (stdev $1.2688)
54: $0.0722 (stdev $1.1927)
55: $0.0722 (stdev $1.1380)
56: $0.0722 (stdev $1.1176)
57: $0.0722 (stdev $1.1877)
58: $0.0722 (stdev $1.1240)
59: $0.1864 (stdev $1.3068)
60: $0.1617 (stdev $1.1836)
61: $0.0722 (stdev $1.2222)
62: $0.1143 (stdev $1.1976)
63: $0.0722 (stdev $1.1974)
64: $0.0740 (stdev $1.0778)
65: $0.0722 (stdev $1.1192)
66: $0.0722 (stdev $1.0962)
67: $0.0722 (stdev $1.1316)
68: $0.5090 (stdev $1.3727)
69: $0.0722 (stdev $1.2442)
70: $0.0722 (stdev $1.1886)
71: $0.0722 (stdev $1.1884)
72: $0.0722 (stdev $1.0677)
73: $0.0722 (stdev $1.1814)
74: $0.0722 (stdev $1.1517)
75: $0.0722 (stdev $1.2184)
76: $0.2883 (stdev $1.1445)
77: $0.0722 (stdev $1.1568)
78: $0.0722 (stdev $1.1671)
79: $0.0722 (stdev $1.1369)
80: $0.0814 (stdev $1.1115)
81: $0.0722 (stdev $1.1636)
82: $0.0722 (stdev $1.0605)
83: $0.0722 (stdev $1.1805)
84: $0.3514 (stdev $1.2692)
85: $0.2996 (stdev $1.2313)
86: $0.0722 (stdev $1.0855)
87: $0.0722 (stdev $1.0822)
88: $0.0722 (stdev $1.0524)
89: $0.0722 (stdev $1.1824)
90: $0.0722 (stdev $1.1521)
91: $0.1669 (stdev $1.1232)
92: $0.3720 (stdev $1.1522)
93: $0.1189 (stdev $1.1094)
94: $0.1202 (stdev $1.0224)
95: $0.1192 (stdev $1.1551)
96: $0.2314 (stdev $0.9708)
97: $0.0931 (stdev $1.0305)
98: $0.1692 (stdev $1.0052)
99: $0.0722 (stdev $1.1909)
```
