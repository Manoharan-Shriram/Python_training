# import sys

# #Print's Filename
# print(sys.argv)

# print("Hello")

# #Print's file name
# print(sys.argv[0])

# #Print the arguments
# print(sys.argv[1:])

# #Print the file name
# print(f'file name: {sys.argv[0]}')

# l=[]
# for i in range(6):
#     if i > 0:
#         l.append(sys.argv[i])
# p=[]
# for i in range(len(l)):
#     p.append(int(l[i]))
# k=0
# for i in range(len(l)):
#     k+=p[i]
# print(k)


# #alternate logic less lines of code

# v1=sys.argv[1:]
# v2=[]
# for i in v1:
#     v2.append(int(i))

# x=sum(v2)
# print(x)

# THe previous is just warmup


#import argparse

#parser - holds our arguments

#syntax - parser = argparse.ArgumentParser()

#basic 

# *******************************************************************************************************************************************


#import argparse


# parser=argparse.ArgumentParser()
#   # 'name' -  positional argument
# parser.add_argument('name',help='Enter your name') 

# #'--age' -  optional argument when giving input you should give --aage then input i.e  --age 22
# # parser.add_argument('--age',required=True,help='Enter your age (Required)') #The optional argument can be covnerted into required(kind of positional) by adding required to True   

#  # The type will check the input type and throw error if its not the given type 
# parser.add_argument('phone',type=int,nargs='?',default=1234,help='Enter your number')  
# parser.add_argument('color',nargs='*',default='No color',help='Enter the colours') 
# #default only work in a few cases such as choice , nargs -  

# #If called in the terminal it will change its value to True else it will stay as false  just mention -t , --true
# # parser.add_argument('-t','--true',action='store_true')  #store_ is keyword it can be either true or false


# # args holds all parsers
# args=parser.parse_args()

# print(args.name)
# print(args.age)
# print(args.phone)
# print(args.true)


# '*' - takes multiple arguments
# parser=argparse.ArgumentParser()
# parser.add_argument('color',nargs='*',default='No color',help='Enter the colours')
# args=parser.parse_args()
# print(args.color)

# # '?' - either accept one arg or zero arg 
# parser=argparse.ArgumentParser()
# parser.add_argument('color',nargs='?',default='No color',help='Enter the colours')
# args=parser.parse_args()
# print(args.color)

# # '+' -  one or more arg 
# parser=argparse.ArgumentParser()
# parser.add_argument('color',nargs='+',help='Enter the colours')
# args=parser.parse_args()
# print(args.color)


#While Entering input in the terminal positional arguments should be given in order but optional order does'nt necessarily need to be in order
# parser = argparse.ArgumentParser()

# parser.add_argument('name',help="Enter your name")
# parser.add_argument('age',type=int,help="Enter your age (int)")
# parser.add_argument('-p','--phone',type=int,help="Enter your number")
# parser.add_argument('-c','--country',help="Enter your country")

# args=parser.parse_args()
# print(args.name)
# print(args.age)
# print(args.phone)
# print(args.country)

#choices
# parser=argparse.ArgumentParser()

# parser.add_argument('Fruit',choices=['banana','kiwi','apple'],help="Choose one from the options")

# parser.add_argument('--Fruits',choices=['banana','kiwi','apple'],default='banana',help="Choose one from the options")

# args=parser.parse_args()

# print(args.Fruit)
# print(args.Fruits)


# *******************************************************************************************************************************************

# metavar  #Provides more data about the variable 

# parser=argparse.ArgumentParser(description="Enter your name in the terminal line")

# parser.add_argument('-n','--name',metavar='Name',required=True)


# parser.add_argument('-s','--something',action='store_const',const=5)

# args=parser.parse_args()

# print(args.name)
# print(args.something)


# *******************************************************************************************************************************************

#function 

# def greeting(name,lang):
#     greet={
#         'english' : 'Hello',
#         'spanish' : 'Hola',
#         'German' : 'Hallo'
#     }

#     msg= f'{greet[lang]} {name}'
#     print(msg)

# parser=argparse.ArgumentParser()

# parser.add_argument('name',help="Enter your name:")

# parser.add_argument('Lang',choices=['english','spanish','german'],help="Choose your Language")

# args=parser.parse_args()

# greeting(args.name,args.Lang)


# *******************************************************************************************************************************************


# Gropus   syntax - login_group=parser.add_argument_group('Login Data')

# parser=argparse.ArgumentParser()

# login_group=parser.add_argument_group('Login Data')
# login_group.add_argument('Name',help='Enter your name')
# login_group.add_argument('Password',help='Enter your age',type=int)

# personal_group=parser.add_argument_group('Personal data')
# personal_group.add_argument('Fathername',help="Enter your father's name ")
# personal_group.add_argument('Mothername',help="Enter your mother's name ")

# args=parser.parse_args()

# print(args.Name)
# print(args.Password)
# print(args.Mothername)
# print(args.Fathername)


# *******************************************************************************************************************************************

# Mutually exclusive groups

# parser=argparse.ArgumentParser()

# group  = parser.add_mutually_exclusive_group(required=True)
# group.add_argument('-u','--upload',action='store_true',help='Upload a file')
# group.add_argument('-d','--download',action='store_true',help='Download a file')

# args=parser.parse_args()

# if args.upload:
#     print("Uploding......")
# elif args.download:
#     print("Downloading.....")


# *******************************************************************************************************************************************

# Tasks


# Command Line Arguments


# Take a list of numbers as arguments and print their average.

# Accept a filename and count how many lines it has.

# Pass two words and print the longer one.

# Check if a number passed is prime.

# Accept multiple filenames and print which ones exist.


# Argparse

# 1. Add two numbers using argparse

# 2.Repeat a Word
# Goal: Accept a word and a count as arguments, print the word that many times.

# 3.Choose Operation (Add, Subtract)
# Goal: Accept two numbers and an operation (--op add or --op sub)

# 4.Multiple File Inputs
# Goal: Use nargs='+' to accept a list of file names

# 5.Word Counter
# Description:
# Accept a sentence and count number of words.

# 6.Create a User Profile
# Description:
# Collect user's name, age, and gender from command line and print profile.

# 7.File Analyzer
# Description:
# Take a file name as input, and return:

# Number of lines

# Number of words

# Number of characters
# Based on flags passed.

# Arguments:

# filename (positional)

# --lines (store_true)

# --words (store_true)

# --chars (store_true)

# 8.Temperature Converter
# Description:
# Convert temperature from Celsius to Fahrenheit or vice versa.

# Arguments:

# --value (required, float)

# --to (choices=['C', 'F'], required)

# 9.Search for Word in File
# Description:
# Search for a word in a text file and print line numbers containing that word.

# Arguments:

# filename (positional)

# --word (required)

# 10.Try to give a example using all types of arguments in parser.add_argument()

# *******************************************************************************************************************************************

# 1 Take a list of numbers as arguments and print their average

# import sys

# a=sys.argv 

# v1=sys.argv[1:]
# v2=[]
# for i in v1:
#     v2.append(int(i))
    
# x=sum(v2)//5

# print(x)

# *******************************************************************************************************************************************

# 2 Accept a filename and count how many lines it has


# import sys 

# a=sys.argv
# l=0
# with open(a[1],'r') as s:
#     l=len(s.readlines())

# print(l)

# *******************************************************************************************************************************************



#Argparse tasks

# 1. Add two numbers using argparse

# import argparse

# parser=argparse.ArgumentParser()

# parser.add_argument('Value1',help='Enter the first value')
# parser.add_argument('Value2',help='Enter the Second value')

# args=parser.parse_args()

# print((int(args.Value1)+int(args.Value2)))


# *******************************************************************************************************************************************



# 2.Repeat a Word
# Goal: Accept a word and a count as arguments, print the word that many times.


# import argparse

# parser=argparse.ArgumentParser()

# parser.add_argument('Word',help='Enter the word ',type=str)
# parser.add_argument('Count',help='Enter the word ',type=int)

# args=parser.parse_args()

# for i in range(args.Count):
#     print(args.Word)



# *******************************************************************************************************************************************



# 4.Multiple File Inputs
# Goal: Use nargs='+' to accept a list of file names

# import argparse

# parser=argparse.ArgumentParser()

# parser.add_argument('Filename',help='Enter the list of file names ',nargs='+')

# args=parser.parse_args()

# k=list(args.Filename)

# print(k)


# *******************************************************************************************************************************************


# 3.Choose Operation (Add, Subtract)
# Goal: Accept two numbers and an operation (--op add or --op sub)

# import argparse

# parser=argparse.ArgumentParser()

# parser.add_argument('Value1',help='Enter the first value',type=int)
# parser.add_argument('Value2',help='Enter the Second value',type=int)
# parser.add_argument('Operation',choices=['ADD','SUB'],help="Enter the operation")

# args=parser.parse_args()

# if args.Operation == 'ADD':
#     print(args.Value1 + args.Value2)
# elif args.Operation =='SUB':
#     print(args.Value1 - args.Value2)

# *******************************************************************************************************************************************


# 5.Word Counter
# Description:
# Accept a sentence and count number of words.

# import argparse

# parser=argparse.ArgumentParser()

# parser.add_argument('Sentence',nargs='+',help= "Enter the sentence")

# args=parser.parse_args()

# print(len(args.Sentence))


# *******************************************************************************************************************************************

# 6.Create a User Profile
# Description:
# Collect user's name, age, and gender from command line and print profile.


