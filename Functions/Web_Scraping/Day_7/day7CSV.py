import csv
#open the file
data=open('eg.csv',encoding='utf-8')
#csv.reader
csv_data=csv.reader(data)
#reformat it into a python obj list of lists  
datalines=list(csv_data )
# print(datalines[10][5])
# print(len(datalines))
# for line in datalines[2:4]:
#     print(line)
#PRINTING ALL DAYS
# all_days=[]
# for line in datalines[1:]:
#     all_days.append(line[1])
# print(all_days )

#COMBINING 2 
# com=[]
# for line in datalines[1:]:
#     com.append(line[1]+"  "+line[2])
# print(com)

# file=open('to_save_file.csv',mode='w',newline='')
# csv_writer=csv.writer(file,delimiter=',')
# print(csv_writer.writerow(['a','b','c']))
# csv_writer.writerows([['1','2','3'],['4','5','6'],['7','8','9']])
# print(file.close())

f=open('to_save_file1.csv',mode='a',newline='')
csv_writer=csv.writer(f)
print(csv_writer.writerow(['1','2','3']))
