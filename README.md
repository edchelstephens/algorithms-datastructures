# Algorithms and Datastructures Learning Repository

## Software Versions:

[Python 3.10](https://docs.python.org/3/)

# Resources in Computing

## Operations

    - The number of times we need to perform some operations

## Memory

    - How much memory is consumed by the algorithms

## Others

    - Network transfer, compressions ratios, disk usage

# Measuring Algorithm Complexities

## Big-O notation O()

Big-O notation represents the upper limit of an algorithm's cost and is associated with a big O parentheses `O(n)` in a formula that uses `n` as the size of the input.

When we're using the Big-O notation, what we're doing is classifying how a function behaves as the size of the input grows or as `n` gets larger. We're trying to estimate how the algorithm scales.

Another term for this is **Asymptotic Analysis**.

### Asymptote

    - The asymptote of a curve is a line where the distance between the curve and the line approach zero as they tend towards infinity.

## Asymptotic Analysis

    - The measurement of how the inputs of an algorithm affect the behavior as the inputs approach some limit.

## Complexity Analysis

    - When we're talking about complexity what we're actually talking about is asymptotic analysis, the performance of an algorithm as an input approaches to an upper limit.

# Big-O Classifications

# 0(1)

    - The cost of algorithm is unchanged by the input size
    - fix cost algorithm

# O(n)

    - A function whose cost scales linearly with the size of the input
    - single loops

# O(log(n))

    - A function whose cost scales logarithmically with the input size
    - Less than linear complexity
    - As the input grows, the cost of the algorithm does not increase at the same rate
    - O(log n) algorithms work by dividing a large problem into smaller and smaller chunks
    - divide and conquer


# O(n^2)
    - A function that exhibits quadratic growth relative to input size
    - doubly nested for loops