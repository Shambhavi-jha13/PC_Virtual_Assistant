# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 22:36:50 2021

@author: Shambhavi Jha
"""

import speech_recognition as sr
r= sr.Recognizer()

with sr.Microphone() as source:
    print("start saying...!!")
    audio = r.listen(source)
    print("speech done!")
    r.recognize_google(audio)
