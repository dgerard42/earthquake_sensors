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

# def find_fastest_wave(waves):

# def find_largest_wave(waves):

def make_waves(displacements): #make a 3d array of waves with wave size, wave time, and wave acceleration
    new_wave = -1
    time = 0.0
    size = 0.0
    sign = (displacements[0] < 0) ? false : true #true is positive, false is negative
    for i in range(len(displacements)):
        time += 0.01
        size += displacements[i]
        if (new_wave == 2)
            
        elif (displacements[i] < 0 && sign == true || displacements[i] > 0 && sign == false)
            sign = (sign == true) ? false : true
            new_wave += 1

def split_by_direction(eq_file): #make 3 subarrays of the displacements for each direction
    displacements = [[], [], []]
    for line in eq_file:
        if line[0].isdigit():
            items = line.split()
            displacements[direction].append(float(items[1]))
        else:
            if line.find("HHE") != -1:
                direction = 0
            elif line.find("HHN") != -1:
                direction = 1
            elif line.find("HHZ") != -1:
                direction = 2
    return displacements

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
        displacements = split_by_direction(eq_file)
        waves = [[],[],[]]
        for direction in displacements
            waves[direction] = make_waves[displacements[direction]]
    else:
       print ("enter the name of the earthquake data file that you wish to parse")
       return 0

main()
