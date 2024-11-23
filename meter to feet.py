# 1m = 3.2808ft

get_input = input()
m = "m"
ft = "ft"

number = ""
si_unit = ""

for char in get_input:
    if char.isdigit():
        number += char
    if char.isalpha():
        si_unit += char
    else :
        print("format error")
        exit()

number = float(number)

if si_unit == "m":
    output_ft = number * 3.2808
    print(f"{output_ft:.2f}ft")

elif si_unit == "ft":
    output_m = number /3.2808
    print(f"{output_m:.2f}m")

else :
    print("FORMAT ERROR")
