#!/usr/bin/python

import re
import os,sys
from git import Repo

cur = os.getcwd()
print cur

project_dir = os.path.join(cur, '../miconnect')
print project_dir


repo = Repo(project_dir)

diff = repo.git.diff('HEAD~1',repo.head).split("\n")
print diff
ret = {}


print ".................................."

file_name = ""
diff_lines = []
current_line = 0
for line in diff:
	print "...",line
	if line.startswith('diff --git'):
		print "1111111111111111"
		if file_name != "":
			ret[file_name] = diff_lines
		file_name = re.findall('b/(\S+)$', line)[0]
		print file_name
		diff_lines = []
		current_line = 0
	elif re.match('@@ -\d+,\d+ \+(\d+),\d+ @@', line):
		print "22222222222222222222222"
		match = re.match('@@ -\d+,\d+ \+(\d+),\d+ @@', line)
		print match
		current_line = int(match.group(1)) - 1
	elif line.startswith("-"):
		continue
	elif line.startswith("+") and not line.startswith('+++'):
		print "3333333333333333333333333333"
		current_line += 1
		diff_lines.append(current_line)
	else:
		current_line += 1
ret[file_name] = diff_lines


print ret
