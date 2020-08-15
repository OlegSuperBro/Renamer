"""
Made by OlegSuperBro
Github https://github.com/OlegSuperBro
"""
import os,time

#answering what file need to copy
while True:	
	file_name=input(">Input name your file (with file extension): ")
	try:
		opening=open(file_name)
		break
	except:
		print("ERROR file "+file_name+" not found!")

while True:	
	file_name=input(">Input file name with names (with file extension): ")
	try:
		file=open(file_name)
		break
	except:
		print("ERROR file "+file_name+" not found!")

#preparing to start code
try:
	os.makedirs("renamed/")
except:
	pass
files=os.listdir("renamed/")
main_file=opening.read() #saves content for testing file
names=[]
name=" " #just for executing line 35

#adding names to list
while not name=="":
	name=file.readline()
	name=name.replace("\n" , "")
	names.append(name)

#creating files with main file content
for i in range(len(names)):
	create=open("renamed/" + names[i] + ".txt","w") #creating file
	create.write(main_file) #coping content main file in copied file
	print("Creating " + names[i] + " complete")
	create.close()

print("Do you want test files? y/n")

#testing files
while True:
	answer=input()
	if answer=="y":
		try:
			for i in range(len(files)):
				file_name="renamed/"+files[i]
				opening=open(file_name)
				test_source=opening.read()
				if main_file==test_source:
					print(file_name.replace("renamed/","")+" file is copied")
				else:
					print(file_name.replace("renamed/","")+" file is corrupted")
			print("Testing complete!")
			os.system("pause")
			break
		except:
			print("Error testing "+file_name)
	elif answer=="n":
		break
	else:
		print("Expecting y or n")