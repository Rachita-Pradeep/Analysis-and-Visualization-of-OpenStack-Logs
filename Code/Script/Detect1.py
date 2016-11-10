import sys
# from nltk.corpus import wordnet
import re

def get_phases(file,phases):
	f = open(file)
	components = f.readlines()
	for comp in components:
		phases[comp.strip().split("/")[-1]] = False
	return phases

def getDetails(file,err,dictionary,key):
	dictionary[key] = {}
	newlist = []
	dictionary[key]["file"] = file
	dictionary[key]["location"] = err.split()[0]
	word_list = err.split()
	for word in word_list:
		if re.match("^[A-Za-z0-9_-]*$", word):
			word.replace("\"",'')
			newlist.append(word)
	dictionary[key]["message"] = " ".join(newlist)
	

def compare(phases,logFile,out):
	f = open(logFile)
	err_out = open("error.txt","w")
	details = {}
	contents = f.readlines()
	count = 1
	for line in contents:
		#print line;
		if line.split(",")[4] == "ERROR":
			#print "error";
			getDetails(line.split(",")[1].split("/")[-1],line.split(",")[5].strip(),details,"error_"+str(count))
			phases[line.split(",")[1].split("/")[-1]]=True
			count += 1;
	for k in phases.keys():
		out.write(k+","+str(phases[k])+"\n")
	print details
	# err_out.write(str(details))
	
	for key in details.keys():
		for innerkey in details[key].keys():
			err_out.write(key+":"+innerkey+"="+details[key][innerkey]+"\n")
	return phases




if __name__ == "__main__":
	phases = {}
	get_phases("/home/ubuntu/Logs/Logs/create.txt",phases)
	get_phases("/home/ubuntu/Logs/Logs/delete.txt",phases)
	out = open("dict.txt","w")
	if len(sys.argv) ==2 :
		out.write(str(len(compare(phases, sys.argv[1],out))))
		out.write("\n");


