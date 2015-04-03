import os

import config

def getstatus(args):
	numberOfMemories = getNumberOfMemories()
	if numberOfMemories == 1:
		print str(numberOfMemories) + " memory has been recorded. "
	else:
		print str(numberOfMemories) + " memories have been recorded. "


def getNumberOfMemories():
	count = 0
	for (dirpath, dirnames, filenames) in os.walk(os.path.expanduser(os.path.join(config.prefix, "memories"))):
		notHiddenFiles = [item for item in filenames if item[0] != "."]
		count += len(notHiddenFiles)
	return count

