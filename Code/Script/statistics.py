import sys
import csv
import os

def count1(file,log_file):
	info_count = 0
	warning_count = 0
	audit_count = 0
	trace_count = 0
	error_count = 0
	f_csv = open(log_file, 'rb')
	reader = csv.reader(f_csv)
	for row in reader:
		if "INFO" in row:
			info_count += 1
		#print row
		#print "i",info_count
		elif "AUDIT" in row:
			audit_count += 1
		#print row
		#print "a",audit_count
		else:
			warning_count += 1
		#print row
		#print "w",warning_count
	print "i",info_count,"a",audit_count,"w",warning_count
	f = open("noerror_count.txt","w")
	file.write("clean;i:"+str(info_count)+"\nclean;a:"+str(audit_count)+"\nclean;w:"+str(warning_count)+"\nclean;t:"+str(trace_count)+"\nclean;e:"+str(error_count)+"\n")

def count2(file,log_file):
	info_count = 0
	warning_count = 0
	audit_count = 0
	trace_count = 0
	error_count = 0

	f_csv = open(log_file, 'rb')
	reader = csv.reader(f_csv)
	for row in reader:
		if "INFO" in row:
			info_count += 1
			#print row
			#print "i",info_count

		elif "AUDIT" in row:
			audit_count += 1
			#print row
			#print "a",audit_count

		elif "TRACE" in row:
			trace_count += 1
			#print row
			#print "a",audit_count

		elif "ERROR" in row:
			error_count += 1
			#print row
			#print "a",audit_count

		else:
			warning_count += 1
			#print row
			#print "w",warning_count

	print "i",info_count,"a",audit_count,"w",warning_count,"t",trace_count,"e",error_count
	file.write("error;i:"+str(info_count)+"\nerror;a:"+str(audit_count)+"\nerror;w:"+str(warning_count)+"\nerror;t:"+str(trace_count)+"\nerror;e:"+str(error_count)+"\n")


if __name__ == "__main__":
	f = open("statistics.txt","w")
	if len(sys.argv) == 3:
		count1(f,sys.argv[1])
		count2(f,sys.argv[2])
