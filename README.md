# Download videos from youtube

<p align="center">
  <img alt="badge" src="https://img.shields.io/badge/author-RogerFernando-191F2B?style=flat-square">
  <img alt="badge" src="https://img.shields.io/badge/license-MIT-191F2B?style=flat-square">
  <img alt="badge" src="https://img.shields.io/badge/version-1.0.0-191F2B?style=flat-square">
</p>

__Project:__ Script written in python to download youtube videos and playlist in a simple and fast way

To assist in the construction of the algorithm, the [Pytube](https://pytube.io/en/latest/) library was used.

## Installing Pytube

You will need [Python](https://www.python.org/) installed on your machine. Then, you can run the scripts below:

```bash
$ pipenv install pytube3
$ pipenv shell
```

## Understanding the algorithm

Operation for video:

```python
# The function takes a parameter in the form of a string
def downloadVideo(VIDEO_URL):
  yt = YouTube(VIDEO_URL)

  # Selects the best available resolution for the video
  video = yt.streams.get_highest_resolution()

  # Start downloading the video
  video.download()
```

Operation for playlist:

```python
# The function takes a parameter in the form of a string
def downloadPlaylist(PLAYLIST_URL):
  playlist = Playlist(PLAYLIST_URL)

  # One iteration happens for each url inside the object
  for url in playlist:
    video = YouTube(url)

    # Selects the best available resolution for the video
    stream = video.streams.get_highest_resolution()

    # Start downloading the video
    stream.download(output_path='playlist')
```

## How to contribute

Contributions are always welcome, no matter how large or small.

1. Fork this repository;
2. Create a branch with your feature: **`git checkout -b my-feature`**;
3. Commit your changes: **`git commit -m 'feat: My new feature'`**;
4. Push to your branch: **`git push origin my-feature`**.

After the merge of your pull request is done, you can delete your branch.

You can report a bug [here](https://github.com/abantes/youtubedownload/issues).

## License

This project is under the MIT license. See the archive [LICENSE](LICENSE.md) for more details.