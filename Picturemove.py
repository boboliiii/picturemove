import os
import tkinter as tk
from tkinter import Frame, Button, Message, filedialog, Label, Entry
from PIL import Image, ImageTk, ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True
alphabet = ('0123456789abcdefghijklmnopqrstuvwxyz')
tk_root = tk.Tk()
tk_root.title("PictureMove 1.0")
file_count = 0
global changekey

global changingtime
changingtime=3
tk_root.withdraw()
folder_selected = filedialog.askdirectory(title='Please choose folder with pictures')
p = path = folder_selected
tk_root.deiconify()

def escape(e):
 quit()

def tab(e):
 top_text.configure(text="Type in which letter you want to change")
 global changingtime
 changingtime=1
 
def space(e): #skip file
 top_text.configure(text="Skipped")
 
 next_image()
 #top_text.after(3000, top_text.configure(text="sk"), 1)
  
def backspace(e):
 recycledir = os.path.join(path, 'Recycle Bin')
 if not os.path.isdir(recycledir):
    print("Recycle Bin doesn't exist")
    os.mkdir(recycledir)
 newfullfilename = os.path.join(recycledir, os.path.basename(photo_path))
 os.rename(photo_path, newfullfilename)
 top_text.configure(text="Moved to Recycle Bin")
 next_image()

def createfolder():
 global folderlisttextversion
 global entrytext
 global folderlistrelativepaths
 global alphabet
 global folderlistshortcutalreadyused
 global randomletter
 ccc = os.path.join(path, entrytext.get())
 fulltext = "Created " + ccc
 top_text.configure(text=fulltext)
 os.mkdir(ccc)
 newfold = entrytext.get() 
 folderlistrelativepaths.append(newfold)
 firstlet = newfold[0]
 firstletlow = firstlet.lower()
 if firstletlow not in folderlistshortcutalreadyused:
  folderlistshortcut.append(firstletlow)
 else:
  folderlistshortcut.append(str(alphabet[randomletter]))
  randomletter += 1
  
 folderlisttextversion += str(folderlistshortcut[-1])
 folderlisttextversion += (' : ')
 folderlisttextversion += str(folderlistrelativepaths[-1])
 folderlisttextversion += ('\n')
 button_delete.configure(text=folderlisttextversion) 
 ee.pack_forget()
 button.pack_forget()
 top_frame.focus_set()
 

    

    
 
def keydown(e):
    global changingtime
    global changekey
    global newfoldername
    global folderlisttextversion
    global folderlistshortcutalreadyused
    global entrytext
    global folderlistrelativepaths
    global ee
    global button
    if e.char == "+":
     top_text.configure(text="Creating directory.")
     entrytext = tk.StringVar()
     ee = Entry(tk_root, textvariable = entrytext)
     ee.pack()
     button = tk.Button(tk_root, text="Add folder", command=createfolder)
     button.pack()
     ee.focus_set()
     changingtime = 0
     return 
    if changingtime == 2:
     
     if e.char not in folderlistshortcutalreadyused:
      folderlistshortcut[folderlistshortcut.index(changekey)] = e.char
      top_text.configure(text="Changed.")
     else:
      top_text.configure(text="That shortcut is already used. Hit tab to start over.")
      
     
     
     changingtime = 0
     
    
     folderlisttextversion=''
     itemnumber = 0 
     for itemz in folderlistrelativepaths:
     
      folderlisttextversion += str(folderlistshortcut[itemnumber])
      folderlisttextversion += (' : ')
      folderlisttextversion += str(itemz)
      folderlisttextversion += ('\n')
      itemnumber += 1
    
     button_delete.configure(text=folderlisttextversion) 
     return
    if changingtime == 1:
     if e.char not in folderlistshortcut:
      top_text.configure(text="Sorry this isn't one of the folders.  Press tab to start over")
      return
     changekey = e.char
     changingtime = 2
     top_text.configure(text="You want to change it to which letter?")
     return
    
    numbz = folderlistshortcut.index(e.char)
    newpath = os.path.join(path, folderlistrelativepaths[numbz])
    newfullfilename = os.path.join(newpath, os.path.basename(photo_path))
    os.rename(photo_path, newfullfilename)

    
    try:
     numbz = folderlistshortcut.index(e.char)
     a = os.path.join(path, folderlistrelativepaths[number])
    except:
     pass
    iforget = "Moved " + os.path.basename(photo_path) + " to " + folderlistrelativepaths[numbz]
    top_text.configure(text=iforget)
    next_image()

    

def search(directory):
    global folderlist
    global folderlistrelativepaths
    global folderlistshortcut
    global numericshortcut 
    global folderlistshortcutalreadyused
    global randomletter
    numericshortcut = 0
    randomletter = 0
    folderlist = []
    folderlistrelativepaths =[]
    folderlistshortcut = []
    folderlistshortcutalreadyused = ('')
    which = 0
    list_subfolders_with_paths = [f.path for f in os.scandir(path) if f.is_dir() and not f.name.startswith('.') ]
    for list in list_subfolders_with_paths:
     folderlist += (os.path.split(list)[1])
     folderlistrelativepaths.append(os.path.split(list)[1])
     firstletter = os.path.split(list)[1][0]
     firstletterlow = firstletter.lower()
     if firstletterlow not in folderlistshortcutalreadyused: 
      folderlistshortcut.append(firstletterlow)
      folderlistshortcutalreadyused += firstletterlow
     else:
       folderlistshortcut.append(str(alphabet[randomletter]))
       folderlistshortcutalreadyused += str(alphabet[randomletter])
       randomletter += 1
    global folderlisttextversion
    folderlisttextversion=('')
    itemnumber = 0
    for itemz in folderlistrelativepaths:
     
     folderlisttextversion += str(folderlistshortcut[itemnumber])
     folderlisttextversion += (' : ')
     folderlisttextversion += str(itemz)
     folderlisttextversion += ('\n')
     itemnumber += 1
    global file_count
    for root, subdirs, files in os.walk(directory, topdown=True):
         subdirs.clear()
         for file in files:
            if os.path.splitext(file)[1].lower() in ('.jpg', '.jpeg'):
                img = os.path.join(root, file)
                file_count += 1
                yield img

   


def next_image():
    try:
        global photo_path
        photo_path = next(path_generator)
        photo = ImageTk.PhotoImage(Image.open(photo_path))
        height = int(photo.height() )
        width = int(photo.width())
        if photo.height() > 800:
         photo = ImageTk.PhotoImage(Image.open(photo_path).resize((int(width/2),int(height/2)), Image.ANTIALIAS))
        picture.configure(image=photo)
        picture.image = photo
    except StopIteration:
        picture.configure(image='', text='All done!')


def move_file(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    new_file = directory + 'Picture_{0}.jpg'.format(file_count)
    os.rename(photo_path, new_file)


top_frame = Frame(tk_root)

top_frame.bind("<KeyPress>", keydown)
top_frame.bind("<BackSpace>", backspace)
top_frame.bind("<space>", space)
top_frame.bind("<Escape>", escape)
top_frame.bind("<Tab>", tab)

top_frame.focus_set()

bottom_frame = Frame(tk_root)
right_frame = Frame(tk_root)
top_frame.pack(side='top')
bottom_frame.pack(side='bottom')
right_frame.pack(side='right')
path_generator = search(p)
photo_path = next(path_generator)
photo = ImageTk.PhotoImage(Image.open(photo_path))
picture = tk.Label(tk_root, image=photo)
picture.image = photo
picture.pack(side='left')

top_text = Message(top_frame, text="Hello", width = 300, justify = 'left')
bottom_text = Label(bottom_frame, text="Choose folder shortcut to move file. Backspace = Delete. Spacebar = Skip. Escape = Quit.", justify = 'left', wraplength=900)

button_delete = Message(right_frame, text=folderlisttextversion)

top_text.pack(side='left')
button_delete.pack(side='right')
bottom_text.pack(side='bottom')

tk_root.mainloop()