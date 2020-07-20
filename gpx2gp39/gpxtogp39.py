# import xml.etree.ElementTree as ET
# root = ET.parse('export1.gpx').getroot()
#
# print(root.attrib)


import xmltodict

def cleanData(data):
    data['gpx'].pop('trk', None)
    data['gpx'].pop('@creator', None)
    data['gpx'].pop('@creator', None)
    data['gpx'].pop('@xmlns:xsi', None)
    data['gpx'].pop('@xmlns:gpxx', None)
    data['gpx'].pop('@xsi:schemaLocation', None)
    data['gpx'].pop('@xmlns:opencpn', None)
    for wpt in data['gpx']['wpt']:
        print(wpt)
        wpt.pop('time', None)
        wpt.pop('sym', None)
        wpt.pop('type', None)
        wpt['extensions']={'GP39Symbol':0,'FECColor':0,'GP39Comment':'nocomment','GP39Flag':1}




with open('export1.gpx') as fd:
    data = xmltodict.parse(fd.read())
    cleanData(data)







with open('export2.xml', 'w') as result_file:
    result_file.write(xmltodict.unparse(data))

