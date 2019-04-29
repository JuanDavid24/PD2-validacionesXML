import pytest
from DTD import valDTD as dtdv
from lxml.etree import XMLSyntaxError

xml1 = "quilmes.xml"
xml2 = "quilmes_roto.xml"
xml3 = "quilmes_dtdroto.xml"
xml4 = "quilmes_sinDef.xml"


def test_ok():
        dtdv.dtd_validate(xml1)
        pass

def test_xml_roto():
    with pytest.raises(XMLSyntaxError):
        dtdv.dtd_validate(xml2)

def test_dtd_roto():
    with pytest.raises(XMLSyntaxError):
        dtdv.dtd_validate(xml3)

def test_invalid_XML():
    with pytest.raises(XMLSyntaxError):
        dtdv.dtd_validate(xml4)