# import xml.etree.ElementTree as ET
# root = ET.parse('export1.gpx').getroot()
#
# print(root.attrib)


import xmltodict
#cleanData function
def processWPT(wpt):
    newWPT={}
    extensions ={}
    newWPT['extensions']=extensions
    newWPT['@lat'] = wpt['@lat']
    newWPT['@lon'] = wpt['@lon']
    name = wpt['name']
    if len(name)>6:
        print("waypoint with name {} was not added since length {} is greater than 6".format(name,len(name)))
        return None
    newWPT['name'] = name
    return newWPT



def cleanData(data):
    cleanData, gpx,waypointList ={}, {},[]
    gpx['wpt']=waypointList
    cleanData['gpx']=gpx
    for wpt in data['gpx']['wpt']:
        processedWPT=processWPT(wpt)
        waypointList.append(processedWPT)
    return cleanData



with open('../export2wpt.gpx') as fd:
    data = xmltodict.parse(fd.read())
    cleanData1=cleanData(data)
    with open('export2.gpx', 'w') as result_file:
        result_file.write(xmltodict.unparse(cleanData1,pretty='True'))








