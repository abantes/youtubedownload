from pytube import YouTube, Playlist

# Playlist
def downloadPlaylist(PLAYLIST_URL):
  playlist = Playlist(PLAYLIST_URL)

  for url in playlist:
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path='playlist')

# Video
def downloadVideo(VIDEO_URL):
  yt = YouTube(VIDEO_URL)

  video = yt.streams.get_highest_resolution()
  video.download()

PLAYLIST_LINK = 'https://www.youtube.com/playlist?list=PL3umV5a_a3P2q31HSu3iSOd-cfQ-z3uFw'
VIDEO_LINK = 'https://www.youtube.com/watch?v=LMgppobOpQA'

# downloadVideo(VIDEO_LINK)
# downloadPlaylist(PLAYLIST_LINK)
