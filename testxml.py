import xml.dom.minidom
# import xml.etree.ElementTree as ET


def read_xml():
    doc = xml.dom.minidom.parse('test.xml')
    students = doc.getElementsByTagName("student")
    for student in students:
        print(student.getAttribute("type"))


read_xml()
