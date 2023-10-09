from datetime import datetime
import cv2
import numpy as np
import face_recognition
import os
import time

class FaceRecognition():

    def __init__(self):
        self.path = "./Photos"
        self.images = []
        self.classNames = []
        self.myList = os.listdir(self.path)
        # print(myList)
        for cl in self.myList:
            curImg = cv2.imread(f"{self.path}/{cl}")
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])
        # print(classNames)

    def findEncodings(self):
        encodeList = []
        for img in self.images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encodeList.append(face_recognition.face_encodings(img)[0])
        return encodeList

    def markAttendance(self,name):
        with open("C:/Users/sidda/PycharmProjects/FacialAttendance/facialattendance/EmployeeApp/Attendance.csv", "r+") as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                dtString = now.strftime('%H:%M:%S')
                dtString2 = datetime.today().strftime('%Y-%m-%d')
                f.writelines(f"{name},{dtString},{dtString2}")

    
    # print("Encoding Complete")
    
    def RecognizeFace(self,img,encodeListKnown):

        debugInfo = {'outer':0, 'inner1':0, 'inner2':0}
        start = time.time()


        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            
            start = time.time()
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)
            end = time.time()
            debugInfo['inner1']= end-start


            if matches[matchIndex]:
                start = time.time()
                name = self.classNames[matchIndex]
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img,name, (x1+6, y2-6),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255),2)                
                self.markAttendance(name)
                end = time.time()
                debugInfo['inner2']= end-start

                return (img,debugInfo)
                
        end = time.time()
        debugInfo['outer']= end-start
        return (img,debugInfo)



# imgElon = face_recognition.load_image_file("ImagesBasic/Elon_Musk_1.jpg")
# imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)
#
# imgTest = face_recognition.load_image_file("ImagesBasic/Elon_Musk_test1.jpeg")
# imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)
#
# faceLoc = face_recognition.face_locations(imgElon)[0]
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon, (faceLoc[3],faceLoc[0]), (faceLoc[1], faceLoc[2]), (255,0,255),2)
#
# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLocTest[3],faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255,0,255),2)

# results = face_recognition.compare_faces([encodeElon],encodeTest)
# faceDist = face_recognition.face_distance([encodeElon], encodeTest)
# print(faceDist)
#
# cv2.putText(imgTest, f"{results} {round(faceDist[0],2)}", (50, 50), cv2.FONT_ITALIC,1,(0,0,255),2)
# cv2.imshow("Elon Musk", imgElon)
# cv2.imshow("Elon Test", imgTest)
#
# cv2.waitKey(0)