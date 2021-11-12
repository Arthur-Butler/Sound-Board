# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:23:14 2021

@author: Arthu
"""
import tkinter as tk
from soundPlayer import function_crickets
from soundPlayer import function_laughter
from soundPlayer import function_wah
from soundPlayer import function_booing,function_poes,function_gay,function_gotHim

from pynput import keyboard

def window():
    window = tk.Tk()
    greeting = tk.Label(text="Soundboard")
    button1 = tk.Button(
        text="Laughter",
        width=5,
        height=1,
        bg="blue",
        fg="yellow",
        command=function_laughter
    )
    button2 = tk.Button(
        text="Crickets",
        width=5,
        height=1,
        bg="blue",
        fg="yellow",
        command=function_crickets
    )
    button3 = tk.Button(
        text="Fail",
        width=5,
        height=1,
        bg="blue",
        fg="yellow",
        command=function_wah
    )
    button4 = tk.Button(
        text="Boos",
        width=5,
        height=1,
        bg="blue",
        fg="yellow",
        command=function_booing
    ) 
    button5 = tk.Button(
        text="Poes",
        width=5,
        height=1,
        bg="blue",
        fg="yellow",
        command=function_poes
    )
    button6 = tk.Button(
        text="Gay",
        width=5,
        height=1,
        bg="blue",
        fg="yellow",
        command=function_gay
    )
    button7 = tk.Button(
        text="GotHim",
        width=5,
        height=1,
        bg="blue",
        fg="yellow",
        command=function_gotHim
    )
    greeting.pack()
    button1.pack()
    button2.pack()
    button3.pack()
    button4.pack()
    button5.pack()
    button6.pack()
    button7.pack()
    window.mainloop()


def on_press(key):
     if key==keyboard.Key.f2:
         function_laughter() 
     if key==keyboard.Key.f3:
         function_crickets()
     if key==keyboard.Key.f4:
         function_wah() 
     if key==keyboard.Key.f5:
         function_booing()

def on_release(key):
    if key ==keyboard.Key.esc:
        # Stop listener
        return False
    
window()  
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# Collect events until release
    #APPLICATION ID:902143970690351124
    #PUBLIC KEY:ae68333e3850ebb760b583d7c22e0ae36c8a46d54770caddf8454be5b0560e13