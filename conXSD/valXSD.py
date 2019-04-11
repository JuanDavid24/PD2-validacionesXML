import xmlschema

def isValidSchema(schemaName, xmlName):
    schema = xmlschema.XMLSchema(schemaName)
    return schema.is_valid(xmlName)
