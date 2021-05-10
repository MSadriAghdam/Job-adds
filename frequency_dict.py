#to calcualte frequency of
def other_freq(col):
    emp = {}
    for item in col:
        if item in emp:
            emp[item] +=1
        else:
            emp[item] = 1
    return emp