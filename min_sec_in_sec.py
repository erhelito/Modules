#!/usr/bin/python3.8
# -*-coding:Utf-8 -*

def minutes_in_sec (time):
    """This module allows you to convert minutes in seconds, by putting time at the format : min.sec"""
    minutes = int(time)
    seconds = time - minutes
    minutes *= 60
    seconds *= 100
    minutes_in_sec = seconds + minutes
    return minutes_in_sec
