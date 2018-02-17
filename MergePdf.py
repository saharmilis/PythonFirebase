from pprint import pprint

import pyrebase

config = {
    "apiKey": "AIzaSyAaztMn6ww7HI9jHtkZ6w4gKw9_I453h4g",
    "authDomain": "afekaunion.firebaseapp.com",
    "databaseURL": "https://afekaunion.firebaseio.com",
    "storageBucket": "afekaunion.appspot.com",
    "messagingSenderId": "349382480933"
  };

print("yoyo start")

firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()


# Log the user in
user = auth.sign_in_with_email_and_password("codethreo@gmail.com", "codethreo");

# Get a reference to the database service
db = firebase.database()
st = firebase.storage();

def getData(dir,dataKey):
    results = db.child(dir + "/" + dataKey).get(user['idToken'])
    return results;

def addData(dir,data):
    results = db.child(dir).update(data, user['idToken']);

def addFile(dirSource,dirStorage,fileName):
    results = st.child(dirStorage+"/"+fileName).put(dirSource+"/"+fileName,user['idToken']);
    return st.child(dirStorage+"/"+fileName).get_url(user['idToken']).split("&token=",1)[0];

def downloadFile(fileName):
    results = st.child(fileName).download("download.pdf")
    print results

print(db)
eee = db.child("exams").child("10006").get();
exams = eee.val();

print(exams["10006"])
print(exams[1])

# for e in ee :
#     print(e)

# for e in db.child("exams").get().each():
#     print(e.key())
#     # print(e.val())

# for e in db.child("exams").child("10006").get().each():
#     print(e.val()["url"])