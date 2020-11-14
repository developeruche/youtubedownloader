try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print(f"Error occured while importing modules {e}")

def download_single_video(): 
    url = input("Enter The full url of the video: ")
    ytd = YouTube(url).streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download("downloads")
    print(ytd)

def download_playlist(): 
    url = input("Enetr The Full url of the Playlist: ")
    playlist = Playlist(url)
    print("Kicking off playlist downloading function...")

    for url_i in playlist.video_urls:
        print(url_i)
        ytd = YouTube(url_i).streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download("downloads/playlists")
        print(ytd)

def application(): 
    print("Welcome nice to hare you here...")
    print("Do you want to Download a playlist of a video?")
    while True:
        choice = input("If playlist Enter p if video enter v ")
        if(choice == "v" or choice == "p"):
            break
        else:
            print("Please Enter a p or v")
    if(choice == "v"):
        download_single_video()
    else:
        download_playlist()
    print("Thank for using this application")

#Calling application function
application()









