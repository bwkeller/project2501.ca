#!/usr/bin/env python3
import re
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
    papers = ET.parse("papers.xml", parser=parser)
    root = papers.getroot()
    records = []
    for record in root:
        rdict = {}
        rdict['authors'] = [elem.text for elem in record if elem.tag == 'author']
        rdict['title'] = record.find('title').text
        rdict['year'] = record.find('pubdate').text.split(' ')[-1]
        rdict['journal'] = record.find('journal').text
        try:
            rdict['DOI'] = record.find('DOI').text
        except:
            pass
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
            entry += "(https://dx.doi.org/" + record['DOI'] + ")\n\n"
            entries += entry
    newcv = re.sub('CVBODY', entries, cv_in)
    cv_out = open('pages/cv.md', 'w')
    cv_out.write(newcv)
    cv_out.close()
