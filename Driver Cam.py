import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox

def on_closing():
    # Release any resources or perform necessary cleanup before exiting
    root.destroy()

def hel():
    help(cv2)

def Contri():
    tkinter.messagebox.showinfo("Contributors","\n1. Siddhant Sanjay Patil \n")

def anotherWin():
    tkinter.messagebox.showinfo("About",'Driver Cam version v1.0\n Made Using\n-OpenCV\n-Numpy\n-Tkinter\n In Python 3')

def exitt():
    exit()

def web():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

def webdet():
    capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('lbpcascade_model_frontalface.xml')
    eye_glass = cv2.CascadeClassifier('haarcascade_model_eye_tree_eyeglasses.xml')

    while True:
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)

        for (x,y,w,h) in faces:
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            eye_g = eye_glass.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eye_g:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

def blink():
    capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('lbpcascade_model_frontalface.xml')
    eye_cascade = cv2.CascadeClassifier('model_eye.xml')
    blink_cascade = cv2.CascadeClassifier('ModelCustomBlinkCascade.xml')

    while True:
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, 'Face', (x + w, y + h), font, 1, (250, 250, 250), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            blink = blink_cascade.detectMultiScale(roi_gray)
            for (eyx, eyy, eyw, eyh) in blink:
                cv2.rectangle(roi_color, (eyx, eyy), (eyx + eyw, eyy + eyh), (255, 255, 0), 2)
                alert()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()

def alert():
    mixer.init()
    alert=mixer.Sound('detected.wav')
    alert.play()
    time.sleep(0.2)
    alert.play()

root = Tk()
root.geometry('500x570')
root.title('Driver Cam')

frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
frame.config(background='light blue')

label = Label(frame, text="Drowsiness Detection",bg='light blue',font=('Times 35 bold'))
label.pack(side=TOP)

filename = PhotoImage(file="Sleepy.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Tools",menu=subm1)
subm1.add_command(label="Open CV Docs",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="About",menu=subm2)
subm2.add_command(label="Driver Cam",command=anotherWin)
subm2.add_command(label="Contributors",command=Contri)

but1 = Button(frame, padx=5, pady=5, width=39, bg='light grey', fg='black', relief=SUNKEN, command=web, text='Open Cam', font=('helvetica 15 bold'))
but1.place(x=5, y=104)

but3 = Button(frame, padx=5, pady=5, width=39, bg='white', fg='black', relief=RIDGE, command=webdet, text='Open Cam & Detect', font=('helvetica 15 bold'))
but3.place(x=5, y=176)

but5 = Button(frame, padx=5, pady=5, width=39, bg='white', fg='black', relief=GROOVE, command=blink, text='Detect Eye Blink & Record With Sound', font=('helvetica 15 bold'))
but5.place(x=5, y=250)

but5 = Button(frame, padx=5, pady=5, width=5, bg='white', fg='black', relief=GROOVE, text='EXIT', command=exitt, font=('helvetica 15 bold'))
but5.place(x=210, y=322)

# Add event binding to handle window closing
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
