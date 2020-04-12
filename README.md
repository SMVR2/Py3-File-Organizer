# Py-File-Organizer

Have you ever had the issue where your downloads folder is a mess with pictures, executables, and all sorts of other stuff?
Well this handy file organizer fixes it for you. I spent some time looking for a good file organizer, and eventually found a pretty simple one I liked made by  Noelia Sales Montes. Her script was in Python 2, so I converted it to Python3, and voila a working script to organize all your files. Things that I am now working on is divirging from the original script and adding some new features like some sort of file watcher that will move files the moment the reach the folder.

#Installation and Usage

First download organize.py from the repo, then take that file and put it in your desired folder. Then start replacing the file extensions given, and change the folder paths to what is desired. After that run the file. I mostly prefer to run it via ```python3 organize.py``` but you do have a couple more options to execute.

#Flags
  * -v -> enable verbose mode
  * -h o --help
  * -s o --secure -> copy files
  * -f o --force -> force the movement of files
                    If file already exists, it is deleted
                   
   Run the script with any of these flags if you must.

The script has been tested on Ubuntu Linux 18.04, I have not tried on Windows yet but I think that it would work fine on windows, just have to replace the paths with the typical windows file path format.
