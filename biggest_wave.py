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

# def find_fastest_wave():
#
# def find_largest_wave():
#
# def make_waves():
#
# def make_lists():
#
# def make_csv():
#
# def split_file(filename):
#
def mkdir(filename):
    path = os.getcwd()
    path += "/" + filename + "_parsed"
    os.mkdir(path)

def main():
    if (len(sys.argv) > 1):
        filename = sys.argv[1]
    else:
       print ("enter the name of the earthquake data file that you wish to parse")
       sys.exit(0)
    mkdir(filename)

main()
