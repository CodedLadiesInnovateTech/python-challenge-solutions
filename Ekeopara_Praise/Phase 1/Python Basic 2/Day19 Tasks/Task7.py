'''7. Write a Python program to find the type of the progression (arithmetic progression/geometric progression)
and the next successive member of a given three successive members of a sequence.
According to Wikipedia, an arithmetic progression (AP) is a sequence of numbers such that 
the difference of any two successive members of the sequence is a constant. For instance,
the sequence 3, 5, 7, 9, 11, 13, . . . is an arithmetic progression with common difference 2.
For this problem, we will limit ourselves to arithmetic progression whose common difference is a non-zero integer.
On the other hand, a geometric progression (GP) is a sequence of numbers where each term after the first is 
found by multiplying the previous one by a fixed non-zero number called the common ratio. For example, 
the sequence 2, 6, 18, 54, . . . is a geometric progression with common 
ratio 3. For this problem, we will limit ourselves to geometric progression whose common ratio is a non-zero integer.'''

def ap_gp_sequence(arr):
  if arr[0]==arr[1]==arr[2]==0:
    return "Wrong Numbers"
  else:
    if arr[1]-arr[0]==arr[2]-arr[1]:
      n=2*arr[2]-arr[1]
      return "AP sequence, "+'Next number of the sequence: '+str(n)
    else:
      n=arr[2]**2/arr[1]
      return "GP sequence, " + 'Next number of the sequence:  '+str(n)

print(ap_gp_sequence([1,2,3]))
print(ap_gp_sequence([2,6,18]))
print(ap_gp_sequence([0,0,0]))