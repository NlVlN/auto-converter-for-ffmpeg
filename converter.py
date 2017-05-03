# -*- coding: utf-8 -*-
import subprocess
import os

directory = raw_input("Enter the path to the files\n>")

if directory[-1:] == "/":
    directory = directory[:-1]
else:
    pass

lista = directory + "/converted/list"
bash_commands = "mkdir %s/converted && ls %s | grep \".\" > %s" % (directory, directory, lista)
#print bash_commands

os.system(bash_commands)
for input_file in open(lista).readlines():
    input_file = input_file.strip()
    output_file =input_file[:input_file.find(".")]
    ffmpeg = "ffmpeg -i \"%s/%s\" -b:a 128 \"%s/converted/%s.mp3\"" % (
    directory, input_file, directory, output_file)
    print ffmpeg
    os.system(ffmpeg)
    # subprocess.call(ffmpeg)
if (raw_input("\nDelete original files? [y/n]\n>") == "n"):
    os.remove(lista)
else:
    cleaning = "rm %s && mv %s/converted/* %s && rmdir %s/converted && rm %s/*.flac && rm %s/*.wav" % (
    lista, directory, directory, directory, directory, directory)
    os.system(cleaning)
