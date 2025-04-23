from importers import *
from spyne import ComplexModel, Unicode

def sha256_hash(obj):
    return hashlib.sha256(obj.encode("utf-8")).hexdigest()




def json_to_xml(root_name, data):
    def build_xml_element(parent, data):
        if isinstance(data, dict):
            for key, value in data.items():
                child = ET.SubElement(parent, key)
                build_xml_element(child, value)
        elif isinstance(data, list):
            for item in data:
                item_element = ET.SubElement(parent, "item")
                build_xml_element(item_element, item)
        else:
            parent.text = str(data)

    root = ET.Element(root_name)
    build_xml_element(root, data)
    return ET.tostring(root)




