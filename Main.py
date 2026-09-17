import tkinter as tk
from tkinter import Message ,Text
#import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
import linreg as lin
import KNeighborsRegressor as knn
import Plot_Graph as pg

from matplotlib import pyplot as plt



from_date = datetime.datetime.today()

currentDate = time.strftime("%d_%m_%y")

#font = cv2.FONT_HERSHEY_SIMPLEX
#fontScale=1
#fontColor=(255,255,255)

cond=0


window = tk.Tk()
window.title("Air Quality Prediction")

 
window.geometry('1280x720')
window.configure(background='blue')

#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)


message1 = tk.Label(window, text="Air Quality Prediction" ,bg="blue"  ,fg="white"  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
message1.place(x=100, y=20)



def clear():
	txt.delete(0, 'end')    
	res = ""
	message.configure(text= res)
    
	
def linear():
	print("Linear Regression")
	lin.Predict()
	
def kn():
	print("Knn Regressor")
	knn.Predict()

def plot():
	print("PlotGraph")
	pg.Graph()
	


  
clearButton = tk.Button(window, text="Clear", command=clear  ,fg="white"  ,bg="red"  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
clearButton.place(x=950, y=100)

trainImg = tk.Button(window, text="PREDICT Using Linear Regression", command=linear  ,fg="red"  ,bg="yellow"  ,width=30  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
trainImg.place(x=400, y=200)

detect = tk.Button(window, text="PREDICT Using Knn Regressor", command=kn  ,fg="red"  ,bg="yellow"  ,width=30  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
detect.place(x=700, y=400)

detect = tk.Button(window, text="PlotGraph", command=plot  ,fg="red"  ,bg="yellow"  ,width=30  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
detect.place(x=900, y=600)

quitWindow = tk.Button(window, text="QUIT", command=window.destroy  ,fg="white"  ,bg="red"  ,width=20  ,height=3, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=200, y=600)

 
window.mainloop()