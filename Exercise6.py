""" Exercise 6 - Getting Values """
# Take one of your example XML scripts from the previous exercises
# Print out all values that are in your XML document with the help of minidom
# use the firstChild.childNodes method we saw in the presentation

import xml.dom.minidom as mini

root = mini.parse("Exercise3b.xml")
print(root.firstChild.childNodes[1].firstChild.nodeValue)
print(root.firstChild.childNodes[3].firstChild.nodeValue)
print(root.firstChild.childNodes[5].firstChild.nodeValue)
print(root.firstChild.childNodes[7].childNodes[1].firstChild.nodeValue)
print(root.firstChild.childNodes[7].childNodes[3].firstChild.nodeValue)
print(root.firstChild.childNodes[9].firstChild.nodeValue)
print(root.firstChild.childNodes[11].firstChild.nodeValue)
