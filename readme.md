Author: Jason Garcia Solorzano

to run simply run python3 AC3_sudoku.py or python3 sudoku_backtracking.py

This folder contains two files.
Sudoku_backtracking.py only does backtracking to solve the two sudoku grids in a bruteforce way.
This was implemented as a way to better understand how to solve sudoku using backtracking. 
AC3_sudoku.py uses the AC3 algorithm along with maintaining arc consistency, and then doing backtracking
to solve the remaining cells when the domains have been reduced. 

Sources:
http://aima.cs.berkeley.edu/python/csp.html
https://norvig.com/sudoku.html