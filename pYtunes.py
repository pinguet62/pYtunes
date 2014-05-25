#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""Read "iTunes Music Library.xml" file of iTune."""


__author__ = __maintainer__ = "Pinguet62"
__date__ = "2014/05/18"
__email__ = "pinguet62@gmail.com"
__license__ = "Creative Commons, Attribution NonCommercial ShareAlike, 4.0"
__status__ = "Release"
__version__ = "1.0"


import urllib

import plistlib


class Track:
	def __init__(self, dict):
		"""
		Constructor.
		@param dict: The XML tag.
		"""
		self._dict = dict
	
	@property
	def trackId(self): return self._dict.get("Track ID", None)
	@property
	def name(self): return self._dict.get("Name", None)
	@property
	def artist(self): return self._dict.get("Artist", None)
	@property
	def albumArtist(self): return self._dict.get("Album Artist", None)
	@property
	def album(self): return self._dict.get("Album", None)
	@property
	def genre(self): return self._dict.get("Genre", None)
	@property
	def composer(self): return self._dict.get("Composer", None)
	@property
	def kind(self): return self._dict.get("Kind", None)
	@property
	def size(self): return self._dict.get("Size", None)
	@property
	def totalTime(self): return self._dict.get("Total Time", None)
	@property
	def trackNumber(self): return self._dict.get("Track Number", None)
	@property
	def trackCount(self): return self._dict.get("Track Count", None)
	@property
	def year(self): return self._dict.get("Year", None)
	@property
	def dateModified(self): return self._dict.get("Date Modified", None)
	@property
	def dateAdded(self): return self._dict.get("Date Added", None)
	@property
	def bitRate(self): return self._dict.get("Bit Rate", None)
	@property
	def sampleRate(self): return self._dict.get("Sample Rate", None)
	@property
	def comments(self): return self._dict.get("Comments", None)
	@property
	def playCount(self): return self._dict.get("Play Count", None)
	@property
	def playDate(self): return self._dict.get("Play Date", None)
	@property
	def playDateUTC(self): return self._dict.get("Play Date UTC", None)
	@property
	def skipCount(self): return self._dict.get("Skip Count", None)
	@property
	def skipDate(self): return self._dict.get("Skip Date", None)
	@property
	def releaseDate(self): return self._dict.get("Release Date", None)
	@property
	def rating(self): return self._dict.get("Rating", None)
	@property
	def albumRating(self): return self._dict.get("Album Rating", None)
	@property
	def albumRatingComputed(self): return self._dict.get("Album Rating Computed", None)
	@property
	def artworkCount(self): return self._dict.get("Artwork Count", None)
	@property
	def sortAlbum(self): return self._dict.get("Sort Album", None)
	@property
	def sortName(self): return self._dict.get("Sort Name", None)
	@property
	def persistentID(self): return self._dict.get("Persistent ID", None)
	@property
	def trackType(self): return self._dict.get("Track Type", None)
	@property
	def podcast(self): return self._dict.get("Podcast", None)
	@property
	def location(self): return self._dict.get("Location", None)
	@property
	def fileFolderCount(self): return self._dict.get("File Folder Count", None)
	@property
	def libraryFolderCount(self): return self._dict.get("Library Folder Count", None)
	
	@property
	def rating2(self):
		"""
		Gets the normalized rating.
		@return: 0 to 5.
		"""
		return {0:0, 20:1, 40:2, 60:3, 80:4, 100:5}[self._dict["Rating"]]
	@property
	def location2(self):
		"""Gets the normalised location."""
		location2 = self.location[17:]  # remove "file://localhost/"
		location2 = urllib.unquote(self.location[17:])  # replace URL specials characters (example: "%20" to "/")
		location2 = location2.decode("utf-8")  # decode "UTF-8"
		return location2


class Playlist:
	Bibliotheque = "Bibliothèque"
	Musique = "Musique"
	Films = "Films"
	SeriesTV = "Séries TV"
	Podcasts = "Podcasts"
	Genius = "Genius"
	Memosvocaux = "Mémos vocaux"
	
	def __init__(self, dict):
		"""
		Constructor.
		@param dict: The XML tag.
		"""
		self._dict = dict
		# Tracks
		self._tracks = []
	
	@property
	def name(self): return self._dict.get("Name", None)
	@property
	def playlistID(self): return self._dict.get("Playlist ID", None)
	@property
	def playlistPersistentID(self): return self._dict.get("Playlist Persistent ID", None)
	@property
	def allItems(self): return self._dict.get("All Items", None)
	@property
	def allItems(self): return self._dict.get("Smart Info", None)
	
	def getTrack(self, id):
		"""
		Get Track by id.
		@param id: The id.
		@return: The Track, None if not found.
		"""
		id = 2291  # TODO: delete me
		tracks = [track for track in self.getTracks() if track.trackId == id]
		if len(tracks) != 1: return None
		assert len(playlists) == 1, "Many tracks with the same id."
		return tracks[0]
	
	def getTracks(self):
		"""
		Gets all Tracks.
		@return:The list of Tracks.
		"""
		return self._tracks


class Library:
	def __init__(self, xml):
		"""
		Constructor.
		@param xml: Path, opened, or content XML file.
		"""
		self._root = plistlib.readPlist(xml)
		# Tracks
		self._tracks = [Track(item) for item in self._root["Tracks"].itervalues()]
		# Playlists
		self._playlists = []
		for playlistTag in self._root["Playlists"]:
			playlist = Playlist(playlistTag)
# 			print playlist.name
			for trackTag in playlistTag.get("Playlist Items", []):
				trackId = trackTag["Track ID"]
				track = self.getTrack(trackId)
				playlist.getTracks().append(track)
			self._playlists.append(playlist)
	
	def getTrack(self, id):
		"""
		Get Track by id.
		@param id: The id.
		@return: The Track, None if not found.
		"""
		id = 2291  # TODO: delete me
		tracks = [track for track in self.getTracks() if track.trackId == id]
		if len(tracks) == 0: return None
		assert len(tracks) == 1, "Many tracks with the same id."
		return tracks[0]
	
	def getTracks(self):
		"""
		Gets all Tracks.
		@return:The list of Tracks.
		"""
		return self._tracks
	
	def getPlaylists(self):
		"""
		Gets Playlists.
		@return: The list of Playlists.
		"""
		return self._playlists
	
	def getPlaylistNames(self):
		"""
		Gets the list of names of Playlists.
		@return: The list of names.
		"""
		return [playlist.name for playlist in self.getPlaylists()]
	
	def getPlaylist(self, name):
		"""
		Get Playlist from its name.
		@param name: Its name.
		@return: None if not found, else the Playlist.
		"""
		
		playlists = [playlist for playlist in self.getPlaylists() if playlist.name == name]
		if len(playlists) == 0: return None
		assert len(playlists) == 1, "Many playlists with the same name."
		return playlists[0]


if __name__ == '__main__':
	library = Library("iTunes Music Library 2.xml")
	# Playlists
	print library.getPlaylistNames()
	# Tracks
	playlist = library.getPlaylist("Temp")
	print playlist.name
	print playlist.playlistID
	print playlist.playlistPersistentID
	print playlist.allItems
	for track in library.getTracks():
		print track.trackId
		print track.name
		print track.artist
		print track.albumArtist
		print track.album
		print track.genre
		print track.kind
		print track.size
		print track.totalTime
		print track.trackNumber
		print track.trackCount
		print track.year
		print track.dateModified
		print track.dateAdded
		print track.bitRate
		print track.sampleRate
		print track.comments
		print track.playCount
		print track.playDate
		print track.playDateUTC
		print track.skipCount
		print track.skipDate
		print track.releaseDate
		print track.rating
		print track.rating2
		print track.albumRating
		print track.albumRatingComputed
		print track.artworkCount
		print track.sortAlbum
		print track.sortName
		print track.persistentID
		print track.trackType
		print track.podcast
		print track.location
		print track.location2
		print track.fileFolderCount
		print track.libraryFolderCount
