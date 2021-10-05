import random
import sys

# This function computes the fibonacci sequence.
#
# Also see: https://en.wikipedia.org/wiki/Fibonacci_number
def fib(n):
    fib_seq = [0,1]
    if n <= 0:
        print("Incorrect input")
    else:
        for i in range(2, n):
            fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq


# This function computes the triangular numbers sequence.
# A triangular number correspond to the number of dots that would appear in an equilateral triangle
# when using a basic triangular pattern to build the triangle.
#
# Also see: https://www.101computing.net/triangular-numbers/#:~:text=The%20first%2010%20numbers%20of,36%2C%2045%2C%2055%2C%20%E2%80%A6&text=So%20using%20an%20iterative%20approach,View%20on%20trinket.io
def tri(n):
    number =  1
    tri_seq = [1]
    for i in range(1, n):
        number = number + n
        tri_seq.append(number)
    return tri_seq

# This function takes two sequences, sorts them and then merges them into one sequence.
def merge(first_seq, sec_seq):
    return sorted(first_seq + sec_seq)

# This function validates whether the sequence is a sorted list.
def validate(seq):
    for i in range(len(seq)):
        if seq[i] < seq[i-1]:
            sys.exit('** ERROR: Invalid sequence (order not ascending)! **')

# This function takes two sequences and checks whether they are similar.
def similar(first_seq, sec_seq):
    for i in range(len(first_seq)):
        if first_seq[i-1] != sec_seq[i-1] or sec_seq[i-1] != first_seq[i-1]:
            sys.exit('** ERROR: Sequences are not similar! **')

# Converts a sequence of strings into a sequence of integers.
# This function returns a new list.
def convert(seq):
    result = []
    for i in range(len(seq)):
        result.append(int(seq[i]))
    return result

#
# Test scenarios
# Fibonacci tests
fib_10 = fib(10)
similar(fib_10, [0,1,1,2,3,5,8,13,21,34])
similar([0,1,1,2,3,5,8,13,21,34], fib_10)
print('PASSED: Fibonacci 10 tests')

fib_2 = fib(2)
similar(fib_2, [0,1])
similar([0,1], fib_2)
print('PASSED: Fibonacci 2 tests')

fib_1 = fib(1)
similar(fib_1, [0])
similar([0], fib_1)
print('PASSED: Fibonacci 1 tests')

fib_0 = fib(0)
similar(fib_0, [])
similar([], fib_0)
print('PASSED: Fibonacci 0 tests')

# Triangular numbers tests
tri_10 = tri(10)
similar(tri_10, [1,3,6,10,15,21,28,36,45,55])
similar([1,3,6,10,15,21,28,36,45,55], tri_10)
print('PASSED: Triangular 10 tests')

tri_1 = tri(1)
similar(tri_1, [1])
similar([1], tri_1)
print('PASSED: Triangular 1 tests')

tri_0 = tri(0)
similar(tri_0, [])
similar([], tri_0)
print('PASSED: Triangular 0 tests')

tri_minus_1 = tri(-1)
similar(tri_minus_1, [])
similar([], tri_minus_1)
print('PASSED: Triangular -1 tests')

# Merge tests
fib_sequence = fib(50)
validate(fib_sequence)
print('PASSED: Fibonacci 50 validation')

tri_sequence = tri(100)
validate(tri_sequence)
print('PASSED: Triangular 100 validation')

tf_merge = merge(tri_sequence, fib_sequence)
validate(tf_merge)
print('PASSED: Triangular-Fibonacci merge validation')

random.shuffle(fib_sequence)
random.shuffle(tri_sequence)

tf_shuffle_merge = merge(tri_sequence, fib_sequence)
validate(tf_shuffle_merge)
print('PASSED: Triangular-Fibonacci shuffle merge validation')

# More merge tests
rand_sequence = ["140892","596854","888599","841236","800876","66173","267460","123647","519502","797927","471326","495186","683245","398056","827037","220154","98419","511555","29725","936711","876364","408745","453790","636945","799309","804424","2209","729634","467023","279268","756590","840776","239875","619870","991189","107193","945216","332850","32076","23407","26682","681099","567713","9653","984770","924041","399722","719831","227121","442622","761112","30452","553260","232461","800799","459159","984788","519897","579716","244407","362494","242082","7O9728","229409","797912","481930","998501","303859","971513","22534","436397","878265","960779","583485","966985","673495","104858","194937","659925","758791","901720","310788","126763","779246","348857","939079","756532","745739","525127","981930","442612","532381","870356","954399","702867","199072","318105","297963","616123","925347"]

tr_merge = merge(tri_sequence, rand_sequence)
validate(tr_merge)
print('PASSED: Triangular-Random merge validation')


print('--------[ END ]----------')
