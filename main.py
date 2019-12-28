# coding: utf-8
 
from tkinter import * 
import os
from os import listdir
import stat 
import json
from os.path import expanduser
from tkinter import filedialog

wifi_folder = "/etc/NetworkManager/system-connections/"
home = expanduser("~")
fenetre = Tk()

def save():
    all_wifi = {"version_wifi_exporter":1}
    f = []

    for filename in listdir(wifi_folder):
        all_wifi[filename] = open(wifi_folder+filename).read()

    #my_dump = open(home+os.sep+"wifiExporter.dump","w")
    #my_dump.write(json.dumps(all_wifi))
    #my_dump.close()

    files = [('All Files', '*.*'),  
             ('dump', '*.dump')] 
    my_dump = filedialog.asksaveasfile(filetypes = files, defaultextension = files,initialdir = home) 
    my_dump.write(json.dumps(all_wifi))
    my_dump.close()

    fenetre.label.sv.set("The backup file is "+home+os.sep+"wifiExporter.dump")
def restore():
    my_dump =  filedialog.askopenfilename(initialdir = home,title = "Select file",filetypes = (("dump files","*.dump"),("all files","*.*")))
    if my_dump =="":
        return
    my_dump = open(my_dump,"r")
    all_wifi = json.loads(my_dump.read())
    my_dump.close()
    if not "version_wifi_exporter" in all_wifi.keys():
            fenetre.label.sv.set("please take a wifi_exporter file !!!!")
            return
    else:
        del all_wifi["version_wifi_exporter"]
    for filename,content in all_wifi.items():
        my_dump = open(wifi_folder+filename,"w")
        os.chown(wifi_folder+filename, 0, 0)# set root right
        os.chmod(wifi_folder+filename, stat.S_IREAD) 
        my_dump.write(content)
    fenetre.label.sv.set("done :)   please reboot ! ")




l = LabelFrame(fenetre, text="Message", padx=20, pady=20)
l.pack(fill="both", expand="yes")
sv = StringVar()
label = Label(l, textvariable=sv)
label.pack()
sv.set("Please click on Export for stock your wifi password in your home ("+home+"/wifiExporter.dump). And import for automaticaly import this file in your system")
fenetre.label = label
fenetre.label.sv = sv
save=Button(fenetre, text="Export wifi passwords", command=save)
save.pack()
restore=Button(fenetre, text="Import wifi passwords", command=restore)
restore.pack()
fenetre.mainloop()
