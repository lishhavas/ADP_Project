import tkinter as tk
from tkinter import *
from tkinter import filedialog
import pyautogui as pgui
import PyPDF2
import docx
import csv
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
pdfmrg=[] #list to store the path of all the selected files
pdfWriter=PyPDF2.PdfFileWriter()
n=0 #keeps the count of pdf
count=1 #used as a counter
while True:
user=pgui.prompt("Enter your choice\n 1.Merge PDF\n2.Word
Document\n3.Selenium\n4.CSV to JSON") #asks the user for choice
if user=='1' or user=='2' or user=='3'or user=='4' or user=='5':
#exception handling if user enters invalid choice
break
else:
pgui.alert("Enter the correct choice")