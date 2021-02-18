

**Bit Manipulation**


& 	Bitwise AND               x & y       10011100
                                        & 00110100
                                        = 00010100

| 	Bitwise OR  	          x | y       10011100
                                        | 00110100
                                        = 10111100

~ 	Bitwise NOT 	          ~x        ~ 11001011
                                        = 00110100

^ 	Bitwise XOR 	          x ^ y       10011100
                                        ^ 00110100
                                        = 10101000

'>>	Bitwise right shift 	  x>>       >> 1001110
                                        =   100111

<< 	Bitwise left shift 	    x<<         << 10011101
                                        =  00111010
 

**01 insert_number.py**

    You are given two 32-bit numbers, N and M, and two bit positions, i and j.
    Write a method to insert M into N such that M starts at bit j and end at bit i.
    You can assume that the bits j through i have enaigh space to fit all of M.
    That is, if M=10011, you can assume that there are at least 5 bits between j and i.
    You would not, for example, have j=3 and i=2, because M could not fully fit between bit 3 and bit 2.

    EXAMPLE
    Input: N = 10000000000, M = 10011, i = 2, j = 6
    Output: N = 10001001100


**02 float_as_binary.py**

    Given a real number between 0 and 1 (e.g. 0.72) that is passed in as a double, print the binary representation.
    If the number cannot be represented accurately in binary with at most 32 characters, print "ERROR".


**03 same_one_bits.py**

    Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation.


**04**

    Explain what the following code does: ((n & (n-1)) == 0)


**05 bits_to_convert.py**

    Write the function to determine the number of bits required to convert integer A to integer B.
    EXAMPLE
    Input: 31, 14
    Output: 2


**06 .py**

    Write a program to swap odd and even bits in an integer with as few instruction as possible
    (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swaped, and so on).


**07 .py**

    An array A contains all the integers from 0 to n, except for one number which is missing.
    In this problem, we cannot access an entire integer in A with a single operation .
    The elements in A are represented in binary, and the only operation we can use  to access them is
    " fetch the jth bit of A[i]", which takes constant time.
    Write code to find the missing integer. Can you do it in O(n) time?


**08 .py**

    A monochrom screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte.
    The screen has width w, where w is divisible by 8 (that is, no byte will be split across rows).
    The height of screen, of course, can be derived from the length of the array and the width.
    Implement a function drawHorizontalLine(byte[] screen, int width, int x1, int x2, int y) 
    which draws a horisontal line from (x1, y) to (x2, y).
