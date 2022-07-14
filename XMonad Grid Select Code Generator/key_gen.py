from other_functions import listJoin, intSplit

def categoryBindings(categoryList, sectionName):
    categoryKeys = []
    first = True
    for index, name in enumerate(categoryList):
        if first:
            if index < 10:
                key = "    " + "(" + "\"{}\", \"xdotool key super+alt+shift+{}\"".format(name, index) + ")"
            elif index > 10:
                key = "    " + "(" + "\"{}\", \"xdotool key super+alt-shift+{}\"".format(name, listJoin(intSplit(index))) + ")"
            categoryKeys.append(key + "\n")
            first = False
        else:
            if index < 10:
                key = "  , " + "(" + "\"{}\", \"xdotool key super+alt+shift+{}\"".format(name, index) + ")"
            elif index > 10:
                key = "  , " + "(" + "\"{}\", \"xdotool key super+alt+shift+{}\"".format(name, listJoin(intSplit(index))) + ")"
            categoryKeys.append(key + "\n")
    codeStr = "{}Categories=\n  [\n".format(sectionName)
    for key in categoryKeys:
        codeStr += key
    codeStr += " ]"
    return codeStr

def spawnBindings(categoryList, sectionName, categoryNames):
    keybindKeys = []
    first = True
    for index, name in enumerate(categoryList):
        if first:
            key = " (" + "\"M-M1-S-{}\"".format(listJoin(intSplit(index))) + ", addName \"{}\" $ spawnSelected\' {}".format(categoryNames[index], categoryList[index]) + ")"
            first = False
        else:
            key = "\n        , " + "(" + "\"M-M1-S-{}\"".format(listJoin(intSplit(index))) + ", addName \"{}\" $ spawnSelected\' {}".format(categoryNames[index], categoryList[index]) + ")"
        keybindKeys.append(key)
    codeStr = "^++^ subKeys \"{} Grid Select\" \n        [".format(sectionName)
    for key in keybindKeys:
        codeStr += key
    codeStr += "\n        ]"
    return codeStr