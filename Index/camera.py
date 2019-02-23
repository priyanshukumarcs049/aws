
import cv2
import face_recognition
import cv2
import glob
import time
import sys
import pickle
import numpy as np
import datetime as dt
from urllib.request import urlopen
import string
import random
from .models  import Notification
from datetime import datetime

known_face_names = []
known_face_encodings = []
N=10

with open('/home/aibssss/Videos/work22FEB/DemoForge/Index/templates/Index/cacase/known_face_names.pickle', 'rb') as f:
    known_face_names = pickle.load(f)
with open('/home/aibssss/Videos/work22FEB/DemoForge/Index/templates/Index/cacase/known_face_encodings.pickle', 'rb') as f:
    known_face_encodings = pickle.load(f)

#baseURL = 'http://crisil.xyz/naved/Web/notify?auth_key=666966123&title='


faceCascade = cv2.CascadeClassifier('/home/aibssss/Videos/work22FEB/DemoForge/Index/templates/Index/cacase/haarcascade_frontalface_default.xml')

class VideoCamera(object):

    def __init__(self,camID):
        self.camID= camID
        self.video = cv2.VideoCapture(camID)
        ret, frame = self.video.read()
        #print('return'+ str(ret))
        #print(camID)

    def __del__(self):
        self.video.release()



    def get_frame(self,CamNameT,camID,id):
        ret, frame = self.video.read()
        #print(camID)
        #print('ret'+str(ret))
        face_locations = []
        face_encodings = []
        face_names = []
        if ret == True:
            BGR = frame
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.3, minNeighbors = 9, minSize = (20, 20))
            for (x, y, w, h) in faces:
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                face_locations.append((y, x + w, y + h, x))
            RGB = BGR[: ,: , ::-1]
            face_encodings = face_recognition.face_encodings(RGB, face_locations)
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance = 0.45)
                name = "Unknown"
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                face_names.append(name)
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                cv2.rectangle(frame, (left, top), (right, bottom), (255, 0, 255), 2)
                #cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (255, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                #cv2.putText(frame, name, (left + 6, bottom + 10), font, 0.7, (255, 255, 255), 1)
                #s="http://1.22.125.227:25000/video_streamer/"+camID
                #filename=''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
                #fullpathfile=("{}{}{}".format('/home/aibssss/Videos/DemoForge/Index/static/Index/',filename,'.jpg'))
                #fullpathURL=("{}{}{}".format('http://1.22.125.227:25000/static/Index/',filename,'.jpg'))
                #cv2.imwrite(fullpathfile,frame)
                #f=urlopen(baseURL+name+'%20Detected&content='+name+'%20Detected%20at%20camera%20of%20'+CamNameT+'&img='+fullpathURL+'&svideo='+s)
                #f=urlopen(baseURL+name+'%20Detected&content='+name+'%20Detected%20at%20camera%20of%20'+CamNameT+'&svideo='+s)
                d=datetime.today()
                print(str(d.strftime('%b.%d,%G, %r'))+' '+name + ' Detected at camera ' + str(CamNameT))
                camObj = Notification.objects.create(name=name,place=str(CamNameT),time = str(d.strftime('%b.%d,%G, %r')),user = id)
                camObj.save()
                #LogFile = open('/home/aibssss/Videos/login/Index/templates/Index/cacase/log.txt','a')
                #LogFile.write(str(datetime.datetime.now().time())+'  '+name + ' Detected at camera ' + str(CamNameT))
                #LogFile.write('\n')
                #LogFile.close()

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()

    def get_frame1(self):
        ret, frame = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()
