# Modify the process function to fit your needs
def process(row):
    result = ''
    n = 0
    save = ''
    for t in row:
        save += t
        if t == '/':
            if len(save) == 2:
                save = '0'+save
            if n == 0:
                save = save[:-1]
                month = save
            elif n == 1:
                save = save[:-1]
                day = save
            save = ''
            n += 1
        if t == ' ':
            year = '20' + save
            save = ''
    time = row[-5:-1]+row[-1]
    result += day + '-' + month + '-' + year + time
    return result

print(process('12/10/18 10:45'))