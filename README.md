
# Welcome to my Python youtube downloader!
This is my first app made in Python so yeah, don't expect it to do a **backflip** or something :) .

# Disclaimer
**This app is not a virus**, windows detects it as a virus because **it creates a .exe file in the temp folder**. That file is **ffmpeg.exe**, which **i use to convert and merge mp3 and mp4 files**. You can search ffmpeg on google to see yourself that it is not a virus. 

## Supported OS
- Windows
- Just windows, i haven't tried it on other OS

# How to use it

First, download the **desired .exe** in the **dist folder** ( for **mp3** or **mp4** ), and then just run it ( your windows **may detect** it as a **virus** because it is a **python script, but don't worry, it is safe**, on god ) . A cmd will open and **instructions will be given** on how to use it. Really simple.

## How does it work

It takes a **link** for a **YouTube video/playlist**, if it is a video, it takes the **highest quality mp3** and downloads it in the specified folder, then, if you are using the mp4 downloader, it downloads the **highest quality audio-less mp4** too ( audio-less for higher quality, ask YouTube why is this, not me ) , and merges both together.

>If you are a programmer, you can look at the code, really simple, no virus or anything. Tried my best :)
>May improve later.

# Want to test and contribute? ( for programmers )
Download the .py , the ffmpeg.exe and the sanki.ico files, put them together in a folder, download the needed libraries for python and you're good to go.
> Libraries used:
> - win10toast
> - pytube
> - time
> - sys
> - subprocess
> - os
