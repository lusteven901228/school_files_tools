import requests
from requests.utils import requote_uri
import re
def main():
    attributelist = ('CID','name', 'formula', 'smiles')
    while s := input("0-cid, 1-name, 2-formula, 3-smiles:"):
        if -1<(i:=int(s))<4:
            value = input(attributelist[i]+':')
            if not value: continue
            get_from_attribute(attributelist[i], value)
        else:
            print("Invalid input")

def get_from_attribute(attribute, value):
    if attribute == 'CID':
        return get_data(value)
    listkey = None
    url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/' + attribute + '/' + value + '/cids/JSON?MaxRecords=1'
    url = requote_uri(url)
    r = requests.get(url).json()
    print(r)
    while not 'IdentifierList' in r:
        listkey = r['Waiting']['ListKey']
        del r
        r = requests.get('https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/listkey/' + listkey + '/cids/JSON').json()
    print(r)
    try:
        if 'IdentifierList' in r:
            cid = r['IdentifierList']["CID"][0]
            get_data(cid)
        else:
            if r['Fault']['Code'] == "PUGREST.BadRequest":
                print(r['Fault']['Message'])
                print(listkey)
            else:
                print('Not Found')
                print(listkey)
            return False
    except KeyError as ex:
        print(listkey)
        print(f'KeyError:{ex}')
        return False
def get_data(cid):
    r = requests.get(f'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/{cid}/JSON').json()['Record']
    result = [r["RecordNumber"], r["RecordTitle"]]
    data_identifier = [
        [
            "Names and Identifiers",
            "Molecular Formula"
        ],
        [
            "Names and Identifiers",
            "Other Identifiers",
            "CAS"
        ],
        [
            "Chemical and Physical Properties",
            "Experimental Properties",
            "Boiling Point"
        ],
        [
            "Chemical and Physical Properties",
            "Experimental Properties",
            "Melting Point"
        ],
        [
            "Chemical and Physical Properties",
            "Experimental Properties",
            "Solubility"
        ],
        [
            "Chemical and Physical Properties",
            "Experimental Properties",
            "Density"
        ],
        [
            "Chemical and Physical Properties",
            "Experimental Properties",
            "Physical Description"
        ],
        [
            "Safety and Hazards",
            "Hazards Identification",
            "GHS Classification"
        ]
    ]
    for i in data_identifier:
        result.append(find_in_json(r['Section'],i))
    hazards = set()
    for i in result.pop(-1):
        m = re.search(r'\[(.+)\]',i)
        if m:
            hazards.add(m.group(1))
    result.append(hazards)
    print(result)
    # ml = 0
    # for i in result:
    #     if type(i) == set:
    #         if ml < (t:=len(i)):
    #             ml = t
    return result
    
def find_in_json(json_list, filter_list):
    search = filter_list.pop(0)
    for section in json_list:
        if section['TOCHeading'] == search:
            if filter_list:
                return find_in_json(section['Section'], filter_list)
            else:
                r = set()
                for i in section.get('Information') or []:
                    for j in i['Value'].get('StringWithMarkup') or []:
                        r.add(j['String'])
                return r

if __name__ == '__main__':
    main()
