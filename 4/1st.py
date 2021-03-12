import re

f = open('C:\\Users\\nguye\OneDrive\\Documents\\advent-of-code\\4\\input.txt', 'r')
content = f.read()

content = content.split("\n\n")

counter = 0

def list_to_dict(rlist):
    return dict(map(lambda s : s.split(':'), rlist))

timer = 0

for i in content:
    print(timer)
    timer += 1
    if "byr" not in i:
        pass
    elif "iyr" not in i:
        pass
    elif "eyr" not in i:
        pass
    elif "hgt" not in i:
        pass
    elif "hcl" not in i:
        pass
    elif "ecl" not in i:
        pass
    elif "pid" not in i:
        pass
    else:
        i = i.split()
        i = list_to_dict(i)
        try:
            if int(i["byr"]) < 1920 or int(i["byr"]) > 2002:
                pass
            elif int(i["iyr"]) < 2010 or int(i["iyr"]) > 2020:
                pass
            elif int(i["eyr"]) < 2020 or int(i["eyr"]) > 2030:
                pass
            elif i["hgt"][-2:] == "cm":
                if int(i["hgt"][:3]) < 150 or int(i["hgt"][:3]) > 193:
                    pass
            elif i["hgt"][-2:] == "in":
                if int(i["hgt"][:3]) < 59 or int(i["hgt"][:3]) > 76:
                    pass
            elif bool(re.match(r"#[0-9a-f]{5}", i["hcl"])) == False:
                pass
            elif i["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                pass
            elif bool(re.match(r"[0-9]\d{9}", i["pid"])) == False:
                pass
            else:
                counter += 1
        except:
            pass
    
print(counter)

f.close()