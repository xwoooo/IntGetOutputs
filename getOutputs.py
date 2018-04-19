import os
import subprocess as sp
import shutil



apk_path="C:\IntGet\Apks"
output_path="C:\IntGet\outputs"
output_name="IntGet_output.txt"

files=[]
for root, dirs, fs in os.walk(apk_path):  
        files=fs

for file in files:
	sp.call("java -jar apktool.jar d "+apk_path+'\\'+file)
	if os.path.exists(file[:-4]+"\original"):
		shutil.rmtree(file[:-4]+"\original")
	if os.path.exists("input"):
		shutil.rmtree("input")
		os.system("mkdir input")
	shutil.move(file[:-4],"C:\IntGet\input")
	os.system("C:\IntGet\IntGet.exe")
	os.system("ren "+output_name+" "+file[:-4]+".txt")
	shutil.move(file[:-4]+".txt","C:\IntGet\outputs")







# file="a742fc9b8c2495e5a584e475f5d59509.apk"

# sp.call("java -jar apktool.jar d "+apk_path+'\\'+file)
# if os.path.exists(file[:-4]+"\original"):
# 	shutil.rmtree(file[:-4]+"\original")
# if os.path.exists(file[:-4]+"input"):
# 	shutil.rmtree("input")
# 	os.system("mkdir input")
# shutil.move(file[:-4],"C:\IntGet\input")
# os.system("C:\IntGet\IntGet.exe")
# os.system("ren "+output_name+" "+file[:-4]+".txt")
# shutil.move(file[:-4]+".txt","C:\IntGet\outputs")