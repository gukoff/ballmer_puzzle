# Winning strategy for Steve Ballmer's puzzle

This repository accompanies my blog post **["Steve Ballmer was wrong"](https://gukov.dev/puzzles/math/2024/09/05/steve-ballmer-was-wrong.html)** and its **[discussion on Hacker News](https://news.ycombinator.com/item?id=41463330)**.

It contains the code for calculating the winning strategy for the Steve Ballmer's [favorite interview question](https://youtu.be/svCYbkS0Sjk?t=35).

## Expected wins

> Note: these numbers were significantly improved by adding the [new pure strategies](https://github.com/gukoff/ballmer_puzzle/pull/1).

- Average win if Ballmer chooses randomly: **$0.16247848000093373**
- Worst win if Ballmer chooses adversarially: **$0.14657033010415613**

## Winning strategy

```
- With probability 0.4714%: Binary search, first guess 29. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.1691%: Binary search, first guess 33. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 1.8980%: Binary search, first guess 35. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 1.0756%: Binary search, first guess 36. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.9380%: Binary search, first guess 38. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 2.1506%: Binary search, first guess 39. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 1.0748%: Binary search, first guess 40. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.3139%: Binary search, first guess 41. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.1320%: Binary search, first guess 42. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 1.6595%: Binary search, first guess 43. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 2.2414%: Binary search, first guess 45. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 2.6079%: Binary search, first guess 46. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.2419%: Binary search, first guess 47. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.2846%: Binary search, first guess 48. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 2.1876%: Binary search, first guess 49. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 2.3532%: Binary search, first guess 51. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.3965%: Binary search, first guess 52. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.3438%: Binary search, first guess 54. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 1.1541%: Binary search, first guess 55. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.5423%: Binary search, first guess 56. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.7888%: Binary search, first guess 57. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.3958%: Binary search, first guess 58. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.2583%: Binary search, first guess 59. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 1.0835%: Binary search, first guess 60. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 3.3341%: Binary search, first guess 62. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.1299%: Binary search, first guess 63. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.9844%: Binary search, first guess 70. On each step, guess the middle element in the interval. In case of tie, guess the left one.
- With probability 0.9844%: Binary search, first guess 29. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.1299%: Binary search, first guess 36. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 3.3341%: Binary search, first guess 37. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 1.0835%: Binary search, first guess 39. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.2583%: Binary search, first guess 40. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.3958%: Binary search, first guess 41. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.7888%: Binary search, first guess 42. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.5423%: Binary search, first guess 43. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 1.1541%: Binary search, first guess 44. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.3438%: Binary search, first guess 45. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.3965%: Binary search, first guess 47. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 2.3532%: Binary search, first guess 48. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 2.1876%: Binary search, first guess 50. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.2846%: Binary search, first guess 51. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.2419%: Binary search, first guess 52. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 2.6079%: Binary search, first guess 53. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 2.2414%: Binary search, first guess 54. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 1.6595%: Binary search, first guess 56. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.1320%: Binary search, first guess 57. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.3139%: Binary search, first guess 58. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 1.0748%: Binary search, first guess 59. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 2.1506%: Binary search, first guess 60. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.9380%: Binary search, first guess 61. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 1.0756%: Binary search, first guess 63. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 1.8980%: Binary search, first guess 64. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.1691%: Binary search, first guess 66. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 0.4714%: Binary search, first guess 70. On each step, guess the middle element in the interval. In case of tie, guess the right one.
- With probability 1.7818%: Binary search, first guess is 43. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 2.3210%: Binary search, first guess is 46. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 3.7722%: Binary search, first guess is 47. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 0.6580%: Binary search, first guess is 51. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 1.1608%: Binary search, first guess is 55. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 1.1608%: Binary search, first guess is 44. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 0.6580%: Binary search, first guess is 48. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 3.7722%: Binary search, first guess is 52. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 2.3210%: Binary search, first guess is 53. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 1.7818%: Binary search, first guess is 56. On each step, guess the leftmost element in the interval that won't increase the worst-case complexity.
- With probability 2.1310%: Binary search, first guess is 42. On each step, guess the endmost element in the interval that won't increase the worst-case complexity.
- With probability 1.1045%: Binary search, first guess is 43. On each step, guess the endmost element in the interval that won't increase the worst-case complexity.
- With probability 1.5560%: Binary search, first guess is 45. On each step, guess the endmost element in the interval that won't increase the worst-case complexity.
- With probability 2.4735%: Binary search, first guess is 48. On each step, guess the endmost element in the interval that won't increase the worst-case complexity.
- With probability 3.8304%: Binary search, first guess is 49. On each step, guess the endmost element in the interval that won't increase the worst-case complexity.
- With probability 3.8304%: Binary search, first guess is 50. On each step, guess the endmost element in the interval that won't increase the worst-case complexity.
- With probability 2.4735%: Binary search, first guess is 51. On each step, guess the endmost element in the interval that won't increase the worst-case complexity.
- With probability 1.5560%: Binary search, first guess is 54. On each step, guess the endmost element in the interval that won't increase the worst-case complexity.
- With probability 1.1045%: Binary search, first guess is 56. On each step, guess the endmost element in the interval that won't increase the worst-case complexity.
- With probability 2.1310%: Binary search, first guess is 57. On each step, guess the endmost element in the interval that won't increase the worst-case complexity.
```

## Average wins for each number

```
0: $0.1466 (stdev $1.1153)
1: $0.2995 (stdev $1.0170)
2: $0.1821 (stdev $1.0526)
3: $0.1881 (stdev $1.0353)
4: $0.1466 (stdev $1.1179)
5: $0.1487 (stdev $1.0283)
6: $0.1466 (stdev $1.0925)
7: $0.1503 (stdev $1.0921)
8: $0.1466 (stdev $1.0836)
9: $0.1466 (stdev $1.1338)
10: $0.1466 (stdev $1.1684)
11: $0.1466 (stdev $1.0660)
12: $0.1561 (stdev $1.1422)
13: $0.1466 (stdev $1.1218)
14: $0.2245 (stdev $1.1609)
15: $0.1466 (stdev $1.1706)
16: $0.1466 (stdev $1.1520)
17: $0.1466 (stdev $1.1775)
18: $0.1466 (stdev $1.2168)
19: $0.1839 (stdev $1.1657)
20: $0.1664 (stdev $1.1329)
21: $0.1466 (stdev $1.1533)
22: $0.1466 (stdev $1.1941)
23: $0.1466 (stdev $1.0873)
24: $0.1466 (stdev $1.2145)
25: $0.1466 (stdev $1.1765)
26: $0.1466 (stdev $1.1587)
27: $0.1466 (stdev $1.1154)
28: $0.1466 (stdev $1.1682)
29: $0.1466 (stdev $1.1821)
30: $0.1466 (stdev $1.1878)
31: $0.3072 (stdev $1.2490)
32: $0.1925 (stdev $1.0992)
33: $0.1466 (stdev $1.1537)
34: $0.2938 (stdev $1.1130)
35: $0.1466 (stdev $1.1692)
36: $0.1466 (stdev $1.1370)
37: $0.1466 (stdev $1.1788)
38: $0.1466 (stdev $1.1310)
39: $0.2077 (stdev $1.2382)
40: $0.1466 (stdev $1.1347)
41: $0.1466 (stdev $1.1259)
42: $0.1466 (stdev $1.1718)
43: $0.1466 (stdev $1.2319)
44: $0.1466 (stdev $1.1465)
45: $0.1466 (stdev $1.2171)
46: $0.1466 (stdev $1.2385)
47: $0.1466 (stdev $1.2202)
48: $0.1466 (stdev $1.2658)
49: $0.1466 (stdev $1.2341)
50: $0.1466 (stdev $1.2341)
51: $0.1466 (stdev $1.2658)
52: $0.1466 (stdev $1.2202)
53: $0.1466 (stdev $1.2385)
54: $0.1466 (stdev $1.2171)
55: $0.1466 (stdev $1.1465)
56: $0.1466 (stdev $1.2319)
57: $0.1466 (stdev $1.1718)
58: $0.1466 (stdev $1.1259)
59: $0.1466 (stdev $1.1347)
60: $0.2077 (stdev $1.2382)
61: $0.1466 (stdev $1.1310)
62: $0.1466 (stdev $1.1788)
63: $0.1466 (stdev $1.1370)
64: $0.1466 (stdev $1.1692)
65: $0.2938 (stdev $1.1130)
66: $0.1466 (stdev $1.1537)
67: $0.1925 (stdev $1.0992)
68: $0.3072 (stdev $1.2490)
69: $0.1466 (stdev $1.1878)
70: $0.1466 (stdev $1.1821)
71: $0.1466 (stdev $1.1682)
72: $0.1466 (stdev $1.1154)
73: $0.1466 (stdev $1.1587)
74: $0.1466 (stdev $1.1765)
75: $0.1466 (stdev $1.2145)
76: $0.1466 (stdev $1.0873)
77: $0.1466 (stdev $1.1941)
78: $0.1466 (stdev $1.1533)
79: $0.1664 (stdev $1.1329)
80: $0.1839 (stdev $1.1657)
81: $0.1466 (stdev $1.2168)
82: $0.1466 (stdev $1.1775)
83: $0.1466 (stdev $1.1520)
84: $0.1466 (stdev $1.1706)
85: $0.2245 (stdev $1.1609)
86: $0.1466 (stdev $1.1218)
87: $0.1561 (stdev $1.1422)
88: $0.1466 (stdev $1.0660)
89: $0.1466 (stdev $1.1684)
90: $0.1466 (stdev $1.1338)
91: $0.1466 (stdev $1.0836)
92: $0.1503 (stdev $1.0921)
93: $0.1466 (stdev $1.0925)
94: $0.1487 (stdev $1.0283)
95: $0.1466 (stdev $1.1179)
96: $0.1881 (stdev $1.0353)
97: $0.1821 (stdev $1.0526)
98: $0.2995 (stdev $1.0170)
99: $0.1466 (stdev $1.1153)
```
