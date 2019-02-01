#! /Users/d4rkness/.pyenv/shims/python

import sys, getopt, os
import urllib.request
import json
from EBToHTMLParser import EBToHTMLParser

# This part obtains arguments from user input
# Start
inputFile = ''
outputFile = ''
holidaysDateString = '1/1/1990'

myOptions, myArguments = getopt.getopt(sys.argv[1:], 'i:o:x:')

for option, argument in myOptions:
  if option == '-i':
    inputFile = argument
  elif option == '-o':
    outputFile = argument
  elif option == '-x':
    holidaysDateString = argument
# End

# This function extract event ID from EventBrite URL
# Start
def extractEventIDFromEventBriteURL(url):
  processedEventID = url.split('-')[-1]
  
  return processedEventID
# End

# This part creates a list containing all of the event IDs in the input file
# Start
listOfEventIDs = []
inputFileStream = open(inputFile)

for line in inputFileStream:
  listOfEventIDs.append(extractEventIDFromEventBriteURL(line).strip())
# End

ebToken = open('./token.txt').readline()

listOfEventResponse = []
eventBriteAPIToken = '?token=' + ebToken
eventBriteAPIRootURL = 'https://www.eventbriteapi.com/v3/'
eventBriteAPIEventURL = eventBriteAPIRootURL + 'events/'

# Creates a list of responses for every single IDs in listOfEventIDs
for item in listOfEventIDs:
  response = urllib.request.urlopen(eventBriteAPIEventURL + item + eventBriteAPIToken).read()
  formattedResponse = json.loads(response)
  listOfEventResponse.append(formattedResponse)
# End

# Writes responses from EBToHTMLParser to the output file
outputFileStream = open(outputFile, 'w')
for item in listOfEventResponse:
  outputFileStream.write(EBToHTMLParser(item, holidaysDateString))
# End

# You need to flush the stream to ensure the file writes is always successful.
outputFileStream.close()

os.system('say "{} links processed."'.format(len(listOfEventResponse)))
