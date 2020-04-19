from pprint import pprint
from collections import Counter

def parse_json():
    import json
    with open("newsafr.json") as f:
        json_data = json.load(f)
        all_descriptions = json_data["rss"]["channel"]["items"]

        item_description = []
        for item in all_descriptions:
            description = item["description"].split()
            item_description += description
    return item_description

def parse_xml():
    import xml.etree.ElementTree as ET
    parser = ET.XMLParser(encoding="utf-8")

    with open("newsafr.xml") as f:
        tree = ET.parse("newsafr.xml", parser)
        root = tree.getroot()
        channel = root.find("channel")
        items = channel.findall("item")
        item_description = []
        for item in items:
            description = item.find("description").text
            description = description.split()
            item_description += description
    return item_description

def search_words_in_descriptions(item_description):
    list_of_words = []
    for word in item_description:
        if len(word) > 6:
            list_of_words.append(word.casefold())
    return list_of_words

def popular_words(format):
    if format == 'json':
        item_description = parse_json()
    elif format == 'xml':
        item_description = parse_xml()
    else:
        print('Неверный формат файла')
    list_of_words = search_words_in_descriptions(item_description)

    popular_words = Counter(list_of_words)
    pprint(popular_words.most_common(10))

print(f"Список слов для файла в формате json:\n")
popular_words('json')

print(f"\nСписок слов для файла в формате xml:\n")
popular_words('xml')
