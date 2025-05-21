import pandas as pd
from openpyxl import load_workbook
from googletrans import Translator

translator = Translator()

dataframe = load_workbook('codelijst.xlsx')

languages = []

# Define filepath
filepath = 'codelijst.xlsx'

# Load Excel file using Pandas
f = pd.ExcelFile(filepath)


# Define an empty list to store individual DataFrames
list_of_dfs = []
list_of_sheets = []

# Iterate through each worksheet
for sheet in f.sheet_names:

    # Parse data from each worksheet as a Pandas DataFrame
    df = f.parse(sheet)

    # And append it to the list
    list_of_dfs.append(df)
    list_of_sheets.append(sheet)



# Combine all DataFrames into one
data = pd.concat(list_of_dfs, ignore_index=True)
tel_nan = 0




for i in range(len(list_of_sheets)):
    text = "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"

    text = text + "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema> .\n"

    text = text + "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n"

    text = text + "\n"
    sheet = i
    print(list_of_dfs[sheet]["Label"][0])

    text = text + "<https://data.vlaanderen.be/id/conceptscheme/" + \
        str(list_of_dfs[sheet]["Klasse"][0]).replace(" ", "_") + ">  a skos:ConceptScheme ;\n"
    text = text + "<https://www.w3.org/ns/adms#status> <https://data.vlaanderen.be/id/concept/Status/ingebruik> ;\n"

    for language in languages:
        text = text + 'skos:definition """' + \
            translator.translate(
                str(list_of_dfs[sheet]["Definitie"][0]), dest=language).text + '"""@' + language + ' ;\n'
        text = text + 'skos:prefLabel "' + \
            translator.translate(
                str(list_of_dfs[sheet]["Label"][0]), dest=language).text + '"@' + language + ' ;\n'

    if {'subklassevan'}.issubset(list_of_dfs[sheet].columns):
        text = text + 'rdfs:subClassOf  <https://data.vlaanderen.be/id/concept/' + \
            str(list_of_dfs[sheet]["subklassevan"][i]) + '> ;\n'
            
    text = text + 'skos:prefLabel "' + str(list_of_dfs[sheet]["Label"][0]) + '"@nl ;\n'
    text = text + 'skos:definition """' + \
        str(list_of_dfs[sheet]["Definitie"][0]) + '"""@nl .\n'
        



        

    text = text + '\n'




    for i in range(len(list_of_dfs[sheet])):
        if (i ==0):
            continue
        print(str(list_of_dfs[sheet]["Klasse"][i]))
        
        if (str(list_of_dfs[sheet]["Klasse"][i]) == "Nan"):
            tel_nan= tel_nan + 1
            continue
        
        
        else:
            text = text + "<https://data.vlaanderen.be/id/concept/" + str(list_of_dfs[sheet]["Klasse"][0]).replace(" ", "_") + "/" + \
                str(list_of_dfs[sheet]["Klasse"][i]).replace(' ', '_') + ">  a skos:Concept ;\n"
            text = text + "<https://www.w3.org/ns/adms#status> <https://wegenenverkeer.data.vlaanderen.be/id/concept/DWMStatus/" + str(list_of_dfs[sheet]["Status"][i]) + "> ;\n"
            
            text = text + 'skos:definition """' + \
                str(list_of_dfs[sheet]["Definitie"][i]) + '"""@nl ;\n'
                
            text = text + 'skos:inscheme ' + \
                "<https://data.vlaanderen.be/id/conceptscheme/" + \
                str(list_of_dfs[sheet]["Klasse"][0]).replace(
                    " ", "_") + '> ;\n'

            text = text + 'skos:notation "' + \
                str(list_of_dfs[sheet]["Notation"][i]) + '" ;\n'
            text = text + 'skos:prefLabel "' + \
                str(list_of_dfs[sheet]["Label"][i]) + '"@nl ;\n'
                
            
            for language in languages:
                text = text + 'skos:definition """' + \
                    translator.translate(
                        str(list_of_dfs[sheet]["Definitie"][i]), dest=language).text + '"""@' + language + ' ;\n'
                text = text + 'skos:prefLabel "' + \
                    translator.translate(
                        str(list_of_dfs[sheet]["Label"][i]), dest=language).text + '"@' + language + ' ;\n'
                    
            if {'subklassevan'}.issubset(list_of_dfs[sheet].columns):
                text = text + 'rdfs:subClassOf  <https://data.vlaanderen.be/id/concept/' + \
                    str(list_of_dfs[sheet]["subklassevan"][i]) + '> ;\n'



            
            text = text + 'skos:topConceptOf <https://data.vlaanderen.be/id/conceptscheme/' + \
                str(list_of_dfs[sheet]["Klasse"][0]).replace(
                    " ", "_") + '> .\n'

            text = text + "\n"
        




    with open(str(list_of_dfs[sheet]["Klasse"][0]) + '.ttl', 'w') as f:
        f.write(text)
        
    print(str(tel_nan) + ' members niet kunnen parsen naar codelijst')
