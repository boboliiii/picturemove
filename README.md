# picturemove
moves pictures to subfolders using keyboard shortcuts to save time.

Picturemove 1.0

Installation
If you are running the .exe file on windows, no need to install, just double-click the .exe.
If you are running the Python 3 script, run it in python (probably by typing “py picturemove.py”).  You need to install the dependencies first, the program uses tkinter and pil.  To install these dependencies, type “pip install tkinter” and “pip install pil”.

Usage
Picturemove is a program to help speed up the process of sorting out masses of pictures, by moving them into different directories.  It uses keyboard shortcuts to move photos one at a time into folders of your choice, without using the mouse or any extra prompts that would slow you down.  It can only move the pictures into folders located inside your photo folder, so keep that in mind.

When you open Picturemove it will ask you for the folder that contains the pictures.  Ideally you have subfolders within that folder with categories of where you want the photos to go.  For example,
C:\Pictures has a bunch of photos in it, and also the folders C:\Pictures\Cats and C:\Pictures\Dogs.  Even if there is no subfolders in the picture folder, you can create them in the program.

The program automatically assigns keyboard shortcuts to every folder, for example, Cats folder will probably get the shortcut c.  This means when you see a picture of a cat, just press c, and the picture will be moved to that folder.

Simple as that.  Other keyboard shortcuts:
TAB button renames shortcuts, let’s say if you wanted to change Cats folder shortcut to a different letter other than c.
+ button creates a new folder you can move stuff to.
BACKSPACE button deletes the current photo.
SPACEBAR skips to the next photo.
ESCAPE quits the program.

There also is a way you can use this program to rename files:  once you are done sorting them into directories that make sense to you, you can go into each directory, select all the files, and right click on the first one and choose rename:  all the files in the directory will have that name with a number at the end.  This is a way to change the filenames to something useful, in case you want to take them out o the directory and for them to be named in a better way.
