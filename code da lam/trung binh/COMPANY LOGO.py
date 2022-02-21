A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

 would have it's logo with the letters .

Input Format

A single line of input containing the string .

Constraints

 has at least  distinct characters
Output Format

Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input 0

aabbbccde
Sample Output 0

b 3
a 2
c 2
Explanation 0


Here, b occurs  times. It is printed first.
Both a and c occur  times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.

Note: The string  has at least  distinct characters.







#bai giai



#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    


    
    #them va thong ke so lan xuat hien cua tu 
    def ham_thong_ke_cac_chu(tu):
        for chu_cai in tu:
            if chu_cai not in thong_ke_chu_cai:
                thong_ke_chu_cai[chu_cai]=1
            else:
                thong_ke_chu_cai[chu_cai]=thong_ke_chu_cai[chu_cai]+1
            
    tu=sorted(input())
    thong_ke_chu_cai={}                  
    dem=0
    chu_top=""
    so_lan_xuat_hien_top=0
    ham_thong_ke_cac_chu(tu)  
    xap_sep_chu_cai=sorted(thong_ke_chu_cai, key=thong_ke_chu_cai.get,reverse=True)
    
    for chu_cai in xap_sep_chu_cai:  
        print(chu_cai,thong_ke_chu_cai.get(chu_cai))
            
        dem+=1
        if dem==3:
            break
        