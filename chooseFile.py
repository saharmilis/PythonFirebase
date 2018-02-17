import os


def isFileExists(fileName):
    print os.path.exists(fileName);

def getAllFilesType(dir,fileType):
    scriptPath = os.path.dirname(os.path.realpath(__file__));
    arr = [];
    for file in os.listdir(scriptPath + "/exams"):
        if file.endswith("."+fileType):
             arr.append(file);
    return arr;

def deleteFile(dir,fileName):
    os.remove(dir+"/"+fileName);


