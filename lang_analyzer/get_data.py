#!/usr/bin/python3
import requests
import xmltodict

url_house="http://clerk.house.gov/xml/lists/MemberData.xml"
url_senate="http://www.senate.gov/general/contact_information/senators_cfm.xml"

xml_house="HouseMemberData.xml"
xml_senate="SenateMemberData.xml"

def get_xml():
	response = requests.get(url_house)
	with open(xml_house, 'wb') as file:
		file.write(response.content)

	file.close()

	response = requests.get(url_senate)
	with open(xml_senate, 'wb') as file:
		file.write(response.content)

	file.close()

get_xml()