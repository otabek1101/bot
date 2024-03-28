import re


def tekshirish(num):
    pattern = re.compile('^[\+]?[(]?[9-9]{2}[)]?[-\s\.]?[8-8]{1}[-\s\.]?[0-9]{4}[-\s\.]?[0-9]{5,5}$')
    return pattern.match(num)

num = input("q= ")

if tekshirish(num):
    print("True")
else:
    print("dvv")