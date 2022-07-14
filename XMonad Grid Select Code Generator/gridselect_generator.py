import sections_generator
import re
from other_functions import listJoin, intSplit
from key_gen import categoryBindings, spawnBindings

def gsSectionGen(sectionName):
    return "{}=\n  [\n\n  ]\n".format(sectionName)

def gsAllGen(sectionsList, arrsName):
    allStr = "gsAll{} = ".format(arrsName)
    first = True
    for section in sectionsList:
        if first:
            allStr += section
            first = False
        else:
            allStr += " ++ " + section 
    return allStr
def gsListGen(filePath):
    sectionsList = []
    namesList = []
    with open(filePath, "r") as f:
        for line in f:
            name = line.strip().capitalize()
            sectionsList.append("gs" + name)
            namesList.append(name)
    return sectionsList, namesList

def gsCodeGen():
    sections, names = gsListGen("txt/raw-sections.txt")
    gsAll = gsAllGen(sections, "Hacking")
    categoryKeys = categoryBindings(names, "hacking")
    spawnKeys = spawnBindings(sections, "Hacking", names)

    codeStr = ""
    codeStr += categoryKeys + "\n"
    for rawSection in sections:
        codeStr += gsSectionGen(rawSection)
    codeStr += "\n" + gsAll
    codeStr += "\n\n\n\n" + spawnKeys
    return codeStr

# ===== MAIN CODE =====
if __name__ == '__main__':
    sections_generator.generateSections()

    with open("txt/output.txt", "w") as f:
        f.write(gsCodeGen())