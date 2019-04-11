from lxml import etree

def dtd_validate(xml):
    parser = etree.XMLParser(dtd_validation=True)
    tree = etree.parse(xml, parser)

#dtd_validate(xml2)