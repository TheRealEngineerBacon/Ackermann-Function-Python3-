GO AND LOOK AT THE ACKERMANN WIKI FIRST.
Do some research into the Ackermann function and recursion before running this script. Recursion can lead to stack overflows if the "matrix" becomes too deep which can lead to stability issues.
I recommend m and n values not exceeding m=3, n=5 for low end systems. An adjustment to the python recursion limit, which is the first prompt of the script, can be adjusted to compute further values of n. As an example, I had to set the recursion limit to 5000 in order to iterate to values of m=3 and n=8. 
It pays to understand the relevance of the ackermann function before running the script as it's a cool case of recursion in python programming.
