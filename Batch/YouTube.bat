@echo off
ECHO Welcome to YouTube Video Downloader batch file version.
ECHO Version 0.3
ECHO more features will come.


set /p input_string=Enter URL of YouTube Video: 

youtube-dl -f bestvideo+bestaudio %input_string%



pause 

rem this is YouTube Video Downloader by ljh.(CLI ver.)
rem you can use or copy, modify this file whenever you want.
rem P.S: This file use youtube-dl, so you should install python and install youtube-dl library to use this program.
rem https://www.python.org/downloads
rem command for install youtube-dl: python -m pip install youtube-dl
rem *this is the way to comment
