import os
import sys
from os.path import abspath, basename, isdir, isfile

def tree(directory, padding = {}, indent = 0):
	root = abspath(directory)
	files = []
	dirs = []

	def get_branch(is_last):
		return '%c-- ' % "|'"[ is_last and 1 or 0 ]

	def get_padding():
		return ''.join([ padding.get(level, '') for level in xrange(indent) ])

	def update_padding():
		return dict([ (idx, pad.replace("'", ' ').replace('--', '  ')) for idx, pad in padding.iteritems() ])

	# find list of files and directores inside of the root
	for name in os.listdir(root):
		path = '%s%s%s' % (root, os.sep, name)
		if isfile(path): files.append(path) 
		if isdir(path): dirs.append(path)

	dir_count = len(dirs)
	files_count = len(files)

	# print current root
	print ('%s%s') % (get_padding(), basename(root))

	# print files from a current root directory
	if files_count > 0:
		padding = update_padding()
		indent = indent + 1

		for idx, entry in enumerate(files, 1):
			padding[indent - 1] = get_branch(idx == files_count and dir_count == 0)
			print ('%s%s') % (get_padding(), basename(entry))

		indent = indent - 1

	# recursively print directories
	if dir_count > 0:
		padding = update_padding()
		indent = indent + 1

		for idx, entry in enumerate(dirs, 1):
			padding[indent - 1] = get_branch(idx == dir_count)
			tree(entry, padding, indent)

def main():
	directory = len(sys.argv) == 1 and os.getcwd() or sys.argv[1]
	tree(directory)

if __name__ == '__main__':
	main()
