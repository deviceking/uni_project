file_path = r"C:\Users\chuaz\Downloads\sensor-data-1k.txt" 
element = [0][0]
float_list = []
line_count = 0

with open(file_path,"r") as file:
    for line in file :
        parts = line.split()

        floats = [float(parts[2]), float(parts[3]), float(parts[4]), float(parts[5])]
        float_list.append(floats)
        line_count +=1

    for add in float_list:
        for i in range (len(add)):
            add[i] +=1

total_sum = sum(sum(sublist)for sublist in float_list)

divide = total_sum/ (line_count*4)
rounded = round(divide,2)
print(f"{divide:.2f}")
#print(rounded)