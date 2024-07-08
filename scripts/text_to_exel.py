import xlsxwriter
import time
workbook = xlsxwriter.Workbook(f'OPAL/OPAL({time.time()}).xlsx')
worksheet = workbook.add_worksheet("My sheet")
def main(text):
    ar = []
    ar2 = []
    ar3 = []
    ar4 = [['Locale','Core string','old loc string','new loc string','mock id']]
    n = []
    n2 = []
    count = 0

    ar.append('')
    for line in text.split('\n'):
        ar.append(line)
    for i in range(len(ar)):
        count += 1
        if count > 3 and count < 5:
            ar = [line.rstrip() for line in ar]
            ar2.append(f'{(ar[i-1])[7:]}\t{(ar[i])[12:]}\t{(ar[i+1])[14:]}\t{(ar[i+2])[14:]}\t')
            ar3.append(ar[i-1]+ar[i]+ar[i+1])
        if count == 7:
            count = 0
    for i in ar2:
        if i not in n:
            n.append(i)

    for i in ar3:
        if i not in n2:
            n2.append(i)
    for i in range(len(n2)):
        ar2=[]
        for x in range(len(ar)):
            count += 1
            if count > 3 and count < 5 and n2[i] == ar[x-1]+ar[x]+ar[x+1]:
                ar2.append((ar[x+3])[7:])
            if count == 7:
                count = 0
        c = n[i]+', '.join(ar2)
        d = c.split('\t')
        ar4.append(d)
    row = 0
    col = 0
    for column1, column2,column3,column4,column5 in (ar4):
        worksheet.write(row, col, column1)
        worksheet.write(row, col + 1, column2)
        worksheet.write(row, col + 2, column3)
        worksheet.write(row, col + 3, column4)
        worksheet.write(row, col + 4, column5)
        row += 1
    workbook.close()
    return True