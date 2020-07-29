#!/usr/bin/env python3
import re
from io import StringIO
import xml.etree.ElementTree as ET

def parse_journal_name(journal):
    return journal.split(',')[0]

def is_proceedings(journal):
    if (re.search('Proceedings', journal) is not None):
        return True
    if (re.search('AAS Meeting', journal) is not None):
        return True
    return False

def get_records():
    parser = ET.XMLParser(encoding="utf-8")
    papers = ET.iterparse("papers.xml", parser=parser)
    #Remove the annoying ADS namespace
    for _, el in papers:
        prefix, has_namespace, postfix = el.tag.partition('}')
        if has_namespace:
            el.tag = postfix  # strip all namespaces
    root = papers.root
    records = []
    for record in root:
        rdict = {}
        rdict['authors'] = [elem.text for elem in record if elem.tag == 'author']
        rdict['title'] = record.find('title').text
        rdict['year'] = record.find('pubdate').text.split(' ')[-1]
        rdict['journal'] = record.find('journal').text
        try:
            rdict['eprint'] = record.find('eprintid').text
        except:
            pass
        try:
            rdict['DOI'] = record.find('DOI').text
        except:
            pass
        for link in record.findall('link'):
            if link.attrib['type'] == 'abstract':
                rdict['ADS'] = link.find('url').text
        records.append(rdict)
    return records

if __name__ == "__main__":
    cv_in = open('pages/cv.md.in').read()
    records = get_records()
    entries = ""
    for record in records:
        entry = "* _"
        if is_proceedings(record['journal']):
            pass
        else:
            entry += record['title'] + "_\n\n    "
            for author in record['authors']:
                if (re.search('Keller', author) is not None):
                    entry += "__" + author + "__"
                else:
                    entry += author 
                if (author != record['authors'][-1]):
                    entry += "; "
            entry += " " + record['year'] + " "
            entry += "[" + parse_journal_name(record['journal']) + "]"
            if 'DOI' in record:
                entry += "(https://dx.doi.org/" + record['DOI'] + ")\n\n"
            else:
                entry += record['ADS'] + ")\n\n"
            entries += entry
    newcv = re.sub('CVBODY', entries, cv_in)
    cv_out = open('pages/cv.md', 'w')
    cv_out.write(newcv)
    cv_out.close()
