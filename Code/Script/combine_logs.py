import csv

f1 = open("/home/ubuntu/Logs/Logs/logs_1.log","rb")
f2 = open("/home/ubuntu/Logs/Logs/logs_2.log","rb")
#f3 = open("/home/ubuntu/Logs/Logs/logs_3.log","rb")
f = open("/home/ubuntu/Logs/Logs/logs_tmp.csv","wb")
w = csv.writer(f, delimiter = ',')
for line in f1.readlines():
	data = line.split()
	try:
		time_temp = data.pop(3)
		data[2] = data[2] + " " + time_temp
		data[5] = ' '.join(data[5:])
		data[5] = data[5].replace(',',';')
		data = data[0:6]
	except IndexError:
		pass
	w.writerow(data)
for line in f2.readlines():
	data = line.split()
	try:
		time_temp = data.pop(3)
		data[2] = data[2] + " " + time_temp
		data[5] = ' '.join(data[5:])
		data[5] = data[5].replace(',',';')
		data = data[0:6]
	except IndexError:
		pass
	w.writerow(data)
#for line in f3.readlines():
#	data = line.split()
#	try:
#		time_temp = data.pop(3)
#		data[2] = data[2] + " " + time_temp
#		data[5] = ' '.join(data[5:])
#		data[5] = data[5].replace(',',';')
#		data = data[0:6]
#	except IndexError:
#		pass
#	w.writerow(data)
f1.close()
f2.close()
#f3.close()
f.close()

# remove empty last line
fi = open("/home/ubuntu/Logs/Logs/logs_tmp.csv","r")
fo = open("/home/ubuntu/Logs/Logs/logs.csv","w")
fo.write(fi.readline().rstrip())
while(1):
	line = fi.readline().rstrip()
	if (line == "" ):
		break
	fo.write("\n" + line)
fi.close()
fo.close()