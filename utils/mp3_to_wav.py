import os, re
from sys import argv, exit
from fabric.api import settings, local

def mp3_to_wav(folder):
	os.chdir(folder)

	for _, _, files in os.walk(os.getcwd()):
		files = [f for f in files if re.match(r'.*\.mp3$', f)]

		for mp3 in files:
			print mp3

			with settings(warn_only=True):
				res = local("ffmpeg -i %s -acodec pcm_s16le -ar 48000 %s" % \
					(mp3, mp3.replace(".mp3", ".wav")), capture=True)
				
				if res.succeeded:
					local("rm %s" % mp3)
					
		break

	return True

if __name__ == "__main__":
	print argv

	if len(argv) != 2:
		print "supply a folder?"
		exit(-1)

	exit(0 if mp3_to_wav(argv[1]) else -1)