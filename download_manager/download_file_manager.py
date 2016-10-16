import os,shutil

def make_directory(s):
	try:
		os.mkdir(s)
	except:
		print "already exist"

url="/home/user_name/Downloads"
os.chdir(url)

pdf=[]
zips=[]
image=[]
deb=[]
video=[]
text=[]
songs=[]
programs=[]
html=[]

make_directory("pdfs")
make_directory("zips")
make_directory("images")
make_directory("debian")
make_directory("video")
make_directory("text")
make_directory("songs")
make_directory("programs")
make_directory("html")

items=os.listdir(url)

for item in items:
	if(item.endswith(".pdf")):
		pdf.append(item)
	elif(item.endswith(".zip")):
		zips.append(item)
	elif(item.endswith(".jpg") or item.endswith(".jpeg") or item.endswith(".png") or item.endswith(".gif")):
		image.append(item)
	elif(item.endswith(".mkv") or item.endswith(".mp4")):
		video.append(item)
	elif(item.endswith(".deb")):
		deb.append(item)
	elif(item.endswith(".txt")):
		text.append(item)
	elif(item.endswith(".mp3")):
		songs.append(item)
	elif(item.endswith(".py") or item.endswith(".cpp") or item.endswith(".c") or item.endswith(".java") or item.endswith(".sh") or item.endswith(".js")):
		programs.append(item)
	elif(item.endswith(".html") or item.endswith(".css")):
		html.append(item)

for item in items:
	if(item.endswith(".pdf")):
		shutil.move(url+"/"+item,url+"/"+"pdfs")
	elif(item.endswith(".zip")):
		shutil.move(url+"/"+item,url+"/"+"zips")
	elif(item.endswith(".jpg") or item.endswith(".jpeg") or item.endswith(".png") or item.endswith(".gif")):
		shutil.move(url+"/"+item,url+"/"+"images")
	elif(item.endswith(".mkv") or item.endswith(".mp4")):
		shutil.move(url+"/"+item,url+"/"+"video")
	elif(item.endswith(".deb")):
		shutil.move(url+"/"+item,url+"/"+"debian")
	elif(item.endswith(".txt")):
		shutil.move(url+"/"+item,url+"/"+"text")
	elif(item.endswith(".mp3")):
		shutil.move(url+"/"+item,url+"/"+"songs")
	elif(item.endswith(".py") or item.endswith(".cpp") or item.endswith(".c") or item.endswith(".java") or item.endswith(".sh") or item.endswith(".js")):
		shutil.move(url+"/"+item,url+"/"+"programs")
	elif(item.endswith(".html") or item.endswith(".css")):
		shutil.move(url+"/"+item,url+"/"+"html")