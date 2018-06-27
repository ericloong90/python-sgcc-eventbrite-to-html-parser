#! /Users/d4rkness/.pyenv/shims/python

import sys, getopt
import urllib.request
import json

# This part obtains arguments from user input
# Start
inputFile = ''
outputFile = ''

myOptions, myArguments = getopt.getopt(sys.argv[1:], 'i:o:')

for option, argument in myOptions:
  if option == '-i':
    inputFile = argument
  elif option == '-o':
    outputFile = argument
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


listOfEventResponse = []
eventBriteAPIToken = '?token=XCGWLF2RIJOXZFGAQRMK'
eventBriteAPIRootURL = 'https://www.eventbriteapi.com/v3/'
eventBriteAPIEventURL = eventBriteAPIRootURL + 'events/'

for item in listOfEventIDs:
  response = urllib.request.urlopen(eventBriteAPIEventURL + item + eventBriteAPIToken).read()
  formattedResponse = json.loads(response)
  listOfEventResponse.append(formattedResponse)

