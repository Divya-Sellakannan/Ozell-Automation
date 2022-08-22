import requests
from bs4 import BeautifulSoup
from PropertyDetails import PAOPropertyDetails
from datetime import datetime

class PropertyAppraiserWebScraper:

    def getPropertyAppraiserDetails(self, realEstateNumber):
        # Making a GET request
        source = requests.get(
            'https://paopropertysearch.coj.net/Basic/Detail.aspx?RE='+realEstateNumber)

        # Parsing the HTML
        soup = BeautifulSoup(source.text, 'html.parser')
        try:
            realEstateNumber = soup.select_one(
                'span#ctl00_cphBody_lblRealEstateNumber').text
            ownerName = soup.select_one(
                'span#ctl00_cphBody_repeaterOwnerInformation_ctl00_lblOwnerName').text
            mailingAddress1 = soup.select_one(
                'span#ctl00_cphBody_repeaterOwnerInformation_ctl00_lblMailingAddressLine1').text
            mailingAddress2 = soup.select_one(
                'span#ctl00_cphBody_repeaterOwnerInformation_ctl00_lblMailingAddressLine3').text
            primaryAddress1 = soup.select_one(
                'span#ctl00_cphBody_lblPrimarySiteAddressLine1').text
            primaryAddressSplit = soup.select_one(
                'span#ctl00_cphBody_lblPrimarySiteAddressLine2').text.split(' ')
            city = primaryAddressSplit[0]
            state = primaryAddressSplit[1]
            zip = primaryAddressSplit[2]
            propertyUseSplit = soup.select_one(
                "span#ctl00_cphBody_lblPropertyUse").text.split(' ', 1)
            propertyUseCode = propertyUseSplit[0]
            propertyUse = propertyUseSplit[1]
            totalArea = soup.select_one("span#ctl00_cphBody_lblTotalArea1").text
            landMarketValue = soup.select_one(
                "span#ctl00_cphBody_lblLandValueMarketInProgress").text
            justMarketValue = soup.select_one(
                "span#ctl00_cphBody_lblJustMarketValueInProgress").text
            buildingTypeSplit = soup.select_one(
                "span#ctl00_cphBody_repeaterBuilding_ctl00_lblBuildingType").text.split('-')
            buildingTypeCode = buildingTypeSplit[0]
            buildingType = buildingTypeSplit[1]
            yearBuilt = soup.select_one(
                "span#ctl00_cphBody_repeaterBuilding_ctl00_lblYearBuilt").text
            buildingValue = soup.select_one(
                "span#ctl00_cphBody_repeaterBuilding_ctl00_lblBldgValue").text
            buildingDetails = soup.find(
                'table', id='ctl00_cphBody_repeaterBuilding_ctl00_gridBuildingAttributes').select('td:nth-child(2)')
            stories = buildingDetails[0].text
            bedrooms = buildingDetails[1].text
            bathrooms = buildingDetails[2].text
            paGrossArea = soup.find(
                'table', id='ctl00_cphBody_repeaterBuilding_ctl00_gridBuildingArea').select('td:nth-child(2)')
            grossArea = paGrossArea[len(paGrossArea)-1].text
            paHeatedArea = soup.find(
                'table', id='ctl00_cphBody_repeaterBuilding_ctl00_gridBuildingArea').select('td:nth-child(3)')
            heatedArea = paHeatedArea[len(paHeatedArea)-1].text
            paUseDescription = soup.find(
                'table', id='ctl00_cphBody_gridLand').select('td:nth-child(3)')
            useDescription = paUseDescription[0].text
            paZone = soup.find('table', id='ctl00_cphBody_gridLand').select(
                'td:nth-child(4)')
            zoningAssessment = paZone[0].text
            paFront = soup.find('table', id='ctl00_cphBody_gridLand').select(
                'td:nth-child(5)')
            front = paFront[0].text
            paDepth = soup.find('table', id='ctl00_cphBody_gridLand').select(
                'td:nth-child(6)')
            depth = paDepth[0].text
            paSaleDate = soup.find(
                'table', id='ctl00_cphBody_gridSalesHistory').select('td:nth-child(2)')
            paSalesHistory = []
            for sd in paSaleDate:
                saleDateStr = sd.text
                dateFormat = '%m/%d/%Y'
                saleDate = datetime.strptime(saleDateStr, dateFormat).date()
                paSalesHistory.append(saleDate)
            maxIndex = paSalesHistory.index(max(paSalesHistory))
            lastSaleDate = paSaleDate[maxIndex].text
            paSalePrice = soup.find(
                'table', id='ctl00_cphBody_gridSalesHistory').select('td:nth-child(3)')
            salePrice = paSalePrice[maxIndex].text
            paDeedInstrumentTypeCode = soup.find(
                'table', id='ctl00_cphBody_gridSalesHistory').select('td:nth-child(4)')
            DeedInstrumentTypeCode = paDeedInstrumentTypeCode[maxIndex].text
            paIsQualified = soup.find(
                'table', id='ctl00_cphBody_gridSalesHistory').select('td:nth-child(5)')
            isQualified = paIsQualified[maxIndex].text
            paVacantOrImproved = soup.find(
                'table', id='ctl00_cphBody_gridSalesHistory').select('td:nth-child(6)')
            vacantOrImproved = paVacantOrImproved[maxIndex].text
            
            return PAOPropertyDetails(realEstateNumber, ownerName, mailingAddress1, mailingAddress2, primaryAddress1, 
                city,state,zip, propertyUseCode, propertyUse,useDescription, zoningAssessment,
                front, depth,totalArea, buildingValue, landMarketValue, justMarketValue, lastSaleDate, salePrice, DeedInstrumentTypeCode, isQualified, vacantOrImproved,
                buildingTypeCode, buildingType, yearBuilt, stories, bedrooms, bathrooms, 
                grossArea, heatedArea)
        except (AttributeError):
            return