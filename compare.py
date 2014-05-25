#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Analyse the iTunes library and check if:
    - the track location exists
    - the rating is the same that ID3 file
    - the tags are empty: "Comments", "Composer", "Album Artist"
Compare the rating of music from iTune library and Windows.
"""


__author__ = __maintainer__ = "Pinguet62"
__date__ = "2014/05/18"
__email__ = "pinguet62@gmail.com"
__license__ = "Creative Commons, Attribution NonCommercial ShareAlike, 4.0"
__status__ = "Development"
__version__ = "1.0"


import argparse
import os
import sys

import mutagen.id3

import pYtunes


def main():
    # ----- argparse -----
    parser = argparse.ArgumentParser()
    parser.add_argument("file",
                        help="the iTunes library",
                        type=argparse.FileType("r"))
    parser.add_argument("--version",
                        action="version",
                        version="%(prog)s " + __version__)
    args = parser.parse_args()
    
    # ----- run -----
    library = pYtunes.Library(args.file)
    for track in library.getTracks():
    	# Location
    	location = track.location2
    	stdoutLocation = location.encode(sys.stdout.encoding, "replace")
    	if not os.path.exists(location):
    		print("Invalid location: " + stdoutLocation)
    		continue
    	
        # Emtpy tags
        if track.albumArtist not in [None, ""]: print("Album Artist not empty: " + stdoutLocation)
    	if track.comments not in [None, ""]: print("Comments not empty: " + stdoutLocation)
        if track.composer not in [None, ""]: print("Composer not empty: " + stdoutLocation)
    	
    	# Rating
#     	iTunesRating = track.rating2
#         try:
#             id3Rating = [int(line[-6:-4]) for line in mutagen.id3.ID3(location).pprint().split("\n") if line[:4] == "POPM"]
#             id3Rating = id3Rating[0] if len(id3Rating) > 0 else 0
#             id3Rating = {0:0, 1:1, 64:2, 28:3, 96:4, 55:5}[id3Rating]
#             if iTunesRating != id3Rating: print("Rating not match: " + stdoutLocation)
#         except: pass


if __name__ == '__main__':
    main()
