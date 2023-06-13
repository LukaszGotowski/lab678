import json
import yaml
import xmltodict
from yaml import SafeLoader

file_type_xml = "plik.xml"
file_type_json = "plik.json"
file_type_yaml = "plik.yaml"

type = input("Podaj rozszerzenie pliku, które chcesz użyć\ndostępne formaty to : xml, yaml, json\n")
type_to = input("Podaj rozszerzenie pliku, na które chcesz przekonwertować : ")

def convert():
    if type == "json":
        if type_to == "xml":
            with open(f'{file_type_json}') as json_file:
                data = json.load(json_file)
                xml_file = open(file_type_xml, "w")
                xmltodict.unparse(data, output=xml_file)
                xml_file.close()
        elif type_to == "yaml":
            with open(f'{file_type_json}') as json_file:
                python_dict = json.load(json_file)
                file1 = open("plik.yaml", "w")
                yaml.dump(python_dict, file1)
                file1.close()


convert()