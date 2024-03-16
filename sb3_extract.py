import sb3
import zipfile as z
import sys, os, json

with z.ZipFile(sys.argv[1], "r") as zr:
	zr.extract("project.json")

pj = json.load(open("project.json", "r"))
list = []
for targ in pj["targets"]:
	for aaa in targ["sounds"]:
		list.append(aaa)

s, a = sb3.open_sb3(sys.argv[1])

for aa in a:
	print("Processing "+aa.name+"...")
	if(aa.name[0:len(aa.name)-4] != ".mp3"):
		print("File is not an MP3")
		pass
	else:
		print("Writing file")
	realName = ""
	for x in list:
		#print(x["assetId"]+".wav")
		if(x["assetId"] == aa.name[0:len(aa.name)-4]):
			realName = x["name"]+"."+x["dataFormat"]
	#print("RN: "+realName)
	if realName == "":
		print()
		pass
	else:

		f = open(realName, "wb")
		nb = f.write(aa.read())
		f.close()
		print("\tWrote "+str(nb)+" bytes")
	"""
	if aa.name[-4:len(aa.name)] == ".mp33333":
		os.system("ffmpeg -i "+aa.name+" "+aa.name[0:-4]+".wav")
		os.remove(aa.name)
		print("FFMPEGed it: "+aa.name[0:-4]+".wav")
	"""
print("Done")
os.remove("project.json")