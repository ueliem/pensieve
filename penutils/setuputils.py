import os

import config

def setup(args):
	# Create the root of the pensieve, and the memories directory
	try:
		os.makedirs(os.path.expanduser(os.path.join(config.prefix, "memories")))
	except OSError:
		pass
	try:
		os.makedirs(os.path.expanduser(os.path.join(config.prefix, "index")))
	except OSError:
		pass

