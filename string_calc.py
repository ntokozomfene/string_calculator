import re

def add(string_numbers):
    list_num = []
    num = []

    if len(string_numbers) == 0: return 0
    
    try:
        int(string_numbers[-1])
    except:
        return "Not ok"
       
    for letter in re.findall(r"-?\d+", string_numbers):
        try:
            if int(letter) > 1000:
                letter = 0
            if int(letter) < 0:
                num.append(letter)
            list_num.append(int(letter))
        except:
            continue
            
    if len(num) > 0:
        raise Exception('negatives not allowed: {}'.format(num))

    return sum(list_num)