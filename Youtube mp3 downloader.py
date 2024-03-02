import os
import subprocess
import sys
import time

from github import Github
from pytube import YouTube, Playlist
from win10toast import ToastNotifier

from Variableenviroments import VariableEnviroments

VERSION = VariableEnviroments.VERSION
GITHUB_TOKEN = VariableEnviroments.GITHUB_TOKEN

# for security purposes :)

toaster = ToastNotifier()

if getattr(sys, 'frozen', False):
    absolute_path = os.path.dirname(sys.executable)
    icon_path = os.path.join(sys._MEIPASS, "sanki.ico")
    ffmpeg_path = os.path.join(sys._MEIPASS, "ffmpeg.exe")
elif __file__:
    absolute_path = os.path.dirname(__file__)
    icon_path = "sanki.ico"
    ffmpeg_path = "ffmpeg.exe"

print("Welcome!", end="\n\n")

time.sleep(1)

print("Don't forget to check from time to time my github for updates ;) !", end="\n\n")

try:
    latest_version = Github(GITHUB_TOKEN). \
        get_repo("nicolengo1/Python-youtube-downloader").get_latest_release().title
    if latest_version != VERSION:
        print("New version detected, go to my github and maybe download it :) !")
        print(f"Actual version = {VERSION}   Latest version = {latest_version}", end="\n\n")
except Exception:
    print("An error occured when trying to check for newer versions - ignore")

time.sleep(1)

if not os.path.exists(f"{absolute_path}\\settingsmp3.txt"):

    Download_directory_temp = \
        input("Where do you want to download the audios ? ( Write the full path, you can paste it. "
              "If nothing is provided or the directory does not exist,\n"
              "a folder will be created in the directory where the .exe file is ) - > ")
    if not os.path.exists(Download_directory_temp):
        Download_directory_temp = os.path.join(absolute_path, "audio")

    os.system('cls')

    try:
        Skip_file_verification_temp = \
            int(input("Do you want to check before downloading if the audio was downloaded and it is in the folder ? "
                      "( 0  for no, 1 for yes ) -> "))
        if Skip_file_verification_temp not in [0, 1]:
            Skip_file_verification_temp = 0
    except Exception:
        Skip_file_verification_temp = 0

    os.system('cls')

    try:
        Skip_log_verification_temp = \
            int(input("Do you want to check before downloading if the audio exists in the txt file log ? "
                      "( 0  for no, 1 for yes ) -> "))
        if Skip_log_verification_temp not in [0, 1]:
            Skip_log_verification_temp = 0
    except Exception:
        Skip_log_verification_temp = 0

    os.system('cls')

    try:
        Skip_log_writing_temp = int(input("Do you want to skip writing in the txt log ? "
                                          "( 0  for no, 1 for yes ) -> "))
        if Skip_log_writing_temp not in [0, 1]:
            Skip_log_writing_temp = 0
    except Exception:
        Skip_log_writing_temp = 0

    os.system('cls')

    settings_file = open(f"{absolute_path}\\settingsmp3.txt", "w")
    settings_file.writelines(f"Download_directory = {Download_directory_temp}\n"
                             f"Skip_file_verification = {Skip_file_verification_temp}\n"
                             f"Skip_log_verification = {Skip_log_verification_temp}\n"
                             f"Skip_log_writing = {Skip_log_writing_temp}\n"
                             "Download directory = copy the full path for a folder where to download\n"
                             "Skip_... = 0 for don't skip and 1 for skip\n"
                             "The file verification checks if the audio exists in the folder\n"
                             "The log verification checks if in the txt file exists the audio title\n"
                             "The log writing appends in the txt file the audio title\n"
                             "For the changes to take action a restart of the app is needed,\n"
                             "also the txt file needs to be saved")

    print("Settings file created!", end="\n\n")

    print("All the settings can be changed in the txt settings file where the .exe is.")
    time.sleep(4)

    DOWNLOAD_DIR = Download_directory_temp
    SKIP_FILE_VERIFICATION = Skip_file_verification_temp
    SKIP_LOG_VERIFICATION = Skip_log_verification_temp
    SKIP_LOG_WRITING = Skip_log_writing_temp

    settings_file.close()
else:
    settings_file = open(f"{absolute_path}\\settingsmp3.txt", "r")
    try:
        DOWNLOAD_DIR = settings_file.readline()

        if DOWNLOAD_DIR is not None and DOWNLOAD_DIR != '' and DOWNLOAD_DIR != '\n':
            if DOWNLOAD_DIR[len(DOWNLOAD_DIR) - 1] == '\n':
                DOWNLOAD_DIR = DOWNLOAD_DIR[:-1]
            DOWNLOAD_DIR = DOWNLOAD_DIR[21:]

            if DOWNLOAD_DIR == "None" or DOWNLOAD_DIR is None or not os.path.exists(DOWNLOAD_DIR):
                raise Exception("Download directory does not exist or isn't valid!")
        else:
            raise Exception("Download directory does not exist or isn't valid!")

    except Exception as error:
        print(f"Error - {error}")
        DOWNLOAD_DIR = os.path.join(absolute_path, "audio")

    try:
        SKIP_FILE_VERIFICATION = settings_file.readline()

        if SKIP_FILE_VERIFICATION is not None and SKIP_FILE_VERIFICATION != '' and SKIP_FILE_VERIFICATION != '\n':
            if SKIP_FILE_VERIFICATION[len(SKIP_FILE_VERIFICATION) - 1] == '\n':
                SKIP_FILE_VERIFICATION = SKIP_FILE_VERIFICATION[:-1]
            SKIP_FILE_VERIFICATION = SKIP_FILE_VERIFICATION[25:]

            if SKIP_FILE_VERIFICATION not in ['0', '1']:
                raise Exception("Skip file verification is not 0 or 1!")
            else:
                SKIP_FILE_VERIFICATION = int(SKIP_FILE_VERIFICATION)
        else:
            raise Exception("Skip file verification is not specified!")
    except Exception as error:
        print(f"Error - {error}")
        SKIP_FILE_VERIFICATION = 0

    try:
        SKIP_LOG_VERIFICATION = settings_file.readline()

        if SKIP_LOG_VERIFICATION is not None and SKIP_LOG_VERIFICATION != '' and SKIP_LOG_VERIFICATION != '\n':
            if SKIP_LOG_VERIFICATION[len(SKIP_LOG_VERIFICATION) - 1] == '\n':
                SKIP_LOG_VERIFICATION = SKIP_LOG_VERIFICATION[:-1]
            SKIP_LOG_VERIFICATION = SKIP_LOG_VERIFICATION[24:]

            if SKIP_LOG_VERIFICATION not in ['0', '1']:
                raise Exception("Skip log verification is not 0 or 1!")
            else:
                SKIP_LOG_VERIFICATION = int(SKIP_LOG_VERIFICATION)
        else:
            raise Exception("Skip log verification is not not specified!")

    except Exception as error:
        print(f"Error - {error}")
        SKIP_LOG_VERIFICATION = 0

    try:
        SKIP_LOG_WRITING = settings_file.readline()
        if SKIP_LOG_WRITING is not None and SKIP_LOG_WRITING != '' and SKIP_LOG_WRITING != '\n':
            if SKIP_LOG_WRITING[len(SKIP_LOG_WRITING) - 1] == '\n':
                SKIP_LOG_WRITING = SKIP_LOG_WRITING[:-1]
            SKIP_LOG_WRITING = SKIP_LOG_WRITING[19:]

            if SKIP_LOG_WRITING not in ['0', '1']:
                raise Exception("Skip log verification is not 0 or 1!")
            else:
                SKIP_LOG_WRITING = int(SKIP_LOG_WRITING)
        else:
            raise Exception("Skip log verification is not not specified!")

    except Exception as error:
        print(f"Error - {error}")
        SKIP_LOG_WRITING = 0

    settings_file.close()

DOWNLOAD_DIR_AUDIO_LOG = os.path.join(DOWNLOAD_DIR, "download_log_mp3.txt")

if not os.path.exists(f"{DOWNLOAD_DIR}"):
    os.mkdir(f"{DOWNLOAD_DIR}")

if not os.path.exists(f"{DOWNLOAD_DIR}\\mp3"):
    os.mkdir(f"{DOWNLOAD_DIR}\\mp3")

if not os.path.exists(DOWNLOAD_DIR_AUDIO_LOG):
    log = open(DOWNLOAD_DIR_AUDIO_LOG, "x")
    log.close()


def ReplaceTitle(title):
    """
    Replaces the invalid characters in "title" that cannot be used to name a file in windows.
    :param title: The character string.
    :return: Title with invalid characters erased.
    """
    title_length = len(title)
    i = 0
    while i < title_length:
        if title[i] in '\\/:*?"<>|':
            title = title[:i] + title[i + 1:]
            title_length = title_length - 1
        else:
            i = i + 1

    return title


def SuccessfulNotification():
    """
    Shows a notification in windows sidebar when the download is complete.
    :return: None
    """
    try:
        print('')
        os.chdir(absolute_path)

        print("All audios were downloaded \n")
        toaster.show_toast("YouTube Downloader", "All videos were downloaded!", duration=0,
                           icon_path=icon_path)
        time.sleep(2)

        os.system('cls')
    except Exception:
        pass


def DownloadMP3FromYouTube(video_url, folder_name="random", modify_volume=0):
    """
    Downloads the highest mp3 quality file from a YouTube video link and puts it in a "folder_name" folder.
    :param video_url: The YouTube video url.
    :param folder_name: The folder in which the audio will be downloaded ( if it's a single audio, the folder will
    :param modify_volume: increase or lower the volume in DB
    be named "random", if it's a playlist, the folder will be named the playlist title ). The folder will be created in
    the "DOWNLOAD_DIR" path.
    :return:
    """
    i = 1
    while i < 10:
        try:
            audio_video_youtube = YouTube(
                video_url).streams.filter(
                progressive=False).filter(only_audio=True).get_audio_only()
        except Exception:
            i = i + 1
            continue
        break

    # audio_video_youtube = YouTube(video_url).streams.filter().filter(only_audio=True).first()

    if audio_video_youtube is not None:
        audio_title = ReplaceTitle(audio_video_youtube.title)
        print(audio_title)

        if not os.path.exists(f"{DOWNLOAD_DIR}\\mp3\\{folder_name}"):
            os.mkdir(f"{DOWNLOAD_DIR}\\mp3\\{folder_name}")

        if SKIP_FILE_VERIFICATION == 0:
            os.chdir(f"{DOWNLOAD_DIR}\\mp3\\{folder_name}")

            if f"{audio_title}.mp3" in os.listdir():
                raise Exception("The audio was already downloaded ( it is in the folder )")

        download_log = open(DOWNLOAD_DIR_AUDIO_LOG, "r", encoding="UTF-8")

        not_in_log = 0

        if SKIP_LOG_VERIFICATION == 0:
            for lines in download_log:
                if lines[:-1] == audio_title:
                    download_log.close()
                    raise Exception("The audio was already downloaded ( it is in the log )")

            not_in_log = 1

        download_log.close()

        audio_video_youtube.download(f"{DOWNLOAD_DIR}\\mp3\\{folder_name}", filename=f"{audio_title}.mp4")

        subprocess.call(
            [f"{ffmpeg_path}", "-y", "-i", f"{DOWNLOAD_DIR}\\mp3\\{folder_name}\\{audio_title}.mp4", "-filter:a",
             f"volume={modify_volume}dB", "-c:a",
             "libmp3lame", "-b:a", "256k", f"{DOWNLOAD_DIR}\\mp3\\{folder_name}\\{audio_title}.mp3"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT
        )

        os.remove(f"{DOWNLOAD_DIR}\\mp3\\{folder_name}\\{audio_title}.mp4")

        if not_in_log == 1 and SKIP_LOG_WRITING == 0:
            download_log = open(DOWNLOAD_DIR_AUDIO_LOG, "a", encoding="UTF-8")
            download_log.write(f"{audio_title}\n")
            download_log.close()

        print("Audio downloaded succesfully")

    else:
        raise Exception("The link is not valid!")


while True:
    url_to_download = input(
        "Write the link of the playlist or video ( to exit press only the enter key ) -> ")
    print('')

    if url_to_download != '':
        if "watch" in url_to_download or "short" in url_to_download:

            try:
                DownloadMP3FromYouTube(url_to_download)
            except Exception as error:
                print(f"Error - {error}")
            else:
                SuccessfulNotification()

            print('')

        elif "playlist" in url_to_download:
            try:
                playlist = Playlist(url_to_download)
                playlist_title = ReplaceTitle(playlist.title)

                start_or_end = int(input(
                    "Do you want to download the videos starting from the start or the end? ( 1 or 0 ) -> "))
                print('')

                if start_or_end == 1:
                    for video_url in playlist.video_urls:
                        try:
                            DownloadMP3FromYouTube(video_url, playlist_title)
                        except Exception as error:
                            print(f"Error - {error}")

                        print('')

                elif start_or_end == 0:
                    playlist_length = len(playlist) - 1

                    for i in range(playlist_length, 0, -1):
                        try:
                            video_url = playlist[i]
                            DownloadMP3FromYouTube(video_url, playlist_title)
                        except Exception as error:
                            print(f"Error - {error}")

                        print('')

            except Exception as error:
                print(f"Error - {error}")

            else:
                SuccessfulNotification()

        else:
            print("The link is not valid!")

    elif url_to_download == '':
        print("Bye bye :)")
        time.sleep(3)
        break
