import shutil
import os

path = input("Enter path to folder you want to organise:")

filelist = os.listdir(path)

types = ["video","audio","executable","docs","image","compressed","iso","torrent"]
extensions = {"video":tuple(["mp4","avi","3gp","webm","flv"]),
                "audio":tuple(["mp3","wav","ogg","aac"]),
                "executable":tuple(["exe","sh","msi","bat","deb"]),
                "docs":tuple(["pdf","ppt","pptx","doc","docx","csv","xls","xlsx","txt"]),
                "image":tuple(["jpg","png","jpeg","gif","tiff","psd","ai"]),
                "compressed":tuple(["zip","rar","rpm","tar.gz"]),"iso":tuple(["iso"])
                ,"torrent":tuple(["torrent"])}

for file_ in filelist:
    name,ext = os.path.splitext(file_)
    ext = ext[1:]
    if ext =="":
        continue
    for t in types:
        if ext in extensions[t]:
            if os.path.exists(path+"\\"+t):
                shutil.move(path+'\\'+file_,path+"\\"+t) 
            else:
                os.makedirs(path+"\\"+t)
                shutil.move(path+'\\'+file_,path+"\\"+t)  
            break
   
filelist = os.listdir(path)                        

for file_ in filelist:
    name,ext = os.path.splitext(file_)
    ext = ext[1:]
    if ext =="":
        continue
    if os.path.exists(path+"\\others"):
        shutil.move(path+'\\'+file_,path+"\\others") 
    else:
        os.makedirs(path+"\\others")
        shutil.move(path+'\\'+file_,path+"\\others")             