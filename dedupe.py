from os import listdir, system
import hashlib, os
import glob

class File:
	def __init__(self, path, hash):
		self.path = path
		self.hash = hash

def hash(file):
	BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
	with open(file, 'rb') as f:
		while True:
			data = f.read(BUF_SIZE)
			if not data:
				break
			return hashlib.sha1(data).hexdigest()

dir1 = "/share/User"
dir2 = "/mnt/E/S_Documents/Games/Emulators/Dolphin Emulator/User"

a = set()
b = set()
c = set()

for file in glob.glob(dir1 + "/**/*.*", recursive = True):
	path = file
	hs = hash(path)
	a.add( File(path, hs) )
	
for file in glob.glob(dir2 + "/**/*.*", recursive = True):
	path = file
	hs = hash(path)
	b.add( File(path, hs) )


for f in a:
	for p in b:
		if f.hash == p.hash: c.add(p)

for f in c:
	print(f.path)

prompt = input("Delete these items? Y / N ")
if prompt == "y":
	for f in c:
		os.remove(f.path)
elif prompt == "n":
	exit()