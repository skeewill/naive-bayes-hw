# bayes-dice

### Introduction

A box contains a 4-sided die, a 6-sided die, an 8-sided die, a 12-sided die, and a 20-sided die. A die is selected at random, and the rest are destroyed.

We would like to determine which die I have selected, given only information of what I roll.

What is the prior associated with choosing any one die?

What is the likelihood function? You should assume that the die are all fair.

Say I roll an 8. After one bayesian update, what are the new priors?

### Coding

You are to create a class called `BayesDice`. Implement as many instance methods as you need. The purpose of this class is to run a simulation. The simulation will choose a die, and then roll it repeatedly. Every time you roll the chosen die, you will update the priors. You should be able to figure out which die was chosen after a small number of rolls have occurred.

Here is a small sample of how you could execute your code.

```
bd = BayesDice()
bd.choose_die()
bd.roll_die()
bd.roll_die()
bd.roll_die()
```

### Layout

Put your code under the `src` directory. Also create a `test` directory to test out your code, to ensure it is working as expected. Use `pytest`.

### Pull Request

Fork and clone the repository. Use a `dev` branch. Send a pull request of your final code.
