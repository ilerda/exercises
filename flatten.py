
# Given a nested list with arbitrary level of nesting, write a function, flatten to flatten it.

# sample input:
# x = [[4,5],[[1,2,3]],6]

# flatten(x) --> [4,5,1,2,3,6]

# Use: https://www.online-python.com or any IDE you have.

def flatten(a):
    result = []
    result = flatten_helper(a, result)
    return result
    
def flatten_helper(a, res):
    for el in a:
        if type(el) == int:
            res.append(el)
        else:
            flatten_helper(el, res)
    return res

x = [[4,5],[[1,2,3]],6]
print(flatten(x))
