from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkcalendar import Calendar

import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

Amount_paid=3500
Interest=2
credit_date="04/07/21"
submit_date="09/24/21"
name="Atul"
dic={"one":1, "two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"zero":0}
cart=["Monte carlo black hooded M size tshirt","levis jeans sized 38","jockey XXL underwear"]
address="Dayal Residency near BBD , Lucknow"
k=9
n=0
def speak(text):
    engine.say(text)
    engine.runAndWait()
"""def speak(text):
    tts=gTTS(text=text, lang="en")
    filename=os.path.dirname(__file__)+"\\voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)"""

def audio():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r.listen(source)
        said=""

        try:
            said=r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: "+str(e))
    return said



def voiceb():
    text="hello"+name+"Welcome to Flipkart , How may I help you"
    speak(text)
    text=audio()
    speak("You said "+text)
    speak("Checking you cart")
    for i in range(len(cart)):
        if(i==len(cart)-1):
            speak(" and ")
        text="item number "+str(i+1)+"is"
        speak(text+cart[i])
    speak("do you want to buy it on one command")
    text=audio()
    if "yes" in text or "ya" in text:
        speak("Plz confirm your Details")
        text="your name is "+name+"Your contact number is "+"XXXXXXX82"+"and your address is "+address
        speak(text)
        speak("do you want to pay now or pay later")
        text=audio()
        if "later" in text:
            speak("order placed , thank you for shopping with flipkart")
        elif "now" in text:
            speak("Tell us OTP")
            text=audio() 
                        
            if text=='1234':
                speak("order placed , thank you for shopping with flipkart")
            else:
                speak("Wrong OTP")

def paymentvoice():
        speak("Plz confirm your credit card Details")
        text="your name is "+name+"Your credit card number is "+"XXXX82"
        speak(text)
        speak("Tell us OTP")
        text=audio()               
        if text=='1234':
            speak("Payment done , thank you for shopping with flipkart")
        else:
            speak("Wrong OTP")

def voiceb2():
    speak("your credit card named "+name)
    text="Your Due amount is "+str(Amount_paid)
    speak(text)
    text="your Due date is "+submit_date[3:5]+ "of this month"
    speak(text)
    text="Do you want to PAY NOW or Pay Later Please click on Button"
    speak(text)


def voiceop(ap,sd):
    text="Updated Submit date is "+sd[3:5]+sd[0:2]+",and calculated amount is "+str(ap)
    speak(text)
    

LARGEFONT=("vardana",20)
class tkinterApp(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        container=Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for F in (homepage,creditpage,shoppage):
            frame=F(container,self)
            self.frames[F]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(homepage)

    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()

class homepage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        toolbar=Frame(self,background="white",bd=1,relief=RAISED)
        toolbar.pack(side=TOP,fill=X)
        global bg
        path=Image.open("Untitled design (5).png")
        
        bg=ImageTk.PhotoImage(path)
        
        label1=Label(self,image=bg)
        label1.pack(side=BOTTOM,fill=BOTH,expand=YES)
        
        home_button=Button(toolbar,bg="#00BFFF",text="HOME")
        home_button.grid(row=0,column=0)
        inputtxt=Text(self,height=2,width=40)
        inputtxt.place(x=190,y=350)

        imgb7=Image.open("acc2.png")
        b7image=ImageTk.PhotoImage(imgb7)
        accbutton=Button(toolbar,text="",image=b7image,borderwidth=0)
        accbutton.place(x=590,y=0)
        accbutton.image=b7image

        imgb8=Image.open("not1.png")
        b8image=ImageTk.PhotoImage(imgb8)
        nortbutton=Button(toolbar,text="",image=b8image,borderwidth=0)
        nortbutton.place(x=630,y=0)
        nortbutton.image=b8image

        imgb9=Image.open("help.png")
        b9image=ImageTk.PhotoImage(imgb9)
        helpbutton=Button(toolbar,text="",image=b9image,borderwidth=0)
        helpbutton.place(x=670,y=0)
        helpbutton.image=b9image
        
        
        b2image=PhotoImage(file="mc1.png")
        
        micbutton=Button(self,text="",command=voiceb,image=b2image,borderwidth=0)
        micbutton.place(x=520,y=340)
        micbutton.image=b2image
        imgb3=Image.open("ms1.png")
        b3image=ImageTk.PhotoImage(imgb3)
        msgbutton=Button(self,text="",image=b3image,borderwidth=0)
        msgbutton.place(x=130,y=340)
        msgbutton.image=b3image
        imgb4=Image.open("cr1.png")
        b4image=ImageTk.PhotoImage(imgb4)
        credbutton=Button(self,text="",command=lambda : controller.show_frame(creditpage),image=b4image,borderwidth=0)
        credbutton.place(x=5,y=100)
        credbutton.image=b4image
        imgb5=Image.open("sh1.png")
        b5image=ImageTk.PhotoImage(imgb5)
        shopbutton=Button(self,text="",command=lambda : controller.show_frame(shoppage),image=b5image,borderwidth=0)
        shopbutton.place(x=5,y=180)
        shopbutton.image=b5image
        imgb6=Image.open("st1.png")
        b6image=ImageTk.PhotoImage(imgb6)
        setbutton=Button(self,text="",image=b6image,borderwidth=0)
        setbutton.place(x=5,y=250)
        setbutton.image=b6image
        
        
class creditpage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        ctoolbar=Frame(self,background="white",bd=1,relief=RAISED)
        ctoolbar.pack(side=TOP,fill=X)
        global bg1
        path=Image.open("bg2.png")
        
        bg1=ImageTk.PhotoImage(path)
        
        clabel1=Label(self,image=bg1)
        clabel1.pack(side=BOTTOM,fill=BOTH,expand=YES)
        chome_button=Button(ctoolbar,command=lambda : controller.show_frame(homepage),bg="#00BFFF",text="HOME")
        chome_button.grid(row=0,column=0)
        tlabel=Label(self,text="Credit Card due bill",bg="black",fg="white",font=LARGEFONT)
        tlabel.place(x=220,y=40)

        tlabel1=Label(self,text="Amount",bg="black",fg="white",font=("Arial",15))
        tlabel1.place(x=200,y=120)
        
        tlabel1=Label(self,text=Amount_paid,bg="black",fg="white",font=("Arial",15))
        tlabel1.place(x=420,y=120)
        tlabel2=Label(self,text="Credit Date",bg="black",fg="white",font=("Arial",15))
        tlabel2.place(x=200,y=160)
        
        tlabel2=Label(self,text=credit_date,bg="black",fg="white",font=("Arial",15))
        tlabel2.place(x=420,y=160)
        tlabel3=Label(self,text="Submit Date",bg="black",fg="white",font=("Arial",15))
        tlabel3.place(x=200,y=200)
        
        tlabel3=Label(self,text=submit_date,bg="black",fg="white",font=("Arial",15))
        tlabel3.place(x=420,y=200)
        tlabel4=Label(self,text="Interest (if any)",bg="black",fg="white",font=("Arial",15))
        tlabel4.place(x=200,y=240)
        
        tlabel4=Label(self,text=str(Interest)+"%",bg="black",fg="white",font=("Arial",15))
        tlabel4.place(x=420,y=240)

        imgbc1=Image.open("PAY NOW.png")
        bc1image=ImageTk.PhotoImage(imgbc1)
        paybutton=Button(self,text="",command= paymentvoice, image=bc1image,borderwidth=0)
        paybutton.place(x=200,y=300)
        paybutton.image=bc1image
        imgbc2=Image.open("PAY LATER.png")
        bc2image=ImageTk.PhotoImage(imgbc2)

        def date_extend():
            window=Tk()
            window.geometry("260x300")
            window.resizable(0,0)
            cal=Calendar(window,selectmode='day',year=2021,month=9,day=24)
            cal.place(x=5,y=10)
            def get_date():
                datelab.config(text="Date Extend till "+cal.get_date()) 
                submit_date=str(cal.get_date())
                tlabel3.config(text=submit_date)
                n=(int(submit_date[0]))*10+(int(submit_date[1]))-k;
                Amount_paid=int(3500+((3500*2)/100)*n)
                tlabel1.config(text=Amount_paid)
                voiceop(Amount_paid,submit_date)
                
            Button(window,text="Extend Date",command=get_date).place(x=100,y=230)
            datelab=Label(window,text="")
            datelab.place(x=60,y=260)
            window.mainloop()
        datebutton=Button(self,text="",command=date_extend,image=bc2image,borderwidth=0)
        datebutton.place(x=420,y=300)
        datebutton.image=bc2image

        imgbc3=Image.open("mc1.png")
        bc3image=ImageTk.PhotoImage(imgbc3)
        cmicbutton=Button(self,text="",command= voiceb2,image=bc3image,borderwidth=0)
        cmicbutton.place(x=540,y=295)
        cmicbutton.image=bc3image
class shoppage(Frame):
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        stoolbar=Frame(self,background="white",bd=1,relief=RAISED)
        stoolbar.pack(side=TOP,fill=X)
        global bg2
        path=Image.open("bg2.png")
        
        bg2=ImageTk.PhotoImage(path)
        
        slabel1=Label(self,image=bg2)
        slabel1.pack(side=BOTTOM,fill=BOTH,expand=YES)
        shome_button=Button(stoolbar,command=lambda : controller.show_frame(homepage),bg="#00BFFF",text="HOME")
        shome_button.grid(row=0,column=0)
        
        simgb1=Image.open("Fs1.png")
        s1image=ImageTk.PhotoImage(simgb1)
        fasbutton=Button(self,text="",image=s1image,borderwidth=0)
        fasbutton.place(x=40,y=40)
        fasbutton.image=s1image
        
        simgb2=Image.open("mob.png")
        s2image=ImageTk.PhotoImage(simgb2)
        mobbutton=Button(self,text="",image=s2image,borderwidth=0)
        mobbutton.place(x=170,y=40)
        mobbutton.image=s2image

        simgb3=Image.open("ele.png")
        s3image=ImageTk.PhotoImage(simgb3)
        elebutton=Button(self,text="",image=s3image,borderwidth=0)
        elebutton.place(x=300,y=40)
        elebutton.image=s3image

        simgb4=Image.open("home.png")
        s4image=ImageTk.PhotoImage(simgb4)
        hombutton=Button(self,text="",image=s4image,borderwidth=0)
        hombutton.place(x=430,y=40)
        hombutton.image=s4image

        simgb5=Image.open("app.png")
        s5image=ImageTk.PhotoImage(simgb5)
        appbutton=Button(self,text="",image=s5image,borderwidth=0)
        appbutton.place(x=40,y=170)
        appbutton.image=s5image

        simgb6=Image.open("bea.png")
        s6image=ImageTk.PhotoImage(simgb6)
        beabutton=Button(self,text="",image=s6image,borderwidth=0)
        beabutton.place(x=170,y=170)
        beabutton.image=s6image

        simgb7=Image.open("toy.png")
        s7image=ImageTk.PhotoImage(simgb7)
        toybutton=Button(self,text="",image=s7image,borderwidth=0)
        toybutton.place(x=300,y=170)
        toybutton.image=s7image

        simgb8=Image.open("furn.png")
        s8image=ImageTk.PhotoImage(simgb8)
        furbutton=Button(self,text="",image=s8image,borderwidth=0)
        furbutton.place(x=430,y=170)
        furbutton.image=s8image

        simgb9=Image.open("spor.png")
        s9image=ImageTk.PhotoImage(simgb9)
        spobutton=Button(self,text="",image=s9image,borderwidth=0)
        spobutton.place(x=40,y=300)
        spobutton.image=s9image

        simgb10=Image.open("grocery.png")
        s10image=ImageTk.PhotoImage(simgb10)
        grobutton=Button(self,text="",image=s10image,borderwidth=0)
        grobutton.place(x=170,y=300)
        grobutton.image=s10image

        simgb11=Image.open("heritage.png")
        s11image=ImageTk.PhotoImage(simgb11)
        heributton=Button(self,text="",image=s11image,borderwidth=0)
        heributton.place(x=300,y=300)
        heributton.image=s11image

        simgb12=Image.open("ins.png")
        s12image=ImageTk.PhotoImage(simgb12)
        insbutton=Button(self,text="",image=s12image,borderwidth=0)
        insbutton.place(x=560,y=40)
        insbutton.image=s12image

        simgb13=Image.open("food.png")
        s13image=ImageTk.PhotoImage(simgb13)
        foodbutton=Button(self,text="",image=s13image,borderwidth=0)
        foodbutton.place(x=560,y=170)
        foodbutton.image=s13image

        simgb14=Image.open("gift.png")
        s14image=ImageTk.PhotoImage(simgb14)
        giftbutton=Button(self,text="",image=s14image,borderwidth=0)
        giftbutton.place(x=430,y=300)
        giftbutton.image=s14image

        simgb15=Image.open("flight.png")
        s15image=ImageTk.PhotoImage(simgb15)
        flibutton=Button(self,text="",image=s15image,borderwidth=0)
        flibutton.place(x=560,y=300)
        flibutton.image=s15image

        

        
        
        
        
        
                
        

        
root=tkinterApp()
root.geometry("700x399")
root.resizable(0,0)
root.mainloop()
        
