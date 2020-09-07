#!/usr/bin/env python
import xml.etree.ElementTree as ET

countrydata='''
<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''

root = ET.parse('country_data.xml')
result = ''

# for elem in root.findall('.//child/grandchild'):
for elem in root.findall('.'):
    # How to make decisions based on attributes even in 2.6:
    # if elem.attrib.get('name') == 'foo':
    #     result = elem.text
    #     break
    # p
    print(elem.tag,elem.attrib)



pass

# 从字符串分析
root = ET.fromstring(countrydata)

# 从文件分析
# root = ET.parse('country_data.xml')

# Top-level elements
all=root.findall(".")
# print(all)
# for child in all:
#     print(child.tag,child.attrib)


# All 'neighbor' grand-children of 'country' children of the top-level
# elements
neighbor=root.findall("./country/neighbor")
# print(neighbor)

# Nodes with name='Singapore' that have a 'year' child
# root.findall(".//year/..[@name='Singapore']")

# 'year' nodes that are children of nodes with name='Singapore'
# root.findall(".//*[@name='Singapore']/year")

# All 'neighbor' nodes that are the second child of their parent
# root.findall(".//neighbor[2]")

