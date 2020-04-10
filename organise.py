import shutil
import os

path = input(
    "Enter path to folder you want to organise (default : current folder) :")
path = path or "."


filelist = os.listdir(path)

types = ["video", "audio", "executable", "docs", "image", "compressed",
         "iso", "torrent", "code", "disk", "data", "fonts", "web", "downloading"]
extensions = {"video": tuple(["mp4", "avi", "3gp", "webm", "flv", "mkv", "wmv", "mpg", "mpeg", "mov", "h264", "vob", "rm"]),
              "audio": tuple(["mp3", "wav", "ogg", "aac"]),
              "executable": tuple(["exe", "sh", "msi", "bat", "deb", "apk", "jar"]),
              "docs": tuple(["pdf", "ppt", "pptx", "doc", "docx", "txt", "md", "epub", "rtf", "tex"]),
              "data": tuple(["csv", "xls", "xlsx", "dat", "db", "log", "sql", "xml", "tar", "mdv", "sav"]),
              "image": tuple(["jpg", "png", "jpeg", "gif", "tiff", "psd", "ai", "ico", "bmp", "ps", "svg", "tif"]),
              "compressed": tuple(["zip", "rar", "rpm", "tar.gz", "pkg", "z"]), "iso": tuple(["iso"]),
              "torrent": tuple(["torrent"]),
              "disk": tuple(["iso", "vcd", "dmg", "bin", "toast"]),
              "code": tuple(["py", "cpp", "c", "java", "cs", "class", "h", "pl", "swift", "vb", "vbs"]),
              "fonts": tuple(["fnt", "fon", "otf", "ttf", "woff"]),
              "web": tuple(["html", "htm", "css", "scss", "js", "jsx", "php", "jsp", "asp", "aspx", "xhtml", "rss", "cer", "cfm"]),
              "downloading": tuple(["part", "download"])
              }

for file_ in filelist:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]
    if ext == "" or (name == "organise" and ext == "py"):
        continue
    for t in types:
        if ext in extensions[t]:
            if os.path.exists(os.path.join(path, t)):
                shutil.move(os.path.join(path, file_), os.path.join(path, t))
            else:
                os.makedirs(os.path.join(path, t))
                shutil.move(os.path.join(path, file_), os.path.join(path, t))
            break


# others
filelist = os.listdir(path)
for file_ in filelist:
    name, ext = os.path.splitext(file_)
    ext = ext[1:]
    if ext == "" or (name == "organise" and ext == "py"):
        continue
    if os.path.exists(os.path.join(path, "others")):
        shutil.move(os.path.join(path, file_), os.path.join(path, "others"))
    else:
        os.makedirs(os.path.join(path, "others"))
        shutil.move(os.path.join(path, file_), os.path.join(path, "others"))
