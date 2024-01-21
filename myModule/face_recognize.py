from face_recognition import api
from face_recognition.api import face_locations, face_encodings, compare_faces, face_distance

import FirebaseAPI_
import cv2
import numpy as np
import time 
import pickle
import random

known_face = FirebaseAPI_.get_FaceEncodingList()
students_id = FirebaseAPI_.get_idList()

def face_checking( face_encoding ):
    #load face list
    # faceencode_db_path = '''Database_fake/face_encoding_db.pkl'''
    # studentInfo_db_path = '''Database_fake/information_db.pkl'''

    global known_face
    global students_id
    
    # with open(faceencode_db_path, "rb") as db:
    #     #face_dict = pickle.load(db)
    #     while True:
    #         try:
    #             load_data = pickle.load(db)
    #         except EOFError:
    #             break
            
    #         known_face.append(load_data["faceEncode"])
    #         students_id.append(load_data["ID"])

    ret = compare_faces( np.array(known_face), np.array(face_encoding), 0.5)
    print(ret)

    # Name_list = []
    # DOB_List = []

    # with open(studentInfo_db_path, "rb") as db:
    #     #face_dict = pickle.load(db)
    #     while True:
    #         try:
    #             load_data = pickle.load(db)
    #         except EOFError:
    #             break
            
    #         Name_list.append(load_data["Name"])
    #         DOB_List.append(load_data["DOB"])

    if len(ret) > 0:
        best_match = np.argmin( face_distance(known_face, face_encoding) )
        # print(best_match)
        if ret[best_match]:
            # return True, (students_id[best_match], Name_list[best_match], DOB_List[best_match])
            best_match_info = FirebaseAPI_.get_studentInformation(students_id[best_match])
            return True, (students_id[best_match], best_match_info["Name"], best_match_info["DOB"])
        
    return False, (-1, -1, -1)


def face_add( face_encoding, info_dict, frame ):
    ret, id = face_checking( face_encoding )
    if ret:
        return "Face included before!"
    
    # studentInfo_db_path = '''Database_fake/information_db.pkl'''
    # faceEncode_db_path = '''Database_fake/face_encoding_db.pkl'''
    # students_id = []
    # with open(faceEncode_db_path, "rb") as db:
    #     #face_dict = pickle.load(db)
    #     while True:
    #         try:
    #             load_data = pickle.load(db)
    #         except EOFError:
    #             break

    #         students_id.append(load_data["ID"])
    global known_face
    global students_id
    
    while True:
        id_list = random.sample( range(10), 10)
        id_list = [str(dig) for dig in id_list]
        ID = "".join(id_list)

        if ID not in students_id:
            break
    
    
    # filepath =  "Student Image//" + ID + ".jpg"
    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR) 
    # cv2.imwrite(filepath, frame)
    FirebaseAPI_.post_student_image(ID, frame)
    info_dict['faceEncode'] = face_encoding.tolist()
    known_face.append(info_dict['faceEncode'])

    # with open(studentInfo_db_path, "a+b") as db:
    #     pickle.dump(info_dict, db)
    # with open(faceEncode_db_path, "a+b") as db:
    #     pickle.dump({
    #         'ID': ID,
    #         'faceEncode': face_encoding
    #     }, db)
    FirebaseAPI_.post_studentInformation(ID, info_dict)
    students_id.append(ID)
    
    return "Face added"

def Add_new_student( face_encoding, frame, name, DOB ):   #will later take input form textbox
    
    return ( face_add(face_encoding, {
        "Name" : name,
        "DOB"  : DOB
    }, frame))
            

              

# if __name__ == "__main__":
#     Add_new_student("Do Tuan Nam", "14/06/2005")