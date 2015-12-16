import xml.etree.ElementTree as ET
import re
import sys
import glob
import os

pos_replacements = {
        "f."            : "N",
        "m."            : "N",
        "v. n."         : "V",
        "a."            : "A",
        "adv."          : "other",
        "prep."         : "other",
        "neutrum"       : "N",
        "adjectivum"    : "A",
        "masculinum"    : "N",
        "verbum"        : "V",
        "feminium"      : "N",
        "verbumneutrum" : "V",
        "verbumactivum" : "V",
        "interjectio"   : "other",
        "??p."          : "A",
        "adverbium"     : "other",
        "verbumreciprocum"  : "V",
        "verbumdeponens"    : "V",
        "??sup."        : "del",
        "comparativus"  : "del",
        "??gen."        : "del",
        "??m.pl."       : "N",
        "pronomen"      : "P",
        "??adj.indecl." : "A",
        "??prÃ¤p."      : "other",
        "??prÃ¤."       : "other",
        "??a."          : "A",
        "pluralis" : "N",
        "??f.pl." : "del",
        "??v.defect." : "del",
        "genuscommune" : "names",
        "??s.pl." : "N",
        "??adj.comp." : "del",
        "conjunctio" : "other",
        "??u." : "N",
        "??n.p." : "N",
        "??(utkomst&c.)" : "N",
        "??(vattufallc.)" : "N",
        "??n.o." : "NUM",
        "??f.a." : "N",
        "??n.c." : "NUM",
        "??adj.mod." : "del",
        "??d." : "A",
        "??adj.pl." : "other",
        "??pron.dat." : "del",
        "??v.n" : "V",
        "??v.imp." : "V",
        "substantioum" : "A",
        "??adj.superl." : "del",
        "??intj." : "other",
        "verbumpassivum" : "V",
        "??n.pl." : "N",
        "??ajd." : "A",
        "??pr." : "other",
        "??pron.rel." : "P",
        "??prÃ¤p.adv." : "other",
        "??j." : "del",
        "??v.fr." : "V",
        "??v.an." : "V",
        "??(arb.kostnad)" : "V",
        "??n.,spyning" : "N",
        "??tr." : "N",
        "??ff." : "N",
        "??adj.sup." : "other",
        "??v..a" : "V",
        "??v.v." : "V",
        "??advv." : "other",
        "??v.an.om." : "V",
        "??proon." : "del",
        "??pl.af" : "other",
        "numeralecardinale" : "NUM",
        "??no." : "NUM",
        "numeraleordinale" : "NUM",
        "??fr." : "N",
        "??(ifr.parti)" : "V",
        "??(comp.aflÃ¥ng)" : "del",
        "??superl." : "del",
        "??l." : "N",
        "??v.a" : "V",
        "??(skr.ochkorn)" : "N",
        "??(ifr.Ã¶fverh.)" : "del",
        "??h." : "N",
        "??r." : "N",
        "imperativus" : "V",
        "??dat." : "del",
        "??gen.pron.adv." : "del",
        "??v.impers." : "V",
        "??pron.pl." : "P",
        "indeclinabile" : "other",
        "??v..r" : "V",
        "??(t.detpÃ¥)" : "V",
        "??num." : "NUM",
        "??uttr.imper." : "del",
        "adjektiivi" : "A",
        "substantiivi" : "N",
        "verbi" : "V",
        "adverbi" : "other",
        "verbumfrequentativo-dim." : "V",
        "verbumsubitum" : "V",
        "verbummedium" : "V",
        "interjektio" : "other",
        "verbumfactivum" : "V",
        "S/A" : "A",
        "A/S" : "A",
        "??(ifr.öfverh.)" : "V",
        "??(t.detpå)" : "V",
        "??(comp.aflång)" : "del",
        "??präp.adv." : "other",
        "konjunktio" : "other",
        "??präp." : "other",
        "??prä." : "other",
        "pronomini" :"P",
        "postpositiojaprepositio" : "other",
        "A/S/AD" : "A",
        "numeraali" : "NUM",
        "V/VM" : "V",
        "liitepartikkeli" : "other",
        "V/S" : "V",
        "A/P" : "A",
        "P/L" : "P",
        "propri" : "names",
        "P/AD" : "P",
        "VM/VS" : "V",
        "A/N" : "A",
        "VS/VM" : "V",
        "A/N" : "A",
        "AD/PP" : "other",
        "S/AD" : "N",
        "AD/K" : "other",
        "AD/P" : "other",
        "I/S" : "other",
        "I/L" : "other",
        "PR/S" : "names",
        "VF/M" : "V",
        "AD/I" : "other",
        "" : "UNK",
        "VM/V" : "V",
        "S/PP" : "other",
        "K/AD" : "other",
        "P/A" : "other",
        "N/S" : "N",
        "AD/L" : "other",
        "unknown" : "UNK"}


def analyse_tree(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    text = root.find('text').find('body')


    entries = text.findall('entry')
    res = []
    print(filename, len(entries))
    for child in entries:

        entry_name = child.find('form').find('orth').text
        entry_name = fix_entry_name(entry_name)
        if len(re.split(" ", entry_name)) == 1:

            if child.find('gramGrp') is not None:
                if child.find('gramGrp').find('pos') is not None:
                    pos = child.find('gramGrp').find('pos').text
                else:
                    pos = child.find('gramGrp').text
                pos = re.sub("[\n\t ]", "", pos)

            else:
                pos = "unknown"


            try:
                pos_c = identify_pos(pos)

            except:
                KeyError
                print("Key Error:"+pos+"   "+entry_name)
            try:
                write_to_file(filename, pos_c, entry_name)
            except:
                UnboundLocalError
                print(ET.tostring(child))

    try:
        text = text.find('div').find('p')
        entries = text.findall('s')
        print(filename, len(entries))
        for entry in entries:
            text = re.sub("[\t\n]", "", entry.text)
            entry_name = re.split("\*", text)[0]
            entry_name = re.split(" ", entry_name)
            if len(entry_name) == 0:
                entry_name = entry_name[0]
                parts = re.split(" ", re.split("\*", text)[1])
                for x in parts:
                    if x in pos_replacements: pos = x
                write_to_file(filename, pos, entry_name)
    except:
        AttributeError





def write_to_file(filename, pos, entry):
    entry = fix_entry_name(entry)
    with open(filename+"_"+pos+".txt", "a", encoding="utf-8") as f:
        f.write("1 "+entry+"\n")

def fix_entry_name(entry):
    entry = re.sub("[\]\[;/\n)(]", "", entry)
    entry = re.sub(" *$", "", entry)
    return entry

def identify_pos(pos):
    return pos_replacements[re.sub("[\t\n ]", "", pos)]

files = ["helenius.xml", "lexik1865.xml", "renvall.xml", "sanakirja1853.xml"]

def clean_files(filename):
    for x in glob.glob(filename+"*.txt"):
        print(x)
        os.remove(x)

for x in files:
    clean_files("cemf-dict/"+x)
    analyse_tree("cemf-dict/"+x)
