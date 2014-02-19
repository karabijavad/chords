#!/usr/bin/python2.7


#
#
# to do: find out why it says list index out of range
#        when you enter a tonic that is too big (ex:
#        G##). it should print the error text, but it
#        does not.
#

from __future__ import print_function
from musicdefs import MAJORS

class Note(object):

    def __init__(self, rawname, quality=None, symcount=None):
        self.rawname = rawname
        self.quality = quality
        if self.quality != None:
            self.symcount = len(self.quality)
        else:
            self.symcount = 0

        if self.quality == None:
            self.notename = self.rawname
        else:
            self.notename = self.rawname+self.quality

    def flatten(self):
        if "#" in self.notename:
            self.notename = self.notename[:-1]
            self.symcount -= 1
        else:
            self.notename += 'b'
            self.symcount += 1

    def sharpen(self):
        if "b" in self.notename:
            self.notename = self.notename[:-1]
            self.symcount -= 1
        else:
            self.notename += '#'
            self.symcount += 1



class Interval(object):

    def __init__(self, startnote, endnote, direction):
        self.startnote


class Scale(object):

    #might need to initialize variables used to create notes
    #here in this namespace
    def __init__(self, rawnote, scaletype=None):
        self.rawnote = rawnote
        self.notebase = []

        self.scaletype = scaletype
        self.processnote = list(self.rawnote)

        #Create Note object for first scale degree
        if len(self.processnote) == 0 or len(self.processnote) > 2:
            print("ERROR, too long or too short")
        elif len(self.processnote) == 1:
            self.scaledeg_1 = Note(str(self.processnote[0]))
            self.notebase.append(self.scaledeg_1)
        else:
            self.scaledeg_1 = Note(str(self.processnote[0]), str(self.processnote[1]))
            self.notebase.append(self.scaledeg_1)

        ##DEBUG##
        print(self.notebase[0].notename)
        self.notebase[0].flatten()
        print('flattened:', self.notebase[0].notename)
        print('number of symbols:', self.notebase[0].symcount)
        self.notebase[0].sharpen()
        self.notebase[0].sharpen()
        print('sharpened twice now:', self.notebase[0].notename)
        print('number of symbols:', self.notebase[0].symcount)

tonic = raw_input('Enter a tonic: ')
Scale(tonic)
