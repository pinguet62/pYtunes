pYtunes
=======

Read iTunes library file.

* [Using](#using)
  * [Library](#library)
  * [Playlist](#playlist)
  * [Track](#track)
* [Python version](#python-version)

## Using

### Library

To read library:
```python
library = Library("iTunes Music Library.xml")

file = open("iTunes Music Library.xml", "r")
library = Library(file)

file = open("iTunes Music Library.xml", "r")
content = file.read()
library = Library(content)
```

### Playlist

To get the list of playlist names:
```python
print(library.getPlaylistNames()
```

To get the playlist from its name:
```python
playlist = library.getPlaylist(Playlist.Bibliotheque)
playlist = library.getPlaylist(Playlist.SeriesTV)
playlist = library.getPlaylist(Playlist.Podcasts)
playlist = library.getPlaylist(Playlist.Genius)
playlist = library.getPlaylist(Playlist.Memosvocaux)
playlist = library.getPlaylist(Playlist.Musique)
playlist = library.getPlaylist(Playlist.Films)

playlist = library.getPlaylist("Electro")
playlist = library.getPlaylist("Pop")
...
```

To get the informations about a playlist:
```python
print(playlist.name)
print(playlist.playlistID)
print(playlist.playlistPersistentID)
print(playlist.allItems)
print(playlist.smartInfo)
```

To get the tracks of a playlist:
```python
for track in playlist.getTracks():
  pass
```

### Track

To get the informations about a track:
```python
print(track.trackId)
print(track.name)
print(track.artist)
print(track.albumArtist)
print(track.album)
print(track.genre)
print(track.kind)
print(track.size)
print(track.totalTime)
print(track.trackNumber)
print(track.trackCount)
print(track.year)
print(track.dateModified)
print(track.dateAdded)
print(track.bitRate)
print(track.sampleRate)
print(track.comments)
print(track.playCount)
print(track.playDate)
print(track.playDateUTC)
print(track.skipCount)
print(track.skipDate)
print(track.releaseDate)
print(track.rating)
print(track.albumRating)
print(track.albumRatingComputed)
print(track.artworkCount)
print(track.sortAlbum)
print(track.sortName)
print(track.persistentID)
print(track.trackType)
print(track.podcast)
print(track.location)
print(track.fileFolderCount)
print(track.libraryFolderCount)

print(track.rating2)
print(track.location2)
```

## Python version

The [pYtunes.py](pYtunes) module is compatible with the version **3.3**.

But the [compare.py](compare) script require version **2.7**.
