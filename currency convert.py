# 1 euro = 7.8942rmb

user_input =  input()

number = ""
currency = ""

for char in user_input:
    if char.isdigit():
        number += char
    elif char.isalpha():
        currency += char
    else :
        print("format error")
        break
        
number = float(number)

if currency == "EUR":
    number *= 7.8942
    print(f"{number:.2f}CNY")

elif currency == "RMB":
    number /= 7.8942
    print(f"{number:.2f}EURO")

else :
    print("error")