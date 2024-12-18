import pyttsx3 as py,time as t
from os import chdir,rename,system
boss=open(r"C:\Users\Public\Name.txt").read()
def exiter():
    try:
        chdir(r"C:\Users\GOKULNAVEEN\Desktop")
        rename("JARVIS_SUPPORTER.py","JARVIS_SUPPORTER.img")
    except:
        print()
    try:
        chdir(r"C:\Users\Public")
        rename("JARVIS_SUPPORTER.py","JARVIS_SUPPORTER.img")
    except:
        print()
from speech_recognition import Recognizer,recognizers,Microphone,UnknownValueError,RequestError
from AppOpener import open,close
from difflib import get_close_matches as get
from screen_brightness_control import set_brightness
from pyautogui import moveTo,click,rightClick
from pywhatkit import playonyt as pl,search
from struct import unpack_from
from pvporcupine import create
from sys import exit as e
from time import sleep
from pyvolume import custom
from keyboard import send,write
from pyaudio import PyAudio,paInt16
from wikipedia import summary
from pygame import mixer
system("cls")
mixer.init()
eng=py.init()
v=eng.getProperty("voices")
eng.setProperty("voice",v[1].id)
r=Recognizer()
process=["whatsapp","file explorer","visual studio code","opera browser"]
apps={
    "operamini":"opera browser",
    "command prompt":"command prompt",
    "whatsapp" :"whatsapp",
    "powershell":"windows powershell",
    "fx sound":"fxsound",
    "file manager":"file explorer",
    "visual studio":"visual studio code",
    "settings":"settings",
    "ms office":"word",
    "live walpaper":"lively wallpaper",
    "calculator":"calculator",#not ok
    "video player":"vlc media player",#not ok
    "wordpad":"wordpad",
    "notepad":"notepad",
    "app editor":"sublime text",#not ok
    "task manager":"task manager",#not ok
    "register editor":"registry editor",#not ok
    "microsoft edge":"microsoft edge",
    "shareit":"shareit",
    "google chrome":"google chrome",
    "chrome":"google chrome",
    "edge":"microsoft edge",
    "music":"music",
    "groove music":"music",
    "movies player":"movies & tv",
    "photos":"photos",
    "windows photos viwer":"photos",
    "get office":"get office",
    "office":"get office",
    "xbox":"xbox",
    "store":"store",
    "onenote":"onenote",
    "mail":"mail",
    "calendar":"calendar",
    "weather":"weather",
    "get skype":"get skype",
    "voice recorder":"voice recorder",
    "appkiwi":"appkiwi",
    "alarms & clock":"alarms & clock",
    "avg":"avg secure browser",
    "python -bit":"python -bit",
    "amd settings":"amd radeon settings",
    "camera":"camera",
    "contact":"contact support",
    "booking":"booking",
    "botim":"botim",
    "onedrive":"onedrive",
    "people":"people",
    "skype":"skype",
    "dvd video playe":"dvdvideosoft free studio",
    "dvd":"dvdvideosoft free studio",
    "decacopy lite":"decacopy lite",
    "kmplayer":"kmplayer",
    "imo messenger":"imo messenger",
    "teracopy":"teracopy",
    "tips":"tips"
   }
def trans():
    system("cls")
    with Microphone() as mic:
            r.adjust_for_ambient_noise(mic,duration=0.5)
            mixer.music.load(r"C:\Users\Public\SOUNDS\strange-notification-36458.mp3")
            mixer.music.play()
            print("LISTANING.........")
            sleep(0.5)
            send("D")
            r.pause_threshold=1
            
            audio=r.listen(mic)
            try:
                send("D")
                mixer.music.load(r"C:\Users\Public\SOUNDS\off.mp3")
                mixer.music.play()
                print("RECOGNIZING........")
                txt2=r.recognize_google(audio,language="en_US")
                mixer.music.load(r"C:\Users\Public\SOUNDS\notification-2-269292.mp3")
                mixer.music.play() 
            except UnknownValueError:
                txt2=""
                print("SORRY UNKNOWN-VALUE-ERROR\nPLEASE TRY AGAIN...")
            except RequestError as e:
                txt2=""
                print("Error; {0}".format(e))
            except TypeError:
                txt2=""
                print("SORRY TYPE-ERROR\nPLEASE TRY AGAIN...")
                spack("TYPE ERROR,PLEASESAY AGAIN")
            except ConnectionResetError:
                txt2=""
                print("CONNECTION-ERROR,PLEASE RTY AGAIN")
                spack("CONNEACTION ERROR TRY AGAIN")
            except ValueError:
                txt2=""
                spack("sorry valuerror")
    return txt2.lower()
def op(l):
    process.append(l)
    print(l+" IS IN RUNNING LIST")
def cl(l):
    try:
        process.remove(l)
    except ValueError:
        print(l+" IS NOT IN LIST")
def clal():
    for i in process:
        close(i,match_closest=True,output=True)
        process.remove(i)
    spack("CLOSING FINISH")
def num_dev(l):
    a1=[]
    a2=""
    for chr in l:
        if chr.isdigit():
            a1.append(str(chr)) 
    if len(a1)==2:
        a2=int(a1[0]+a1[1])
    if len(a1)==3:
        a2=int(a1[0]+a1[1]+a1[2])
    return a2
def num_tab(l):
    for i in l:
        try:
            i1=int(i)
            l1=i1.is_integer()
            if l1==True:
                print()
        except:
            continue   
def num_finder(l):
    for i in l:
        try:
            i1=int(i)
            l1=i1.is_integer()
            if l1==True:
                return i1
        except:
            continue
def Refresher(num):
        send("windows+m")
        t.sleep(1)
        try:
            for i in range(1,num+1):
                moveTo(700,60)
                rightClick()
                moveTo(710,110)
                t.sleep(0.30)
                click() 
        except:
            spack("none typical error.... refreshing 2 times")
            for i in range(2):
                moveTo(700,60)
                rightClick()
                moveTo(710,110)
                t.sleep(0.30)
                click() 
def shutdown():
    spack("shutdowning...")
    spack(f"good bye {boss}")
    system('shutdown /s /t 0')
def spack(t):
    eng.say(t)
    eng.runAndWait()
def start():
            room=1
            mixer.music.load(r"C:\Users\Public\SOUNDS\on.mp3")
            mixer.music.play()
            spack(f"HOW CAN I HELP U {boss}")
            while room==1:  
                p2=""
                txt2=trans()
                print("YOU SAID: "+txt2)          
                "boss"in txt2 is spack(f"YOUR MY BOSS {boss}")
                "version"in txt2 is spack(f"I'M JARVIS VESION 4.0 AND I'M EARLY ACCESS VERSION NOW") 
                "who is your creator"in txt2 is spack("NAVEEN KUMAR IN MY AUTHOR")
                "how r u"in txt2 is spack("I AM GOOD SIR THANKS TO CARE ME SIR")
                if"open"in txt2 or "close"in txt2 :
                    txt3=txt2.replace("open","")
                    txt1=get(txt3,apps.keys(),n=1)
                    if "close it"in txt2 or"close current window"in txt2 or "close the window"in txt2 or"close the current window"in txt2:
                            spack("CLOSING CURRENT WINDOW")
                            send("alt+f4")
                            sleep(1)
                            send("enter")
                            room=2
                            continue
                    elif "close the tab"in txt2 or "close current tab" in txt2 or "close current screen"in txt2 or "close the current tab" in txt2:
                        spack("CLOSING COURENT TAB")
                        send("ctrl+w")
                        room=2
                        continue
                    elif "open tab"in txt2 or "open the tab"in txt2:
                        i1=num_finder(txt2)
                        spack(f"opening tab {i1}")
                        send(f"windows+{i1}")
                        room=2
                        continue
                    elif "open it"in txt2 or "again"in txt2 or "open last tab"in txt2 or "open close tab"in txt2:
                            spack("REOPENING CLOSED WINDOW")
                            send("ctrl+shift+t")
                            room=2
                            continue
                    elif "close all"in txt2:
                        spack(f"REALY YOU WANT TO CLOSE ALL PROGRAMS {boss}")
                        choice=trans().lower()
                        if "of course"in choice or"yes"in choice or"do" in choice or"do it"in choice or "you can do"in choice:
                            spack("CLOSING ALL RUNNING PROGRAMS")
                            clal()
                            spack("DO U WANT TO SHUTDOWN U R PC")
                            ans=trans()
                            if "ofcourse"in ans or"do"in ans or"do it"in ans or "you can do"in ans:
                                shutdown()
                                room=2
                                continue
                            elif"don't"in ans or "no"in ans or "not need"in ans or "no nood"in ans or "not necessary"in ans:
                                spack("ABORTED FROM SHUTDOWN")
                                room=2
                                continue
                        elif"don't"in choice or "no"in choice or "not need"in choice or "no nood"in choice or "not necessary"in choice:
                            spack("ABORTED FROM CLOSING ALL APPS")
                            room=2
                            continue 
                        room=2
                        continue
                    elif "open search box"in txt2 or "open windows search box"in txt2 or "search app" in txt2 or "search application"in txt2:
                        spack("opening windows search box")
                        send("windows+s")
                        sleep(5)
                        spack("what you want to search")
                        at=trans().replace("search","").lower()
                        write(f"{at}")  
                        sleep(2)
                        spack("tell me what you want to select....... as up down right left.... and.....select say... for enter")
                        root=1
                        while root==1:  
                            at=trans().lower().replace("search","").replace("side","").replace("go to","").replace("go","")
                            if "right"in at:
                                send("right")
                            elif "down"in at:
                                send("down")
                            elif "up"in at:
                                send("up")
                            elif "left"in at:
                                send("left")
                            elif "enter"in at or "select"in at or "choose"in at:
                                spack("selecting")
                                send("enter")
                                root=2
                                room=2
                                continue
                            else:
                                spack("exit path 1")
                    try:
                        for i in txt1:
                            p2=p2+i
                        txt=apps[p2]
                        if "open" in txt2 or "start" in txt2:
                            spack("openig"+txt)
                            txt=txt.replace("open","").replace('start',"")
                            open(txt,match_closest=True)
                            return op(txt)
                        elif "close" in txt2 or "end"in txt2:  
                            spack("closing"+txt)
                            txt=txt.replace("close","").replace('end',"")
                            close(txt,match_closest=True,output=True)
                            p2=p2.replace(p2,"")
                            return cl(txt)                            
                    except KeyError:
                        print("I CAN'T UNDERSTAND PLEASE SAY THAT AGAIN")
                        spack("sorry please tell me again") 
                elif "refresh my pc"in txt2 or "refresh" in txt2:
                    a2=num_finder(txt2)
                    if a2 is int:
                        spack(f"STARTING REFRESH {a2} TIMES")
                    Refresher(a2)
                    spack("REFRESH FINISHED")
                    room=2
                    continue
                elif"exit"in txt2:
                    spack("stoping jarvis 4.0 early access version.....C U SOON SIR")
                    mixer.music.load(r"C:\Users\Public\SOUNDS\two-drops-87977.mp3")
                    mixer.music.play() 
                    exiter()
                    e()    
                elif"songs"in txt2 or "you tube"in txt2 or "youtube"in txt2 or "music"in txt2: 
                    if "youtube" in txt2 or "songs" in txt2 or"play" in txt2 or "you tube"in txt2 :
                        txt2=txt2.replace("you tube","").replace("youtube","").replace("play","").replace("in","").replace("on","")
                        spack("playing"+txt2),pl(txt2)
                        room=2
                        continue 
                    if "pause" or "stop" or "resume" or "pass"in txt2:
                        spack("ok sir")
                        send("play/pause media")
                        send("enter")
                        room=2
                        continue 
                    elif "next song"in txt2 or"next"in txt2:
                        spack("playing next song")
                        send("shift+n")
                        send("next track")
                        room=2
                        continue
                    elif "previwe"in txt2 or "last"in txt2 or "previos" in txt2:
                        spack("plaing last played song")
                        send("previous track")
                        room=2
                        continue
                elif"jarvis" or "jarves" in txt2:
                    txt3=txt2
                    txt3=txt3.replace("jarvis","").replace("jarves","")
                    "hey"in txt3 is spack("YES SIR I HONER TO MEET U HOW CAN I HELP YOU SIR") 
                    "how are you"in txt3 is spack("I AM GOOD SIR THANKS TO CARE ME SIR")
                    "are you fine"in txt3 is spack("YES SIR I'M FINE THANKS TO WORRY ABOUT ME SIR")
                    "new command prompt" or "new cmd"in txt3 is spack("OPENING NEW WINDOW CMD"),system('prompt') 
                    "update"in txt3 is spack("YES SIR I'M UPDATED VERSION 4.0 AS EARLY ACCESS")
                    "can you mak me a faver"in txt3 is spack("YES SIR I CAN......TELL ME WHAT U WANT SIR")
                    "i miss you" in txt3 in spack(f"i missed you too {boss}")
                    if"jarvis"in txt2 and "bhai" in txt2 or "bye" in txt2 or "buy"in txt2 or "by" in txt2 or "stop" in txt2:
                        spack("C U AGAIN SIR")                       
                        mixer.music.load(r"C:\Users\Public\SOUNDS\two-drops-87977.mp3")
                        mixer.music.play()  
                        room=2
                        continue
                    elif"what"in txt2:
                        "what is your name"in txt2 is spack("MY NAME IS JARVIS VERSION 4.0 AND MY CREATORE IS NAVEEN SABINA AND NOW I'M EARLY ACCESS VERSION")
                        txt2=txt2.replace("what","")
                        if"tell me"in txt2 or"wikipedia"in txt2 :
                            txt2.replace("wikipedia","")
                            spack("results os"+txt2+" back from a search")
                            result=summary(txt2,2)
                            spack(f"the {txt2} of answer is "+result)
                            room=2
                            continue
                        elif"search"in txt2 or"google"in txt2:
                            txt2.replace("search","")
                            spack("results of"+txt2+" back from a search")
                            search(txt2)
                            room=2
                            continue
                    elif"lock"in txt2 or "lock my pc"in txt2 or "lock my screen"in txt2:
                        spack("LOCKING")
                        system("Rundll32.exe user32.dll,LockWorkStation")
                        room=2
                        continue
                    elif "restar"in txt2 or "restart my pc"in txt2:                    
                        spack("COMPUTER RESTARTING NOW")
                        spack(f"meet u soon {boss}")
                        system('shutdown /r /t 0')
                        room=2
                        continue                         
                    elif "shutdown" in txt2 or "shut down my pc"in txt2 :                     
                        shutdown()
                        room=2
                        continue
                    elif "minimaise"or "maximaise" or"putit"or"make"or "maximize"or"minimize"or"resume"or"recent window"or"change tab"or"valume"or"sound"or "change tab"in txt2 or "change the tab" in txt2 or "recent tab" in txt2 or"tab"  in txt2:
                        txt2=txt2.replace("make it","").replace("minimaise","")
                        try:
                            if"escape"in txt2 or"enough"in txt2:
                                spack("OK SIR")
                                send("esc")
                            elif "brightness" in txt2 or"set brightness"in txt2:
                                a2=num_dev(txt2)
                                spack(f"setting brightness {a2} percentage")
                                set_brightness(a2)
                            elif"show all windows" in txt2 or "show all window"in txt2:
                                spack("THERE REMAINING TABS SIR")
                                send("windows+tab")
                            elif"all"in txt2:
                                spack("MINIMIZING ALL APPLICATIONS")
                                send("windows+m")
                            elif"minimise"in txt2 or "minimize"in txt2:
                                spack("MINIMASING...")
                                send("windows+down")
                                sleep(1)
                                send("windows+down")
                            elif"maximise"in txt2 or "maximize"in txt2:
                                spack("MAXIMIZING")
                                send("windows+up")
                                sleep(1)
                                send("windows+up")
                            elif"right"in txt2 :
                                spack("GETING RIGHT")
                                send("windows+right")
                            elif"left"in txt2 :
                                spack("GETING LEFT")
                                send("windows+left")
                            elif"resume"in txt2 or "pause"in txt2 or "pass"in txt2:
                                spack(txt2+"ing")
                                send("space")                                                  
                            elif"full"in txt2 or "off" in txt2 or"on"in txt2:
                                if "full screen advertisement" in txt2 or "full screen ad"in txt2 or "on screen advertisement" in txt2 or "on screen advertise"in txt2 or"full screen advertise" in txt2 or "skip full screen" in txt2: 
                                    spack("SKIPING FULL SCREEN advertisement")
                                    moveTo(1285,640,duration=1) # for full screen
                                    click()
                                elif "small screen advertisement" in txt2 or "off screen advertisement" in txt2 or "off screen ad" in txt2 or "small screen ad"in txt2 or "skip off screen add" in txt2 or "skip off screen" in txt2 :
                                    spack("SKIPING OFF SCREEN advertisement")
                                    moveTo(1285,540,duration=1) # for off  screen
                                    click()
                                else:
                                    spack("SCREENING")
                                    send("f")
                            elif"recent window"in txt2 or "change the screen"in txt2  or "change the window"in txt2  or "change screen" in txt2  or "change window"in txt2:
                                spack("changing window")
                                send("alt+tab")
                            elif"change tab"in txt2 or "change the tab" in txt2 or "recent tab" in txt2 or"tab"in txt2:
                                if"change tab" or "change the tab" in txt2:
                                    spack("changing tab")
                                    send("ctrl+tab")
                            elif"volume"in txt2 or "sound"in txt2 or"sounds"in txt2:
                                a2=int(num_dev(txt2))
                                spack(f"seting valume {a2} percentage")
                                custom(percent=a2)
                            elif"mute sound" in txt2 or"mute valume"in txt2 or"unmute valume"in txt2 or"unmute sound"in txt2 or"mute"in txt2:
                                txt=txt2.replace("valume","").replace("sound","")
                                spack(txt+"ing")
                                send("D")
                            elif "next song"in txt2 or"next"in txt2:
                                spack("playing next song")
                                send("next track")
                            elif "previwe"in txt2 or "last"in txt2:
                                spack("plaing last played song")
                                send("previous track")
                            room=2
                            continue 
                    
                        except KeyError:
                            print("I CAN'T UNDERSTAND PLEASE SAY THAT AGAIN")
                else:
                    spack("please tell again sir") 
while True:
    exiter()
    pvp=None
    pyaud=None
    audio_stream=None
    print("IT,S ON WORKING.......") 
    spack("activated")
    spack(f"i honer to meet u {boss}")
    try: 
        pvp=create(keywords=["jarvis","alexa","computer"],access_key="yWK2HAMS6eaY/Gu3/vRFqLHWZAK4/D2e73KENGLlavkkhPu4RIDUuQ==")
        pyaud=PyAudio()
        audio_stream=pyaud.open(rate=pvp.sample_rate,channels=1,format=paInt16,input=True,frames_per_buffer=pvp.frame_length)
        while True: 
            pcm=audio_stream.read(pvp.frame_length)
            pcm=unpack_from("h"*pvp.frame_length,pcm)
            keyword_index=pvp.process(pcm)
            if keyword_index>=0:
                print("hot word detected")
                start()
    finally:
        if pvp is not None:
            pvp.delete()
        if audio_stream is not None:
            audio_stream.close()                    