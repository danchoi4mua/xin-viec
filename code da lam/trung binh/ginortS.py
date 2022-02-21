"""
You are given a string .
 contains alphanumeric characters only.
 Your task is to sort the string  in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.
Input Format

A single line of input contains the string .

Constraints

Output Format

Output the sorted string .

Sample Input

Sorting1234
Sample Output

ginortS1324

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



print(*sorted(input(), key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')

import string
print(*sorted(input(), key=(string.ascii_letters + '1357902468').index), sep='')  




print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')


