import re
def brand_strip(sectionStr):
    return re.sub('blackarch-', '', sectionStr)

def generateSections():
    sectionsList = []

    with open("txt/app-sections.txt") as f:
        for line in f:
            section = brand_strip(line).strip()
            sectionsList.append(section)

    with open("txt/raw-sections.txt", "w") as f:
        for section in sectionsList:
            section = re.sub('-', '_', section)
            f.write(section + "\n")