from pytube import Playlist, YouTube
from pydub import AudioSegment
import os

import re  # Import regular expressions
import yt_dlp

# Function to sanitize filenames
def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def download_video_as_mp3(video_url, output_folder):
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,
        'audioformat': 'mp3',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([video_url])
        except Exception as e:
            print(f"Error downloading {video_url}: {e}")

# Main function to download playlist

# !!! Provide the path of the output folder !!!!
def download_playlist_as_mp3(playlist_url, output_folder="ENTER THE OUTPUT FOLDER HERE"):
    try:

        playlist = Playlist(playlist_url)


        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

    
        for video_url in playlist.video_urls:
            download_video_as_mp3(video_url, output_folder)

        print(f"All videos from the playlist have been downloaded.")
    except Exception as e:
        print(f"Error processing playlist: {e}")



if __name__ == "__main__":
    # Provide the playlist URL here
    playlist_url = "https://www.youtube.com/playlist?list=PLcLtbK8Nf64InyudI1rnYwwRbCr08yup_"
    download_playlist_as_mp3(playlist_url)
