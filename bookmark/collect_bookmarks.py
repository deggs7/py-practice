# -*- coding=utf-8 -*-
import sys, codecs
from xml.dom.minidom import parseString
from lxml import etree


def get_formated_string(f):
    rt = f.read()
    rt = rt.replace('&amp;', '&')
    rt = rt.replace('&', '&amp;')
    return rt


if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print "please enter filename"
    else:
        with codecs.open(sys.argv[1], 'r', 'utf-8') as f:
            #str = get_formated_string(f)
            str = f.read()
            tree = etree.HTML(str.encode('utf-8'))
            nodes = tree.xpath('//a')
            for n in nodes:
                print n.text
                print n.attrib['add_date']



