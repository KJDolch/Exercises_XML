""" Exercise 5 - Starting with minidom
you created three different XML documents in the earlier exercises
use a small python script to parse these three documents
add two lines to parse simple XML strings"""

import xml.dom.minidom as mini


# to parse a docuemt
root = mini.parse("Exercise3b.xml")
print(root.firstChild.childNodes[1].firstChild.nodeValue)

root1 = mini.parse("Exercise2.xml")


# to parse a XML string
xml_string = "<a><b>1</b><c>2</c></a>"
root3 = mini.parseString(xml_string)
print(root3.firstChild.childNodes[1].firstChild.nodeValue)
