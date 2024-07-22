import sb3
import zipfile as z
import sys, os, json, shutil

if(not os.path.exists("out")):
	os.mkdir("out")
else:
	shutil.rmtree("out")
	os.mkdir("out")

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
	realName = ""
	for x in list:
		#print(x["assetId"]+".wav")
		if(x["assetId"] == aa.name[0:len(aa.name)-4]):
			realName = x["name"]+"."+x["dataFormat"]
	#print("RN: "+realName)
	if realName == "":
		pass
	else:
		f = open("out/"+aa.name, "wb")
		nb = f.write(aa.read())
		f.close()
		print("\tWrote "+str(nb)+" bytes")
		os.system("ffmpeg -i \"out/"+aa.name+"\" \"out/"+realName.split(".")[0]+".mp3\"")
		os.remove("out/"+aa.name)
		print("FFMPEGed it: out/"+realName.split(".")[0]+".mp3")
	
print("Done")
os.remove("project.json")