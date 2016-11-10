import os
import datetime as dt
import re

def search_file(pattern,f_tmp,offset=0):
	f_tmp.seek(offset)
	line = f_tmp.readline()
	while line:
		m = re.search(pattern, line)
		if m:
			search_offset = f_tmp.tell() - len(line)
			return search_offset 
		line = f_tmp.readline()

def main():
	now=dt.datetime.now()
	ago=now-dt.timedelta(minutes=15)
	f = open("/home/ubuntu/Logs/Logs/logs_1.log", "w")
	server = "10.10.1.97"
	openstack_dir = ['/var/log/nova', '/var/log/glance', '/var/log/cinder', '/var/log/keystone', '/var/log/apache2/']
	for opstk_dir in openstack_dir:
		for root,dirs,files in os.walk(opstk_dir): 
			for fname in files:
				path=os.path.join(root,fname)
				append_path = server+" "+path
				st=os.stat(path)    
				mtime=dt.datetime.fromtimestamp(st.st_mtime)
				if mtime>ago:
					f_tmp = open(path,"r",encoding="utf8",errors='ignore')
					ago_tmp = ago
					while(ago_tmp<now):
						# Do the re match
						a = str(ago_tmp).split(" ")
						a1 = a[0]
						a2_tmp = a[1]
						a2 = a2_tmp.split(":")
						off = search_file(a1, f_tmp, offset=0)
						if(off != None):
							off = search_file(a1+" "+a2[0], f_tmp, offset=off)
							if(off != None):
								off = search_file(a[0]+" "+a2[0]+":"+a2[1], f_tmp, offset=off)
								if(off != None):
									f_tmp.seek(off)
									break
						ago_tmp = ago_tmp + dt.timedelta(minutes=1)
					# writting the entire file
					prev_line = line = f_tmp.readline()
					while(line!=""):
						if(re.match(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3}', line)):
							f.write(append_path + " " + prev_line)
							prev_line = line
						else:
							prev_line = prev_line.strip("\n") + ";" + line
						line = f_tmp.readline()
					f_tmp.close()
	# read from syslog
	path='/var/log/syslog'
	append_path = server+" "+path
	st=os.stat(path)
	mtime=dt.datetime.fromtimestamp(st.st_mtime)
	if mtime>ago:
		f_tmp = open(path,"r",encoding="utf8",errors='ignore')
		ago_tmp = ago
		while(ago_tmp<now):
			# Do the re match
			a = str(ago_tmp).split(" ")
			a1 = a[0]
			a2_tmp = a[1]
			a2 = a2_tmp.split(":")
			off = search_file(a1, f_tmp, offset=0)
			if(off != None):
				off = search_file(a1+" "+a2[0], f_tmp, offset=off)
				if(off != None):
					off = search_file(a[0]+" "+a2[0]+":"+a2[1], f_tmp, offset=off)
					if(off != None):
						f_tmp.seek(off)
						break
			ago_tmp = ago_tmp + dt.timedelta(minutes=1)
		# writting the entire file
		line = f_tmp.readline()
		while(line!=""):
			f.write(append_path + " " + line)
			line = f_tmp.readline()
		f_tmp.close()				
	f.close()

if __name__ == '__main__':
	main()
