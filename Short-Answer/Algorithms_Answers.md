#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n), a increases proportionally to n but in that process, no additional processes are required.


b) O(n^2), the loop is n-sized and the while loop will only run a handful of times but its execution depends on n


c) O(n), the function returns itself only n times and the inside of the function is simple

## Exercise II


Because all floors below f are "safe" for egg-tossing, the best solution is to start from the bottom and iterate upwards until one egg is broken. The point at which the egg breaks is floor f.

take a number of eggs, eggs and number of floors n:
    for floor in n:
        if throw(egg) < egg:
          f = floor
          return f
    return f

This solution has a runttime complexity of O(n)
