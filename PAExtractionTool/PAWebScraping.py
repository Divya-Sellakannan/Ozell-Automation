import json
from PropertyAppraiserWebScraper import PropertyAppraiserWebScraper

inputFilePath ='inputForPAExtraction.json'
paoInputRENumbers=[]

# Opening JSON file
with open(file = inputFilePath, mode ='r') as openfile:
    # returns JSON object as
    # a dictionary
    inputData = json.load(openfile)
 
for apn in inputData:
    realEstateNumberFromJSON= apn['realEstateNumber']
    paoInputRENumbers.append(realEstateNumberFromJSON)

paoArray= []

for paoInputRENumber in paoInputRENumbers: 
    #create an instance for PropertyAppraiserWebScraper class
    webScraper = PropertyAppraiserWebScraper()
    
    # calling getPropertyAppraiserDetails method
    propertyDetails= webScraper.getPropertyAppraiserDetails(paoInputRENumber)
    
    paoArray.append(propertyDetails)

with open('paoSearchResult.json', "w") as outputFile:
    jsonString =json.dumps(paoArray, indent=2)
    outputFile.write(jsonString)

