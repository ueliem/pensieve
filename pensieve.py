#!/usr/bin/python

import argparse

import config
import penutils

def main():
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(title='subcommands', description='valid subcommands')

	parser_setup = subparsers.add_parser('setup', help="Setup help")
	parser_setup.set_defaults(func=penutils.setuputils.setup)

	parser_new = subparsers.add_parser('new', help="new help")
	parser_new.set_defaults(func=penutils.newutils.newmemory)

	parser_import = subparsers.add_parser('import', help="import help")
	parser_import.add_argument('files', nargs='+', help="import files help")
	parser_import.set_defaults(func=penutils.importutils.importmemory)

	parser_status = subparsers.add_parser('status', help="status help")
	parser_status.set_defaults(func=penutils.statusutils.getstatus)

	#parser_setup = subparsers.add_parser('search', help="search help")
	#parser_setup.set_defaults(func=penutils.setuputils.setup)

	#parser_setup = subparsers.add_parser('index', help="index help")
	#parser_setup.set_defaults(func=penutils.setuputils.setup)



	args = parser.parse_args()
	args.func(args)

if __name__ == "__main__":
	main()

