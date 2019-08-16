import xml.etree.ElementTree as ET

SAMPLE_FILE = "hawaii_medium.osm"


# Check if the postcodes are valid and accurate.
def audit_zip(osm_file):
    zip_length = []
    problematic_zips = []
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "tag" and elem.attrib['k'] == "addr:postcode":
            if len(elem.attrib['v']) != 5:
                zip_length.append(elem.attrib['v'])

            if not elem.attrib['v'].startswith('96'):
                problematic_zips.append((elem.attrib['v']))

    return zip_length, problematic_zips


# Cleaning procedure for XML-CSV conversion.
def update_zip_code(zip):
    if len(zip) != 5:
        index = zip.find('96')
        zip = zip[index:index+5]

    return zip