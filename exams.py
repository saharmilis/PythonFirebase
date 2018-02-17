import chooseFile
import firebase
import time

directoryName = "Exams";
filesType = "pdf"
runOverExams = False;
FIREBASE_DIRECTORY = "exams";


def uploadDirectory():

    print "\n";


    filesNamesArray = chooseFile.getAllFilesType(directoryName,filesType);

    for fileName in filesNamesArray:
        # try:
        print "FILE >>> " + str(fileName);

        # getting course number from file name
        courseNumber = fileName.split('-', 1)[0].replace("course", "");
        examName = str(fileName).replace(".pdf","");

        isFileExists = firebase.getData(FIREBASE_DIRECTORY + "/" + courseNumber,str(examName)).val()

        if isFileExists is not None :
            print "duplication";
            if not runOverExams:
                # deleting the file
                chooseFile.deleteFile(directoryName, fileName);
                continue;

        # adding file from local to firebase storage
        fileDownloadUrl = firebase.addFile(directoryName,FIREBASE_DIRECTORY,fileName);

        # prepering data as dictionary for firebase real time DB
        # course20304-year2014-semester3-moed1
        info = examName.split('-');
        courseId    = info[0].replace("course", "");
        year        = info[1].replace("year", "");
        semester    = info[2].replace("semester", "");
        moed        = info[3].replace("moed", "");
        url         = str(fileDownloadUrl);


        data = {
            str(examName) : {
                "courseId" : courseId,
                "year" : year,
                "semester" : semester,
                "moed" : moed,
                "url" : url
        }};

        print "DATA >> " + str(data);

        # adding the name and URL to the firebase DB
        firebase.addData(FIREBASE_DIRECTORY+"/"+str(courseNumber),data);

        # deleting the file
        chooseFile.deleteFile(directoryName,fileName);

        print "done\n"



        # except:
        #     print "\n\n ERROR with file "+ str(fileName) +" \n\n";

    print "\n";
    print "finish uploading directory : " + str(directoryName) + "\n";
    print "\n";
