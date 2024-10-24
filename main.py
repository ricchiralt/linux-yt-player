import re
import subprocess
import sys

def is_valid_youtube_url(url):
    youtube_regex = re.compile(
        r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+$')
    return youtube_regex.match(url)

def main():
    url = input("Please enter the YouTube URL:").strip()
    
    if not url or not is_valid_youtube_url(url):
        print("Invalid or unprovided URL. Exiting script.")
        sys.exit(1)    
    
    command = f"yt-dlp -q -o - {url} | mpv --no-video -"
    
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("Error executing command.")
        sys.exit(1)

if __name__ == "__main__":
    main()
