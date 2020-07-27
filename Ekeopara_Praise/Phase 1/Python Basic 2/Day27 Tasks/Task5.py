'''5. Write a Python program to check whether a given sequence is linear, quadratic or cubic.
Sequences are sets of numbers that are connected in some way.
Linear sequence:
A number pattern which increases or decreases by the same amount each time is called a linear sequence. The amount it increases or decreases by is known as the common difference.
Quadratic sequence:
In quadratic sequence, the difference between each term increases, or decreases, at a constant rate.
Cubic sequence:
Sequences where the 3rd difference are known as cubic sequence.
Sample Output:
Linear Sequence
Quadratic Sequence
Cubic Sequence
Linear Sequence'''

def Seq_Linear_Quadratic_Cubic(seq_nums):
  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  if len(set(seq_nums)) == 1: return "Linear Sequence"
  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  if len(set(seq_nums)) == 1: return "Quadratic Sequence"
  seq_nums = [seq_nums[x] - seq_nums[x-1] for x in range(1, len(seq_nums))]
  if len(set(seq_nums)) == 1: return "Cubic Sequence"
  
print(Seq_Linear_Quadratic_Cubic([0,2,4,6,8,10]))
print(Seq_Linear_Quadratic_Cubic([1,4,9,16,25]))
print(Seq_Linear_Quadratic_Cubic([0,12,10,0,-12,-20]))
print(Seq_Linear_Quadratic_Cubic([1,2,3,4,5]))

#Reference: w3resource