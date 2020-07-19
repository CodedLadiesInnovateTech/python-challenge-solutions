'''6. Write a Python program to calculate body mass index.'''

def M_I(wt, h):
    m_i = wt/h**2
    return "The body Mass Index is: ", m_i
print(M_I(70, 5))

