#!/usr/local/bin/python
import numpy as np
import matplotlib.pyplot as plt

# data to plot
n_groups = 5
# error_logs = (2996 ,891, 99948, 0, 0)
# success_logs = (3037, 967, 26352, 72370, 1212)
error_logs = []
success_logs = []
f_clean = open("noerror_count.txt","r")
data_clean = f_clean.readlines()
for line in data_clean:
	success_logs.append(int(line.split(":")[1].strip()))
success_logs.append(0)
success_logs.append(0)

f_error = open("statistics.txt","r")
data_error = f_error.readlines()
for line in data_error:
	error_logs.append(int(line.split(":")[1].strip()))

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 0.8
 
rects1 = plt.bar(index, error_logs, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Error Logs')
 
rects2 = plt.bar(index + bar_width, success_logs, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Success Logs')
 
plt.xlabel('Type of Logs')
plt.ylabel('Statistics')
plt.title('Comparison of Error and Successful logs')
plt.xticks(index + bar_width, ('INFO', 'AUDIT', 'WARNINGS', 'ERROR','TRACE'))
plt.legend()
 
plt.tight_layout()
plt.show()
