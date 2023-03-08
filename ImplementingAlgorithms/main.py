import time
import random
from rabin import Rabin_Karp_Matcher
from BruteForce import BruteForce
from kmp import KMP
from Sunday import sunday_find
from Fsm import fsm

def timing(text, pattern):
    text_length = len(text)
    increment = 100
    lengths = tuple(range(0, text_length, increment))

    sunday_result = []
    for length in lengths:
        start = time.perf_counter_ns()
        sunday_find(text[:length], pattern)
        duration = time.perf_counter_ns() - start
        sunday_result.append(duration)

    bruteforce_result = []
    for length in lengths:
        start = time.perf_counter_ns()
        BruteForce(text[:length], pattern)
        duration = time.perf_counter_ns() - start
        bruteforce_result.append(duration)

    kmp_result = []
    for length in lengths:
        start = time.perf_counter_ns()
        KMP(text[:length], pattern)
        duration = time.perf_counter_ns() - start
        kmp_result.append(duration)

    fsm_result = []
    for length in lengths:
        start = time.perf_counter_ns()
        fsm(text[:length], pattern)
        duration = time.perf_counter_ns() - start
        fsm_result.append(duration)

    rabin_karp_result = []
    for length in lengths:
        start = time.perf_counter_ns()
        Rabin_Karp_Matcher(text[:length], pattern)
        duration = time.perf_counter_ns() - start
        rabin_karp_result.append(duration)


    print(" Text size | Brute-Force RT |  Sunday RT  |   KMP RT   |   FSM RT   | Rabin Karp RT | - (RT: Running Time)")
    for it, length in enumerate(lengths):
        print(
                "% 11d" % length,
                "% 16d" % bruteforce_result[it],
                "% 13d" % sunday_result[it],
                "% 12d" % kmp_result[it],
                "% 12d" % fsm_result[it],
                "% 15d" % rabin_karp_result[it]
                )



with open("python.txt") as textfile:
    timing(textfile.read(), 'is')
