This problem is about candy. Initially, you only have 1 candy, and you want to have exactly n candies.

You can use the two following spells in any order at most 40 times in total.

Assume you have x candies now. If you use the first spell, then x candies become 2x−1 candies. Assume you have x candies now. If you use the second spell, then x candies become 2x+1 candies. Construct a sequence of spells, such that after using them in order, you will have exactly n candies, or determine it's impossible.

Input
Each test contains multiple test cases. The first line contains a single integer t
 (1≤t≤104
) — the number of test cases. Their description follows.

Each test case contains one line with a single integer n
 (2≤n≤109
) — the required final number of candies.

Output
For each test case, output the following.

If it's possible to eventually have n
 candies within 40
 spells, in the first line print an integer m
 (1≤m≤40
), representing the total number of spells you use.

In the second print m
 integers a1,a2,…,am
 (ai
 is 1
 or 2
) separated by spaces, where ai=1
 means that you use the first spell in the i
-th step, while ai=2
 means that you use the second spell in the i
-th step.

Note that you do not have to minimize m
, and if there are multiple solutions, you may output any one of them.

If it's impossible, output −1
 in one line.
