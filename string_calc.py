import re
def add(string_calc):
    number_ls = []
    num = 0
    negatives_num = []

    if string_calc is (""):
        return 0
    if string_calc == ("1\n"):
        return "Not ok"

    else:#for each_num in string_calc.split(","):
        for each_num in re.split(r'[`\=~!@#$%^&*()_+\[\]{};\'\\:"|<,./<>?\n]',string_calc):
            try:
                if int(each_num) > 1000:
                    each_num = 0
                num += int(each_num)
                number_ls.append(int(each_num))
            except:
                continue
        
        for number in number_ls:
            if number < 0:
                negatives_num.append(number)

        if len(negatives_num) == 0:
            return num

        else:
            error ='ERROR: negatives not allowed'
            for number in negatives_num:
                error += " "
                error += str(number)
            raise ValueError(error)