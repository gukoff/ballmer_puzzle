# Winning strategy for Steve Ballmer's puzzle

TODO - link to the blog article.

## Expected wins

- Average win if Ballmer chooses randomly: **$0.12143596781369118**
- Worst win if Ballmer chooses adversarially: **$0.07224557629674774**

## Winning strategy

```
- With probability 0.4239%: [also mirror this strategy with 50% probability] Binary search, first guess is 29. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.0900%: [also mirror this strategy with 50% probability] Binary search, first guess is 33. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.5114%: [also mirror this strategy with 50% probability] Binary search, first guess is 38. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 1.3781%: [also mirror this strategy with 50% probability] Binary search, first guess is 39. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.4481%: [also mirror this strategy with 50% probability] Binary search, first guess is 42. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 5.4421%: [also mirror this strategy with 50% probability] Binary search, first guess is 43. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 4.6561%: [also mirror this strategy with 50% probability] Binary search, first guess is 45. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 3.9196%: [also mirror this strategy with 50% probability] Binary search, first guess is 46. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 2.4085%: [also mirror this strategy with 50% probability] Binary search, first guess is 47. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 4.9852%: [also mirror this strategy with 50% probability] Binary search, first guess is 49. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 3.6889%: [also mirror this strategy with 50% probability] Binary search, first guess is 51. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.9332%: [also mirror this strategy with 50% probability] Binary search, first guess is 53. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.4183%: [also mirror this strategy with 50% probability] Binary search, first guess is 54. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.8884%: [also mirror this strategy with 50% probability] Binary search, first guess is 55. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 1.3072%: [also mirror this strategy with 50% probability] Binary search, first guess is 57. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 4.6627%: [also mirror this strategy with 50% probability] Binary search, first guess is 59. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 0.1043%: [also mirror this strategy with 50% probability] Binary search, first guess is 60. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 7.1026%: [also mirror this strategy with 50% probability] Binary search, first guess is 61. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 7.5506%: [also mirror this strategy with 50% probability] Binary search, first guess is 62. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 3.3419%: [also mirror this strategy with 50% probability] Binary search, first guess is 70. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 1.3820%: [also mirror this strategy with 50% probability] Binary search, first guess is 71. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 1.9686%: [also mirror this strategy with 50% probability] Binary search, first guess is 73. On each step, guess the middle element in the interval, in case of tie guess the left one.
- With probability 1.9372%: [also mirror this strategy with 50% probability] Binary search, first guess is 1. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 1.4269%: [also mirror this strategy with 50% probability] Binary search, first guess is 18. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 5.4576%: [also mirror this strategy with 50% probability] Binary search, first guess is 46. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 8.3833%: [also mirror this strategy with 50% probability] Binary search, first guess is 51. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 4.1314%: [also mirror this strategy with 50% probability] Binary search, first guess is 57. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 5.3279%: [also mirror this strategy with 50% probability] Binary search, first guess is 58. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 10.4418%: [also mirror this strategy with 50% probability] Binary search, first guess is 59. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.
- With probability 5.2822%: [also mirror this strategy with 50% probability] Binary search, first guess is 63. On each step, guess the rightmost element in the interval that won't increase the worst-case complexity.

```

## Average wins for each number

```
0: 0.0722455762967486
1: 0.16917030189852314
2: 0.09310409154626963
3: 0.231428364061588
4: 0.1192028868849244
5: 0.12018494251249995
6: 0.11886752289608296
7: 0.3720064174271922
8: 0.16691619252562442
9: 0.07224557629674846
10: 0.07224557629674846
11: 0.0722455762967486
12: 0.07224557629674849
13: 0.07224557629674858
14: 0.2995745151575407
15: 0.35139893864421123
16: 0.07224557629674858
17: 0.07224557629674974
18: 0.07224557629674883
19: 0.08142588487295806
20: 0.07224557629674838
21: 0.07224557629674835
22: 0.07224557629674885
23: 0.288312119642362
24: 0.07224557629674797
25: 0.0722455762967483
26: 0.07224557629674838
27: 0.07224557629674848
28: 0.07224557629674844
29: 0.07224557629674841
30: 0.07224557629674858
31: 0.5089700836005978
32: 0.07224557629674805
33: 0.07224557629674888
34: 0.0722455762967498
35: 0.07400672407553734
36: 0.07224557629674834
37: 0.11432803941624262
38: 0.07224557629674866
39: 0.16168724964553413
40: 0.1864218504470468
41: 0.0722455762967485
42: 0.07224557629674846
43: 0.07224557629674855
44: 0.07224557629674849
45: 0.0722455762967488
46: 0.07224557629674774
47: 0.24879186587947671
48: 0.10193127193472226
49: 0.09670183871316737
50: 0.09670183871316737
51: 0.10193127193472226
52: 0.24879186587947671
53: 0.07224557629674774
54: 0.0722455762967488
55: 0.07224557629674849
56: 0.07224557629674855
57: 0.07224557629674846
58: 0.0722455762967485
59: 0.1864218504470468
60: 0.16168724964553413
61: 0.07224557629674866
62: 0.11432803941624262
63: 0.07224557629674834
64: 0.07400672407553734
65: 0.0722455762967498
66: 0.07224557629674888
67: 0.07224557629674805
68: 0.5089700836005978
69: 0.07224557629674858
70: 0.07224557629674841
71: 0.07224557629674844
72: 0.07224557629674848
73: 0.07224557629674838
74: 0.0722455762967483
75: 0.07224557629674797
76: 0.288312119642362
77: 0.07224557629674885
78: 0.07224557629674835
79: 0.07224557629674838
80: 0.08142588487295806
81: 0.07224557629674883
82: 0.07224557629674974
83: 0.07224557629674858
84: 0.35139893864421123
85: 0.2995745151575407
86: 0.07224557629674858
87: 0.07224557629674849
88: 0.0722455762967486
89: 0.07224557629674846
90: 0.07224557629674846
91: 0.16691619252562442
92: 0.3720064174271922
93: 0.11886752289608296
94: 0.12018494251249995
95: 0.1192028868849244
96: 0.231428364061588
97: 0.09310409154626963
98: 0.16917030189852314
99: 0.0722455762967486
```
