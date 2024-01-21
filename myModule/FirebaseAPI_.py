import firebase_admin
from firebase_admin import db, credentials, storage
from cv2 import imencode, imdecode, IMREAD_COLOR, imshow, waitKey
import requests
import numpy as np
import datetime
# from datetime.datetime import now


cred = credentials.Certificate("sources\\firebase_SDK_install.json")
firebase_admin.initialize_app(cred, {
   'databaseURL': 'https://attendencechecking-df1dd-default-rtdb.firebaseio.com/',
   'storageBucket': 'attendencechecking-df1dd.appspot.com'
})

# Database Path
studentInfo_db_path = '''Information/'''
# faceEncode_db_path = '''Face Encoding/'''
StudImg_db_path = "Student Image/"

# Get a reference to the default storage bucket
bucket = storage.bucket()

# Reference to a specific location in the database
# data_ref_faceEncode = db.reference(faceEncode_db_path)



def post_student_image(id, frame):
   image_path = StudImg_db_path + ("%s.jpg" %id)
   blob = bucket.blob(image_path)
   _, image_data = imencode('.jpg', frame)
   blob.upload_from_string(image_data.tobytes(), content_type='image/jpeg')

def get_student_image(id):
   image_path = StudImg_db_path + ("%s.jpg" %id)
   blob = bucket.blob(image_path)
   download_url = blob.generate_signed_url(version="v2",
      expiration=datetime.timedelta(days=365),
      method="GET")
   response = requests.get(download_url)
   student_image = np.frombuffer(response.content, dtype=np.uint8)
   student_image = imdecode(student_image, IMREAD_COLOR)
   return student_image

def post_studentInformation(id, info ):
   data_ref = db.reference( studentInfo_db_path + id )
   for key in info.keys():
      data_ref.child(key).set( info[key] )

# post_studentInformation("1234567890", {
#    "Name" : "HTHH",
#    "DOB" : "2/8/2005",
#    "faceEncode" : np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).tolist()
# })

# post_studentInformation("9876543210", {
#    "Name" : "TNMA",
#    "DOB" : "26/3/2005",
#    "faceEncode" : np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).tolist()
# })

def get_idList():
   data_ref = db.reference( studentInfo_db_path)
   data_snapshot = data_ref.get()
   if data_snapshot is None:
      return []
   return list( data_snapshot.keys() )

def get_FaceEncodingList():
   data_ref = db.reference( studentInfo_db_path)
   data_snapshot = data_ref.get()
   if data_snapshot is None:
      return []
   return [ np.array(data_snapshot[id]["faceEncode"]) for id in data_snapshot.keys()]

def get_studentInformation(id):
   data_ref = db.reference( studentInfo_db_path + id)
   data_snapshot = data_ref.get()
   return data_snapshot

# data_ref = db.reference( studentInfo_db_path)
# data_snapshot = data_ref.get()
# print(list(data_snapshot.keys()))

def get_checkin_list(db_path):
   data_ref = db.reference( db_path )
   data_snapshot = data_ref.get()
   if data_snapshot is None:
      return []
   return list( data_snapshot.keys() )

def post_checkin_id(db_path, id):
   current_time = datetime.datetime.now()
   time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
   data_ref = db.reference( db_path )
   data_ref.child(id).set(time_string)
   
