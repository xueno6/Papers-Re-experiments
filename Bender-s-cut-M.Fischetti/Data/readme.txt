All files contain a (possibly infeasible) system Ax <= b with the
following scheme (all fields are separated by a tab):

1) First line: number of variables n, number of constraint m, number
of nonzeros nnz;

2) Lines 2 to n+1: each line contains lower and upper bound of all
variables (-/+ 1e30 if unbounded);

3) lines n+2 + n+m+1: each line describes an inequality with K terms 

$$l <= \sum_{k=1..K} a_{i(k)} x_{i(k)} <= u 
$$
with a list of numbers (separated by tab) such that:

  - the first number is K, the number of variables in the inequality

  - the second and third are l and u, respectively. Note: either
    l=-1e30 or u=1e30, i.e., for now Creme only deals with
    inequalities;

  - the remaining 2K elements are pairs (index,coefficient), i.e.,
    $i(k)$ and $a_{i(k)}$

A translator from .lp to this compact format is in the works and will
be included in an early revision of Creme.
