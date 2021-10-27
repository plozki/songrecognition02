
import parselmouth
import sounddevice as sd
import wavio
import wave
import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from CONST import *

def testSongs():
    """function that Guy needs to test his user interface"""
    return "sweetchild"


def saveBlob(blob):
    """testing how does blob works and how to use it"""
    
    with open(r"recordings\audio1.wav", "wb") as aud:
        aud_stream = blob.read()
        # print(aud_stream)
        aud.write(aud_stream)
        print("done")
    
       
    with wave.open(r"recordings\audio1.wav", "rb") as audio:
        print(audio.getsampwidth())


def songRecognition():
    sample = [0] * 4
    bokol = True
    nite = [0] *4
    pitcher = 0
    pitchi = 0
    counter = 0
    note = 0
    estring = 329.63
    bstring = 246.94
    gstring = 196.00
    dstring = 146.83
    astring = 110.00
    Estring = 82.41
    absolute_number = 0
    nchannels = 2
    sampwidth = 2
    my_counter = 0

    fs = 44100  # frame rate?

    duration = 2  # seconds

    # myrecording = sd.rec(duration * fs, samplerate=fs, channels=2,dtype='float64')
    # print ("Recording Audio")
    # sd.wait()
    # print ("Play Audio Complete")
    # wavio.write(RECORDINGS_PATH[1], myrecording, fs, sampwidth=2)

    sns.set()  # Use seaborn's default style to make attractive graphs

    # Plot nice figures using Python's "standard" matplotlib library
    snd = parselmouth.Sound(RECORDINGS_PATH[1])

    pitch = snd.to_pitch()
    mean = pitch_values = pitch.selected_array['frequency']

    for i in range(197):
        pitcher = mean[i]
        if (((pitcher - pitchi) > 10) | ((pitchi - pitcher) > 10)) & (pitcher != 0.0):
            # print(pitcher)
            # might
            sample[counter] = pitcher
            counter += 1
            # the PROBLEM#########################################3
            if abs(pitcher - ANIVEATA[counter]) < 10:
                if counter == 3:
                    return "aniveata"
            if abs(pitcher - THUNDERSTRUCK[counter]) < 10:
                if counter == 3:
                    return "thunderstruck"
            if abs(pitcher - LAYLAACOUSTIC[counter]) < 10:
                if counter == 2:
                    return "layla acoustic"

            if abs(pitcher - SWEETCHILDOMINE[counter]) < 10:
                if counter == 3:
                    return "sweetchild"
            if abs(pitcher - SULTANS[counter]) < 10:
                if counter == 1:
                    return "sultans"
            if counter == 3:
                counter = 0

                # work
            pitchi = pitcher

    print(sample)
    print(ANIVEATA)