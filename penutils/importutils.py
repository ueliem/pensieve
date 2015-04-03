import datetime, os

import config

def importmemory(args):
	handledfiles = []
	for item in args.files:
		if os.path.isfile(item):
			if item in handledfiles:
				print "File " + item + " is duplicated in arguments. "
				continue
			else:
				createdDate = datetime.datetime.fromtimestamp(os.path.getctime(item))
				datePath = os.path.expanduser(
						os.path.join(
							config.prefix, 
							"memories", 
							str(createdDate.year), 
							str(createdDate.month), 
							str(createdDate.day)
						)
					)
				fileOutputPath = os.path.join(datePath, os.path.basename(item))
				try:
					os.makedirs(datePath)
				except OSError:
					# Path already exists, which is not a problem
					pass

				with open(item, 'r') as itemf:
					with open(fileOutputPath, 'w') as outf:
						outf.write("---\ntitle: " + os.path.splitext(os.path.basename(item))[0] + "\n")
						outf.write("date: %04d-%02d-%02d\n" % (createdDate.year, createdDate.month, createdDate.day))
						outf.write("datetime: " + createdDate.isoformat() + "\n---\n")
						outf.write(itemf.read())

