#!/usr/bin/python2.7
from __future__ import print_function
from musicdefs import MAJORS

CYCLE_OF_FIFTHS = {
        'C#' : 0,
        'F#' : 1,
        'B'  : 2,
        'E'  : 3,
        'A'  : 4,
        'D'  : 5,
        'G'  : 6,
        'C'  : 7,
        'F'  : 8,
        'Bb' : 9,
        'Eb' : 10,
        'Ab' : 11,
        'Db' : 12,
        'Gb' : 13,
        'Cb' : 14,
        }

CHROMATIC_SCALE = {
        'C'  : 0,
        'C#' : 1,
        'Db' : 1,
        'D'  : 2,
        'D#' : 3,
        'Eb' : 3,
        'E'  : 4,
        'Fb' : 4,
        'E#' : 5,
        'F'  : 5,
        'F#' : 6,
        'Gb' : 6,
        'G'  : 7,
        'G#' : 8,
        'Ab' : 8,
        'A'  : 9,
        'A#' : 10,
        'Bb' : 10,
        'B'  : 11,
        'Cb' : 11,
        'B#' : 0,
        'C'  : 0,
        }

SHARPS = (
        'A', 'A#', 'B', 'B#', 'C', 'C#', 'D', 'D#', 'E', 'E#', 'F', 'F#', 'G', 'G#'
)

class Note(object):

    def __init__(self, tonic, quality=None, symcount=None):
        self.tonic = tonic
        self.quality = quality
        self.symcount = symcount

class Interval(object):

    def __init__(self): pass


class Scale(object):

    #might need to initialize variables used to create notes
    #here in this namespace
    def __init__(self, rawnote, scaletype=None):
        self.rawnote = rawnote
        self.notebase = []
        self.scaletype = scaletype
        self.processnote = list(self.rawnote)

        if len(self.processnote) == 0 or len(self.processnote) > 2:
            print("ERROR, too long or too short")
        elif len(self.processnote) == 1:
            self.scaledeg_1 = Note(self.processnote)
            self.notebase.append(self.scaledeg_1)
        else:
            self.scaledeg_1 = Note(self.processnote[0], self.processnote[1])
            self.notebase.append(self.scaledeg_1)

        print(self.notebase[0].tonic)

tonic = raw_input('Enter a tonic: ')
Scale(tonic)
