#!/usr/bin/python3
import ctypes
import sys
from time import time as timestamp
from resource import getrusage as resource_usage, RUSAGE_SELF


def unix_time(function):

    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    function()
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()

    return "\nreal: {}\nuser: {}\nsys: {}".format(
        end_time - start_time,
        end_resources.ru_utime - start_resources.ru_utime,
        end_resources.ru_stime - start_resources.ru_stime)


def print_factors():
    fun = ctypes.CDLL("./lib_factors_functions.so")
    fun.trial_division.argtypes = [ctypes.c_long]
    with open(sys.argv[1], 'r') as prime:
        line = prime.readline()
        while line != '':
            n = int(line)
            fun.trial_division(n)
            line = prime.readline()
