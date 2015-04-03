import datetime, os, tempfile, subprocess
import config

def newmemory(args):
	print "hey new memory!"
	
	memoryname = None
	memorybody = None
	with tempfile.NamedTemporaryFile(suffix=".tmp") as tmp:
		tmp.write("")
		tmp.flush()
		subprocess.call([config.EDITOR, tmp.name])

		now = datetime.datetime.now()
		year = now.year;
		month = now.month;
		day = now.day;
		datePath = os.path.expanduser(os.path.join(config.prefix, "memories", str(year), str(month), str(day)))
		try:
			os.makedirs(datePath)
		except OSError:
			# Path already exists, which is not a problem
			pass

		ftype = ".txt"

		while True:
			try:
				memoryname = raw_input("What would you like to call this memory? ")
				if os.path.isfile(os.path.join(datePath, memoryname + ftype)):
					print "A memory with this name already exists. Please name it something else. "
				else:
					break
			except:
				print "Something went wrong, let's that try again. "
		
		with open(os.path.join(datePath, memoryname + ftype), 'w') as memout:
			memout.write("---\ntitle: " + memoryname + "\n")
			memout.write("date: %04d-%02d-%02d\n" % (year, month, day))
			memout.write("datetime: " + now.isoformat() + "\n---\n")
			with open(tmp.name, 'r') as f:
				memout.write(f.read())

