#!/usr/bin/python2.7

MAJORS = {
        'Cb' : 'Cb Db Eb Fb Gb Ab Bb',
        'C'  : 'C D E F G A B',
        'C#' : 'C# D# E# F# G# A# B#',
        'Db' : 'Db Eb F Gb Ab Bb C',
        'D'  : 'D E F# G A B C#',
        'D#' : 'D# E# F## G# A# B# C#',
        'Eb' : 'Eb F G Ab Bb C D',
        'E'  : 'E F# G# A B C# D#',
        'E#' : 'E# F## G## A# B# C## D##',
        'Fb' : 'Fb Gb Ab Bbb Cb Db Eb Fb',
        'F'  : 'F G A Bb C D E',
        'F#' : 'F# G# A# B C# D# E#',
        'Gb' : 'Gb Ab Bb Cb Db Eb F',
        'G'  : 'G A B C D E F#',
        'G#' : 'G# A# B# C# D# E# F##',
        'Ab' : 'Ab Bb C Db Eb F G',
        'A'  : 'A B C# D E F# G#',
        'A#' : 'A# B# C## D# E# F## G##',
        'Bb' : 'Bb C D Eb F G A',
        'B'  : 'B C# D# E F# G# A#',
        'B#' : 'B# C## D## E# F## G## A##'
        }

CYCLE_OF_FIFTHS = {
        'C#' : 0, #SHARPS
        'F#' : 1, #  |
        'B'  : 2, #  |
        'E'  : 3, #  |
        'A'  : 4, #  |
        'D'  : 5, #  |
        'G'  : 6, #  |
        'C'  : 7, #NEUTRAL POINT
        'F'  : 8, #  |
        'Bb' : 9, #  |
        'Eb' : 10,#  |
        'Ab' : 11,#  |
        'Db' : 12,#  |
        'Gb' : 13,#  |
        'Cb' : 14,#FLATS
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
        'A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#'
)

FLATS = (
        'A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab'
)

#SCALES =
