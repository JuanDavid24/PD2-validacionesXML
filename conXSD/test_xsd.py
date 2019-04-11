import pytest
from xmlschema.etree import ParseError
from conXSD import valXSD

schema1 = "formacion.xsd"
schema2 = "formacion_roto.xsd"

xml1 = "quilmes_basico.xml"
xml2 = "quilmes_basico_roto.xml"
xml3 = "quilmes_basico_sinArq.xml"

def test_ok():
    assert valXSD.isValidSchema (schema1, xml1) == True
    pass

def test_xmlRoto():
    with pytest.raises(ParseError):
        valXSD.isValidSchema (schema1, xml2)
    pass

def test_xsdRoto():
    with pytest.raises(ParseError):
        valXSD.isValidSchema (schema2, xml1)
    pass
def test_xmlInvalido():
    assert valXSD.isValidSchema(schema1, xml3) == False
    pass


