import sys
import threading
sys.path.append("C:\\Dev\\ATIN\\Training\\PyQT5\\myModule")

from face_recognize import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel

# Import the generated module
from addNewStudent import Ui_AddNewStudent 
from attendanceCheck import Ui_AttendanceCheck
from HomePage import Ui_HomePage
from lessonInfo import Ui_LessonInfo

import FirebaseAPI_

from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QImage, QPixmap
import cv2
import numpy as np
import time 



class MyApp(QMainWindow):
   def __init__(self):
      super().__init__()
      self.currentFrame = None
      self.captured = False
      self.checked_list = []
      self.attendence_db_path = ""
      self.load_checked_list()
      self.timer = QTimer(self)
      self.facerec_timer = QTimer(self)
      self.setup_notif_box()
      self.studentImageDict = {}
      

      self.home_page_window()
      # self.addNewStudentWindow()
      # self.attendanceCheckWindow()

   def home_page_window(self):
      self.ui = Ui_HomePage()
      self.ui.setupUi(self)
      self.timer.stop()
      self.facerec_timer.stop()
      self.ui.Button_register.clicked.connect(self.addNewStudentWindow)
      self.ui.Button_Rollcall.clicked.connect(self.lessonInfoWindow)

   def setup_notif_box(self):

      self.labelnotif = QLabel('This is a QLabel', self)
      self.labelnotif.setGeometry(310, 0, 650, 30)
      self.labelnotif.hide()

      self.notiftimer = QTimer(self)
      self.notiftimer.timeout.connect(self.labelnotif.hide)
      self.notiftimer.timeout.connect(self.notiftimer.stop)

   
   def display_notice(self, text, sec = 0.5):
      self.labelnotif.setText(text)
      self.labelnotif.show()
      self.notiftimer.start( (int)(sec * 1000))

   def load_checked_list(self):
      # with open(self.attendence_db_path, "rb") as db:
      #    while True:
      #       try:
      #          load_data = pickle.load(db)
      #       except EOFError:
      #          break
   
      #       self.checked_list.append(load_data)
      self.checked_list = FirebaseAPI_.get_checkin_list(self.attendence_db_path)

   def lessonInfoWindow(self):
      self.ui = Ui_LessonInfo()
      self.ui.setupUi(self)
      self.ui.ButtonIntoClass.clicked.connect(self.IntoClassClicked)

   def IntoClassClicked(self):
      classID = self.ui.InputClassID.text()
      lesson = self.ui.InputLesson.text()
      if classID == "" or lesson == "" :
         self.display_notice("Please fill lesson information")
      else:
         self.attendence_db_path = classID + ("/Lesson%s"%lesson)
         self.attendanceCheckWindow()

   def attendanceCheckWindow(self):
      self.ui = Ui_AttendanceCheck()
      self.ui.setupUi(self)
      self.ui.button_rerecognize.hide()
      self.ui.button_checkin.hide()
      self.reconized = False
      self.current_student_id = None
      self.milisecond_per_update_facerec = 1000
      self.ui.button_rerecognize.clicked.connect(self.rerecognize)
      self.ui.button_checkin.clicked.connect(self.checkin)
      self.ui.commandLinkButton_backhp.clicked.connect(self.home_page_window)

      #2 thread: 1 for display and 1 for encoding   
      #ACW = Attendance check window
      self.ACW_app_displaying()
      self.ACW_face_encoding()
      # self.face_reconizing_thread = ProcessThread(self.ACW_face_encoding_thread )
      
      # self.app_displaying_thread.update_signal.connect(self)
      # self.face_reconizing_thread.join()
      # self.face_reconizing_thread.start()


   def rerecognize(self):
      self.facerec_timer.start(self.milisecond_per_update_facerec)
      self.ACW_reset()

   def checkin(self):
      self.facerec_timer.start(self.milisecond_per_update_facerec)
      # with open(self.attendence_db_path, "a+b") as db:
      #    pickle.dump(self.current_student_id, db)
      FirebaseAPI_.post_checkin_id(self.attendence_db_path, self.current_student_id)
      self.ACW_reset()
      self.checked_list.append(self.current_student_id)

   def ACW_reset(self):
      self.ui.labelDobDisplay.clear()
      self.ui.labelNamdisplay.clear()
      self.ui.imageDisplay.clear()
      self.ui.button_rerecognize.hide()
      self.ui.button_checkin.hide()

   def ACW_app_displaying(self):
      self.display_webcam()

   def ACW_face_encoding(self):
      self.facerec_timer.timeout.connect(self.face_checking_and_displaying)
      self.facerec_timer.start(self.milisecond_per_update_facerec)
   


   def face_checking_and_displaying(self):

      start_time = time.time()

      face_lct = face_locations(self.currentFrame)

      end_time = time.time()

      print(end_time - start_time)
      face_encoding_list = face_encodings(self.currentFrame, face_lct, model="large")

      if len(face_encoding_list) == 0:
         return
      
      self.facerec_timer.stop()
      is_stop = True

      for face_encoding in face_encoding_list:
         
         ret, (id, name_, dob_) = face_checking( face_encoding )
         print(name_, dob_, id)
         if not ret:
            continue
         
         is_stop = False
         if id not in self.studentImageDict.keys():
            self.studentImageDict[id] = FirebaseAPI_.get_student_image(id)
         student_image = self.studentImageDict[id]
         height, width, channel = student_image.shape
         bytes_per_line = 3 * width
         q_image = QImage(student_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
         pixmap = QPixmap.fromImage(q_image)
         self.ui.imageDisplay.setPixmap(pixmap)
         self.ui.labelNamdisplay.setText(name_)
         self.ui.labelNamdisplay.setText(dob_)
         if id in self.checked_list:
            self.facerec_timer.start(self.milisecond_per_update_facerec)
            self.display_notice("Checked Before!")
            self.ACW_reset()
         else:
            self.ui.button_rerecognize.show()
            self.ui.button_checkin.show()
            self.current_student_id = id

      if is_stop:
         self.facerec_timer.start(self.milisecond_per_update_facerec)

   

   def addNewStudentWindow(self):
      self.ui = Ui_AddNewStudent()
      self.ui.setupUi(self)
      self.ui.button_save.clicked.connect(self.submit)
      self.ui.button_takeagain.clicked.connect(self.takePhotoClick)
      self.ui.commandLinkButton_backhp.clicked.connect(self.home_page_window)
      self.display_webcam()

   

   def submit(self):
      if not self.captured:
         self.display_notice("Image haven't captured yet")         
      else:
         name = self.ui.inputName.text()
         dob = self.ui.inputDOB.text()
         print (name)
         print (dob)
         if name == "" or dob == "":
            self.display_notice("Please fill the information box")
         else:

            face_lct = face_locations(self.currentFrame)
            #Face Encoding
            face_encoding_list = face_encodings(self.currentFrame, face_lct, model="large")
            if (len(face_encoding_list) == 0):
               self.display_notice("No Face Detected!", 1)
            elif len(face_encoding_list) > 1:
               self.display_notice("Too Many Faces Detected!", 1)
            else:
               for face_encoding in face_encoding_list:
                  send_back = Add_new_student(face_encoding, self.currentFrame, name, dob)
                  self.display_notice(send_back, 1)
                  self.ui.inputName.setText("")
                  self.ui.inputDOB.setText("")

                  

         self.captured = False
         self.ui.button_takeagain.setText("Take Photo")
         self.ui.inputName.setText("")
         self.ui.inputDOB.setText("")

         

   def display_webcam(self):
      self.cam = cv2.VideoCapture(0)

      milisecond_per_update = 50
      self.timer.timeout.connect(self.update_webcam)
      self.timer.start(milisecond_per_update)      

   def takePhotoClick(self):
      if self.captured:
         #Resume display
         self.captured = False
         self.ui.button_takeagain.setText("Take Photo")
      else:
         #Pause display
         self.captured = True
         self.ui.button_takeagain.setText("Take Again")  

   def update_webcam(self):

      ret, self.currentFrame = self.cam.read()

      if ret and not self.captured:
         #convert to QImage
         self.currentFrame = cv2.cvtColor(self.currentFrame, cv2.COLOR_BGR2RGB) 
         height, width, channel = self.currentFrame.shape
         bytes_per_line = 3 * width
         q_image = QImage(self.currentFrame.data, width, height, bytes_per_line, QImage.Format_RGB888)

         # Set Camera Display
         pixmap = QPixmap.fromImage(q_image)
         self.ui.Cameradisplay.setPixmap(pixmap)

   def closeEvent(self, event):
      # Release the webcam when the application is closed
      if self.cam.isOpened():
         self.cam.release()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyApp()
   window.show()
   sys.exit(app.exec_())