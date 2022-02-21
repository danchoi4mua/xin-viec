"""There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.

Hence, the total happiness is .

Language
Python 3

More
1234567891011121314
_ = input()
tap_so = input().split()

so_ta_thich = set(input().split())
so_ta_ghet = set(input().split())


p=0
for i in tap_so:
    if i in so_ta_thich:
        p+=1
    if i in so_ta_ghet:
        p-=1
print(p)
Line: 1 Col: 1

Submit Code

Run Code

Upload Code as File

Test against custom input
Congratulations
Share on FacebookShare on TwitterShare on LinkedIn
You solved this challenge. Would you like to challenge your friends?
Next Challenge
Earn a certificate in Python
Kudos on your progress! Take the HackerRank Skills Certification test and enrich your profile

Get Certified

Test case 0

Test case 1

Test case 2

Test case 3

Test case 4

Test case 5

Test case 6

Test case 7
Compiler Message
Success
Input (stdin)

Download
3 2
1 5 3
3 1
5 7
Expected Output

Download
1
Contest CalendarBlogScoring"""





#bai giai






_ = input()

tap_so = input().split()
so_ta_thich = set(input().split())
so_ta_ghet = set(input().split())


hanh_phuc=0
for i in tap_so:
    if i in so_ta_thich:
        hanh_phuc+=1
    if i in so_ta_ghet:
        hanh_phuc-=1
print(hanh_phuc)
