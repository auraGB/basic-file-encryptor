import argparse # this is for the CLI tool which is how we will use the script ( allows us to parse the arguments passed )
import os       #The os module will help with getting files, directorys, ect 
import sys      #system module lets us use system commands 

arg_parser = argparse.ArgumentParser( description = "give me a file to encrypt!" )
