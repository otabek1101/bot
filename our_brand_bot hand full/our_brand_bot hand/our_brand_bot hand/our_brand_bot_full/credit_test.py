import re


def tekshirish_humo(num):
    humo = re.compile('(^9860[0-9]{12}(?:[0-9]{3})?$)')
    return humo.match(num)

def tekshirish_uzcard(num):
    uzcard = re.compile('(^8600[0-9]{12}(?:[0-9]{3})?$)')
    return uzcard.match(num)
def tekshirish_visa(num):
    visa= re.compile('(^4[0-9]{12}(?:[0-9]{3})?$)|(^(?:5[1-5][0-9]{2}|222[1-9]|22[3-9][0-9]|2[3-6][0-9]{2}|27[01][0-9]|2720)[0-9]{12}$)|(3[47][0-9]{13})|(^3(?:0[0-5]|[68][0-9])[0-9]{11}$)|(^6(?:011|5[0-9]{2})[0-9]{12}$)|(^(?:2131|1800|35\d{3})\d{11}$)')
    return visa.match(num)
num = input("q= ")

if tekshirish_humo(num) or tekshirish_uzcard(num) or tekshirish_visa(num):
    print("True")
else:
    print("Bunday karta mavjud emas")