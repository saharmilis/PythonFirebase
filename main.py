

print "Start";



if __name__ == "__main__":


    import exams
    import time

    print "uploading directory : " + str(exams.directoryName) + "\n";

    print "to cancel push CTRL+C+C";

    print "lunch in 10 seconds"
    for t in range(10,1,-1):
        print t
        time.sleep(1)


    exams.uploadDirectory()

    # import firebase
    # firebase.downloadFile("exams/course10007-year2014-semester2-moed1.pdf");







print "finish";


input("CLICK TO EXIT")

