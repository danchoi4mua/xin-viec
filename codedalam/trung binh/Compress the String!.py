"""
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .


Sample Input

1222311
Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)
Explanation

First, the character  occurs only once. It is replaced by . Then the character  occurs three times, and it is replaced by  and so on.

Also, note the single space within each compression and between the compressions.
"""


# bai giai cua ban than


tu = input()
chu_thuong=""
chu_hoa=""
so_le=""
so_chan=""
for chu in tu : 
    if chu.islower():
        chu_thuong+=chu
    elif chu.isupper():
        chu_hoa+=chu
    elif chu.isdigit():
        if int(chu)%2!=0:
            so_le+=chu
        else:
            so_chan+=chu
print("".join(sorted(chu_thuong)+sorted(chu_hoa)+sorted(so_le)+sorted(so_chan)))      




#giai cua mn 



from itertools import groupby

#user input

myinput = input()

#creating empty list to store output

thong_ke = []

for so,so_loc_trong_input in groupby(myinput):
    
    
    thong_ke.append((len(list(so_loc_trong_input)),int(so)))

print(*thong_ke)
