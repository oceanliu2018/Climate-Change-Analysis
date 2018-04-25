#!/cygdrive/c/Python34/python
#oliu1:20150406:project.py

"""This script will read the file data.txt which includes the global temperature anomolies from 1800. The script will compute the average anomoly for each year into a list of values. Then it will create two dictionaries with the years as keys, one with the average anomoly as a value and one using average temperature as the value. Finally, the two dictionaries will be written into a file out.txt"""

a=open("data.txt")
datalist=a.readlines()
annualdata=[]
for i in range(1,len(datalist)):
	value=0
	for j in range(1,12):
		value=value+float((datalist[i].split()[j]))
	averagevalue=value/12
	annualdata.append(round(averagevalue,3))
anomolies_dictionary={}
for i in range (1,len(datalist)):
	anomolies_dictionary.update({int(datalist[i].split()[0]):annualdata[i-1]})
temperature_dictionary={}
for i in range(1,len(datalist)):
	temperature_dictionary.update({int(datalist[i].split()[0]):14.0+annualdata[i-1]/100})
with open("out.txt","w") as textfile:
	textfile.write(str(anomolies_dictionary))
	textfile.write("\n")
	textfile.write(str(temperature_dictionary))


"""This script will now also vonbert the dictionaries into lists and write it into a file new_out.dat so that the data is easier to umport into MATLAB"""
a=anomolies_dictionary.keys()
b=anomolies_dictionary.values()
year_list=[]
for i in a:
	year_list.append(i)
anomolies_list=[]
for i in b:
	anomolies_list.append(i)
c=temperature_dictionary.values()
temp_list=[]
for i in c:
	temp_list.append(i)
data=[year_list,anomolies_list]
'''with open('new_out.txt', 'w') as f:
    for row in zip(*data):
        f.write('\t'.join(row)+'\n')'''
 

totaldata = '\n'.join('\t'.join(map(str,row)) for row in zip(year_list,anomolies_list,temp_list))
with open('new_out.txt','w') as textfile:
	textfile.write(totaldata)
