import xml.etree.ElementTree as ET
from collections import defaultdict
import re

# Regular Expression to search for a sequence of non-whitespace characters
# optionally followed by a period to catch abbreviations like Ave or St.
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

# Provide mapping for expected values
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons", "Highway", "Way", "Walk", "Circle", "Promenade", "Dr", "Honolulu", "Kailua,",
            "Kalanikaumaka", "Loop", "Mall", "Promenade"]

# Provide mapping for data cleaning
mapping = {"Ave": "Avenue",
           "Ave.": "Avenue",
           "Blvd": "Boulevard",
           "Hwy": "Highway",
           "Hwy.": "Highway",
           "Rd.": "Road",
           "Rd": "Road",
           "St": "Street",
           "St.": "Street"
           }


# Add street name to street_types dictionary.
def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)


# Check if attribute is a street.
def is_street_name(elem):
    return elem.attrib['k'] == "addr:street"


# Return the street_types dictionary.
def audit_streets(osm_file):
    street_types = defaultdict(set)

    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    return street_types


# Cleaning procedure for XML-CSV conversion.
def update_name(name):
    street = street_type_re.search(name)

    if street:
        street_type = street.group()
        if street_type not in expected:
            name = mapping[street_type]
    return name
