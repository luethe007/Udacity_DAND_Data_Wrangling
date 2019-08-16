'''This module is a playground, it does not contribute to data.py'''

import xml.etree.ElementTree as ET
import audit_streets
import audit_elevation_data

SAMPLE_FILE = "hawaii_medium.osm"


# count occurrence of tags
def count(filename):
    tags = {}
    for _, elem in ET.iterparse(filename):
        if elem.tag in tags:
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
    return tags

count(SAMPLE_FILE)


# check street data
street_types = audit_streets.audit_streets(SAMPLE_FILE)
for st_type, ways in street_types.items():
    for name in ways:
        better_name = audit_streets.update_name(name)
        print(name, "=>", better_name)

# elevation_data consists of 2 lists [elevation data too high], [elevation data format issues]
elevation_data = audit_elevation_data.audit_elevation(SAMPLE_FILE)

# check elevation data
for old_elevation in elevation_data[1]:
    new_elevation = audit_elevation_data.update_elevation(old_elevation)
    print(old_elevation, "=>", new_elevation)


# check for any id values in nodes table that cannot be converted to int values
def audit_node_id(osm_file):
    defect_ids = []
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node":
            for attrName, attrValue in elem.attrib.items():
                    if attrName == 'id':
                        try:
                            int(attrValue)
                        except ValueError:
                            defect_ids.append(attrValue)
    return defect_ids
