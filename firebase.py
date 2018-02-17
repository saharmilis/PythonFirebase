import pyrebase

config = {
    "apiKey": "***",
    "authDomain": "***",
    "databaseURL": "***",
    "storageBucket": "***",
    "messagingSenderId": "***",
  };


firebase = pyrebase.initialize_app(config)

# Get a reference to the auth service
auth = firebase.auth()


# Log the user in
user = auth.sign_in_with_email_and_password("exampleo@gmail.com", "example");

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



'''
service firebase.storage {
  match /b/afekaunion.appspot.com/o {
    match /{allPaths=**} {
      allow read, write: if request.auth != null;
    }
  }
}
'''

