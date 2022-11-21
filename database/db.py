import firebase_admin
from firebase_admin import db
from firebase_admin import storage
import certifi
import os

dBRef = False
storageRef = False
#To achieve DRY (Dont Repeat Yourself), let's create a singlton function to hold the connection
def getDbRef():
    global dBRef,storageRef
    if not dBRef:
        os.environ['SSL_CERT_FILE'] = certifi.where()
        cred_obj = firebase_admin.credentials.Certificate('comp7510-svc.json')
        firebase_admin.initialize_app(cred_obj, {
            'databaseURL': 'https://comp7510-svc-default-rtdb.firebaseio.com/',
            'storageBucket':'comp7510-svc.appspot.com'
        })
        storageRef = storage.bucket()
        dBRef = db.reference('/')
    return dBRef

def getStorageRef():
    global dbRef,storageRef
    if not storageRef:
        os.environ['SSL_CERT_FILE'] = certifi.where()
        cred_obj = firebase_admin.credentials.Certificate('comp7510-svc.json')
        firebase_admin.initialize_app(cred_obj, {
            'databaseURL': 'https://comp7510-svc-default-rtdb.firebaseio.com/',
            'storageBucket':'comp7510-svc.appspot.com'
        })
        storageRef = storage.bucket()
        dbRef = db.reference('/')
    return storageRef
