# -*- coding: utf-8 -*-
from collections import OrderedDict

def roman(num):

    roman = OrderedDict()
    roman[1000000] = "M̄"
    roman[900000] = "C̄M̄"
    roman[500000] = "D̄"
    roman[400000] = "C̄D̄"
    roman[100000] = "C̄"
    roman[90000] = "X̄C̄"
    roman[50000] = "Ḹ"
    roman[40000] = "X̄Ḹ"
    roman[10000] = "X̄"
    roman[9000] = "MX̄"
    roman[5000] = "V̄"
    roman[4000] = "MV̄"
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])

num = input("Give a number: ")
if num > 0 and num <= 1000000:
    print "The latin number is:" , roman(num)
else:
    print "Out of index, please try again"