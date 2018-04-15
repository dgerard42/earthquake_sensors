# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    biggest_wave.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: daniella <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/04/10 16:34:56 by daniella          #+#    #+#              #
#    Updated: 2018/04/10 16:35:01 by daniella         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/python3
import sys
import os

# def find_fastest_wave(wave_sets):

# def find_largest_wave(wave_sets):

def make_waves(deltas): #make a 3d array of waves with wave size, wave time, and wave acceleration
    new_wave = -1 # -1 == wave just started, 0 == one sign change, 1 == 2 sign changes
    time = 0.0
    size = 0.0
    sign = False if (deltas[0] < 0) else True #True is positive, False is negative
    waves = []
    # print("len delatas =", len(deltas))
    for i in range(len(deltas)):
        # print("new wave val=", new_wave)
        if (new_wave == 1):
            # print("making new wave")
            waves.append([[time], [size], [(size * 100 / time * 100)]]) #last num in array is avg. speed during wave in meters per second
            time = 0.0
            size = 0.0
            new_wave = -1
            # sign = False if (deltas[i] < 0) else True #True is positive, False is negative
        elif i < (len(deltas) - 1):
            if deltas[i + 1] < 0 and sign == True or deltas[i + 1] > 0 and sign == False:
                sign = False if (sign == True) else True
                new_wave += 1
                # print ("here")
        elif i == len(deltas):
            sign = False if (sign == True) else True
            new_wave += 1
        time += 0.01
        size += abs(deltas[i])
    # print (waves)
    return waves

def split_by_direction(eq_file): #make 3 subarrays of the displacements for each direction
    deltas = [[], [], []]
    for line in eq_file:
        if line[0].isdigit():
            items = line.split()
            deltas[direction].append(float(items[1]))
        else:
            if line.find("HHE") != -1:
                direction = 0
            elif line.find("HHN") != -1:
                direction = 1
            elif line.find("HHZ") != -1:
                direction = 2
    return deltas

def open_file(filename):
    try:
        eq_file = open(filename)
    except:
        return 0
    return eq_file

def main():
    if (len(sys.argv) > 1):
        eq_file = open_file(sys.argv[1])
        if (eq_file == 0):
           print ("file '"+filename+"' not found")
           return 0
        deltas = split_by_direction(eq_file)
        # print (deltas)
        wave_sets = []
        for direction in range(len(deltas)):
            wave_sets.append(make_waves(deltas[direction]))
        print (wave_sets)
    else:
       print ("enter the name of the earthquake data file that you wish to parse")
       return 0

main()
