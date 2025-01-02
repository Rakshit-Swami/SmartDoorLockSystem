import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
import pickle
import pathlib
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Door ")
        self.root.geometry("1000x520+290+98")
        self.root.config(bg="#050505")
        self.root.resizable(False,False)
        
        
        #icon image
        icon_image=tk.PhotoImage(file="images/icon.png")
        root.iconphoto(False,icon_image)
        
        #background image
        
        self.background_photo=Image.open("images/smart door.png")
        
        self.background_photo=ImageTk.PhotoImage(self.background_photo)
        tk.Label(root,image=self.background_photo,background="#242424").place(x=45,y=20)
        
        
        
        self.path = 'Access'
        self.images = []
        self.classNames = []
        self.mylist = os.listdir(self.path)

        for cl in self.mylist:
            curImg = cv2.imread(f'{self.path}/{cl}')
            self.images.append(curImg)
            self.classNames.append(os.path.splitext(cl)[0])

        self.encoded_face_train = self.find_encodings(self.images)

        self.cap = cv2.VideoCapture(0)

        self.create_widgets()

    def find_encodings(self, images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encoded_face = face_recognition.face_encodings(img)[0]
            encodeList.append(encoded_face)
        return encodeList

    def mark_attendance(self, name):
        with open('Database/Attendance.csv', 'r+') as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])
            if name not in nameList:
                now = datetime.now()
                time = now.strftime('%I:%M:%S:%p')
                date = now.strftime('%d-%B-%Y')
                f.writelines(f'\n{name}, {time}, {date}')

    def update_frame(self):
        success, img = self.cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faces_in_frame = face_recognition.face_locations(imgS)
        encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
        for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
            matches = face_recognition.compare_faces(self.encoded_face_train, encode_face)
            faceDist = face_recognition.face_distance(self.encoded_face_train, encode_face)
            matchIndex = np.argmin(faceDist)
            print(matchIndex)
            if matches[matchIndex]:
                name = self.classNames[matchIndex].upper().lower()
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                self.mark_attendance(name)
        photo = self.convert_image_to_photo(img)
        self.label.config(image=photo)
        self.label.image = photo
        self.root.after(10, self.update_frame)

    def convert_image_to_photo(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        photo = ImageTk.PhotoImage(image=image)
        return photo

    def create_widgets(self):
        self.label = ttk.Label(self.root)
        self.label.pack(padx=10, pady=10)

        self.quit_button = ttk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.pack(pady=10)

        self.update_frame()

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    root.mainloop()
