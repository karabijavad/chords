#!/usr/bin/python2.7
from __future__ import print_function
from operator import itemgetter

chromatic = ('A', 'Bb',
             'B', 'C',
             'Db', 'D',
             'Eb', 'E',
             'F', 'Gb',
             'G', 'Ab')


chroma = { "A" : "A",
           "A#" : "A#/Bb",
           "Bb" : "A#/Bb",
           "B" : "B",
           "C" : "C",
           "C#" : "C#/Db",
           "Db" : "C#/Db",
           "D" : "D",
           "D#" : "D#/Eb",
           "Eb" : "D#/Eb",
           "E" : "E",
           "F" : "F",
           "F#" : "F#/Gb",
           "Gb" : "F#/Gb",
           "G" : "G",
           "G#" : "G#/Ab",
           "Ab" : "G#/Ab"
           }

print(chroma)


class Scale(object):

    def __init__(self, tonic, scaletype):
        self.tonic = tonic
        self.scaletype = scaletype

    


def get_major(tonic):

    for note in chromatic:
        if tonic == note:
            root = chromatic.index(tonic)
            if root+4 > 11:
                third = root+4-12
                fifth = root+7-12
            elif root+4 >= 5 and root+4 <= 11:
                third = root+4
                fifth = root+7-12
            else:
                third = root+4
                fifth = root+7
            chord = c_tonic, c_third, c_fifth = itemgetter(root,third,fifth)(chromatic)
            print(chord)
            return chord

def inversions(src_chord):
    root_pos = list(src_chord)
    order_first = [1,2,0]
    order_second = [2,0,1]
    first_inv = [ root_pos[i] for i in order_first ]
    second_inv = [ root_pos[i] for i in order_second ]
    print("Root position:", root_pos)
    print("First inversion:", first_inv)
    print("Second inversion:", second_inv)


while 1:
    chosen_root = raw_input("Choose a tonic for a major triad: ")
    #get_major(chosen_root)
    inversions(get_major(chosen_root))

