Project Euler Solutions in Python
==================================

Every once in a while, I need to solve a problem for the fun of it.  Project Euler has a bunch of problems that are fun, challenging, and don't requre external libraries to solve.  It's just you and your noggin'.  This repo contains a bunch of my solutions.

Running
-------
First, clone the repository by using `git clone --recursive` to make sure the submodules are also cloned.  Second, install the dependencies in `requirements.txt`.

You can call:

* `python3 cli.py run_all` to run all problems
* `python3 cli.py run_one X` where `X` is a problem number that you want to see solved.

How
---
PocketEuler contains an answer file where each answer has been hashed to prevent you from just taking all of the solutions and running to the Project Euler website to claim credit for solving them.  My project checks out PocketEuler as a git submodule and uses it's answer files to check my work.

Each solution function is wrapped with a `Problem` decorator.  This decorator builds a map of (solution number, solution function) pairs.  The CLI program uses this map to trigger each function and to get an answer.  It then SHA1's the answer and compares it to the answer file in PocketEuler.

Why
---
Because brain teasers are fun!  It also gives me something to discuss with employers during interviews.  Not all of these answers are super-optimized or the most "canonically" correct.  Rather, they're the first solution that I came up with.  This can sometimes be a good place for discussion when others are judging my code.