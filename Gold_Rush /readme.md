Initially you have a single pile with n
 gold nuggets. In an operation you can do the following:

Take any pile and split it into two piles, so that one of the resulting piles has exactly twice as many gold nuggets as the other. (All piles should have an integer number of nuggets.)

One possible move is to take a pile of size 6
 and split it into piles of sizes 2
 and 4
, which is valid since 4
 is twice as large as 2
.

Can you make a pile with exactly m
 gold nuggets using zero or more operations?

 
Input: 

The first line contains an integer t
 (1≤t≤1000
) — the number of test cases.

The only line of each test case contains two integers n
 and m
 (1≤n,m≤107
) — the starting and target pile sizes, respectively.


Output: 

For each test case, output "YES" if you can make a pile of size exactly m
, and "NO" otherwise.

You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).

