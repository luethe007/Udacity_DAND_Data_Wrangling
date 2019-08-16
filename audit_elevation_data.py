import xml.etree.ElementTree as ET


# Check the elevation data for accuracy and uniformity.
def audit_elevation(osm_file):
    data_out_of_range = []
    data_format_issue = []
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "tag" and elem.attrib['k'] == "ele":
            try:  # Try to convert the elevation to an integer
                value = int(elem.attrib['v'])
                # Elevation data range [0m;4205m]
                if value > 4205 or value < 0:
                    data_out_of_range.append(value)
            except ValueError:  # If conversion to integer failed
                data_format_issue.append(elem.attrib['v'])

    return [data_out_of_range, data_format_issue]

# provide mapping to convert data to [meters], INTEGER or empty string ''
mapping = {'-5': '',
           '1.5': '1',
           '2.4': '2',
           '2694 feet MSL': '821',
           '147.2': '147',
           "571' MSL": '571',
           '1150.6': '1150',
           '521.51': '521',
           '700 ft': '213',
           '3055 m am Aussichtspunkt': '3055',
           '400-1100 ft': ''}


# Cleaning procedure for XML-CSV conversion.
def update_elevation(elevation):
    if elevation in mapping:
        return mapping[elevation]
    else:
        return elevation
