import requests
from lxml import etree
from bs4 import BeautifulSoup
from PropertyDetails import PAOPropertyDetails

class PropertyAppraiserWebScraper:

    def getPropertyAppraiserDetails(self,realEstateNumber):    
        # Making a GET request
        # source = requests.get('https://paopropertysearch.coj.net/Basic/Detail.aspx?RE='+realEstateNumber)

        # Parsing the HTML
        # soup = BeautifulSoup(source.text, 'html.parser')
        # dom = etree.HTML(str(soup))
                
        # apn = dom.css("div[class='propDetail_data'] >> table >> tbody >>tr >> td >> span[id='ctl00_cphBody_lblRealEstateNumber']")[0].text

        apn = realEstateNumber
        ownerName ='Test'
    
        """ apn = dom.xpath('//*[@id="ctl00_cphBody_lblRealEstateNumber"]')[0].text
        ownerName = dom.xpath('//*[@id="ctl00_cphBody_repeaterOwnerInformation_ctl01_lblOwnerName"]')[0].text

        propertyUse = dom.xpath('//*[@id="ctl00_cphBody_lblPropertyUse"]')[0].text
        totalBuildingValue = dom.xpath('//*[@id="ctl00_cphBody_lblBuildingValueInProgress"]')[0].text
        marketValue = dom.xpath('//*[@id="ctl00_cphBody_lblJustMarketValueCertified"]')[0].text
        justMarketValue = dom.xpath('//*[@id="ctl00_cphBody_lblJustMarketValueInProgress"]')[0].text
        totalArea = dom.xpath('//*[@id="ctl00_cphBody_lblTotalArea1"]')[0].text
        buildingType = dom.xpath('//*[@id="ctl00_cphBody_repeaterBuilding_ctl00_lblBuildingType"]')[0].text
        yearBuilt = dom.xpath('//*[@id="ctl00_cphBody_repeaterBuilding_ctl00_lblYearBuilt"]')[0].text
        buildingValue = dom.xpath('//*[@id="ctl00_cphBody_repeaterBuilding_ctl00_lblBldgValue"]')[0].text
        bedroom = dom.xpath('//*[@id="ctl00_cphBody_lblBeds"]')[0].text
        bathroom = dom.xpath('//*[@id="ctl00_cphBody_lblBaths"]')[0].text
        primaryResidence = dom.xpath('//*[@id="ctl00_cphBody_lblPrimarySiteAddressLine1"]')[0].text  """

        return PAOPropertyDetails(apn,ownerName)