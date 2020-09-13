import sys
import os
from itertools import product
sys.path.insert(1, os.path.dirname(os.getcwd()))
from aoc_functions import intcode_machine

with open('input') as f:
    inp = list(map(int, f.read().split(',')))

n = 50
comps = [intcode_machine(inp, [i, -1]) for i in range(n)]

def packets_to_send():
    packets = []
    for i in range(n):
        while True:
            try:
                _, output = comps[i].run_till_output_or_halt()
                packets.append(output)
            except IndexError:
                break
    return [[packets[k+i] for i in range(3)] for k in range(0, len(packets), 3)]

def send_packets(ps):
    for p in ps:
        comps[p[0]].add_inputs([p[1], p[2]])

# Part 1 and 2
comps = [intcode_machine(inp, [i, -1]) for i in range(n)]

break_var = False
nat_packet = None
last_nat_packet = None
first_time = True

while True:
    packets = packets_to_send()
    if not packets:
        if nat_packet == last_nat_packet and nat_packet:
            print(nat_packet[1])
            break_var = True
        comps[0].add_inputs(nat_packet)
        last_nat_packet = nat_packet
        nat_packet = None
    else:
        for p in packets:
            if p[0] == 255:
                if first_time:
                    print(p[2])
                    first_time = False
                nat_packet = p[1:3]
        packets = [p for p in packets if p[0] != 255]
        send_packets(packets)
    if break_var:
        break