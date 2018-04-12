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
    #iterate through the waves
# def find_largest_wave(waves):

# def make_waves(): #make a data frame of waves with wave size, wave time, and wave acceleration

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
        print (displacements)
    else:
       print ("enter the name of the earthquake data file that you wish to parse")
       return 0

main()
