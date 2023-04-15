filename = "flower_info.txt"
data_file = open(filename, 'r', encoding='UTF8')
data = []
flag = 0
for line in data_file:
    linelist = line.strip().split('\t')
    data.append({
        'name' : linelist[0],
        'description' : linelist[3].replace('â€“', '-').replace("Ã—", '*'),
        'states' : linelist[2],
        'common_name' : linelist[1]
    })
    flag+= 1
    if flag > 3:
        break
for dict in data:
    print(f"{dict['name']} {dict['common_name']} {dict['states']} {dict['description']}")
