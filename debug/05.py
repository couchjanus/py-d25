def valid(candidate):
    if candidate <= 1:
        return False

    lower = candidate - 1
    # Add  breakpoint(), after the while loop:
    while lower > 1:
        breakpoint()
        if candidate / lower == candidate // lower:
            return False
        lower -= 1

    return True


assert not valid(1)
assert valid(3)
assert not valid(15)
assert not valid(18)
assert not valid(50)
assert valid(53)

# Execute the code again, and see that it stops at the breakpoint, 
# entering into the interactive Pdb mode:

# $ python debug.py
#  /home/janus/work/py-g25/debug/05.py(9)valid()
# -> if candidate / lower == candidate // lower:
# (Pdb)

# Check the value of the candidate and the two operations. 
# This line is checking whether the dividing of candidate 
# by lower is an integer (the float and integer division is the same):
# (Pdb) candidate
# 3
# (Pdb) candidate / lower
# 1.5
# (Pdb) candidate // lower
# 1
# Continue to the next instruction with n. 
# See that it ends the while loop and returns True:
# (Pdb) n
# > ...debug.py(10)valid()
# -> lower -= 1
# (Pdb) n
# > ...debug.py(6)valid()
# -> while lower > 1:
# (Pdb) n
# > ...debug.py(12)valid()
# -> return True
# (Pdb) n
# --Return--
# > ...debug.py(12)valid()->True
# -> return True
# Continue the execution until another breakpoint is found with c. 
# Note that this is the next call to valid(), which has 15 as an input:
# (Pdb) c
# > ...debug.py(8)valid()
# -> if candidate / lower == candidate // lower:
# (Pdb) candidate
# 15
# (Pdb) lower
# 14
# Continue running and inspecting the numbers until 
# what the valid function is doing makes sense. 

# When you’re done, exit with q. 
# This stops the execution:
# (Pdb) q
# ...
# bdb.BdbQuit