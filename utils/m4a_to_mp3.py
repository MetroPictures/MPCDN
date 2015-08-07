import os, re
from sys import argv, exit
from fabric.api import settings, local

def m4a_to_mp3(folder):
	os.chdir(folder)

	for _, _, files in os.walk(os.getcwd()):
		files = [f for f in files if re.match(r'.*\.m4a$', f)]

		for m4a in files:
			print m4a

			with settings(warn_only=True):
				res = local("ffmpeg -i %s -acodec libmp3lame -ab 128k %s" % \
					(m4a, m4a.replace(".m4a", ".mp3")), capture=True)
				
				if res.succeeded:
					local("rm %s" % m4a)
					
		break

	return True

if __name__ == "__main__":
	print argv

	if len(argv) != 2:
		print "supply a folder?"
		exit(-1)

	exit(0 if m4a_to_mp3(argv[1]) else -1)