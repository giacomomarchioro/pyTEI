from pymongo import MongoClient
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
from confidenziale import databaseaddress_capitolare_mongo,secret_key
client = MongoClient(databaseaddress_capitolare_mongo)
var = client.capitolare.codici.find_one({'segnatura_id': "m0043_0"}) 
#https://www.tei-c.org/release/doc/tei-p5-doc/it/html/MS.html
import xml.etree.ElementTree as ET

currentyear = 2021


p = ET.Element("TEI")
p.set("xmlns","http://www.tei-c.org/ns/1.0") 
p.set("xml:lang","it")
teiHeader = ET.SubElement(p,'teiHeader')
fileDesc = ET.SubElement(teiHeader,'teiHeader')
publicationStmt = ET.SubElement(teiHeader,'publicationStmt')
availability = ET.SubElement(publicationStmt,'availability')
ab = ET.SubElement(availability,'ab')
ab.text = f"Copyleft {currentyear} Università di Verona"
                            
sourceDesc = ET.SubElement(teiHeader,'sourceDesc')
msDesc = ET.SubElement(sourceDesc, 'msDesc')
# Mandatory
msIdentifier = ET.SubElement(sourceDesc, 'msIdentifier')
# The msIdentifier element is intended to provide an unambiguous means of uniquely 
# identifying a particular manuscript. This may be done in a struct ured way, by providing 
# information about the holding institution and the call number, shelfmark, or other 
# identifier used to indicate its location within that institution. Alternatively, or in 
# addition, a manuscript may be identified simply by a commonly used name.
country = ET.SubElement(msIdentifier, 'country')
country.text = "Italy"
# contiene il nome di un'unità geopolitica, come una nazione, un paese, una colonia, 
# o un'unione di stati, che sia più ampia o amministrativamente superiore rispetto a una
# regione ma di dimensioni inferiori rispetto a un blocco
region = ET.SubElement(msIdentifier, 'region')
region.text = "Veneto"
settlement = ET.SubElement(msIdentifier, 'settlement')
settlement.text = "Verona"
institution = ET.SubElement(msIdentifier, 'institution')
institution.text ="Biblioteca Capitolare di Verona"
institution.set("xml:lang","it")

#repository = ET.SubElement(msIdentifier, 'repository')
#repository.text = "Cavou della biblioteca"
collection = ET.SubElement(msIdentifier, 'collection')
collection.text = "Fondo manoscritti Biblioteca Capitolare"
collection.set("xml:lang","it")
# for i in names
# un qualsiasi nome alternativo non strutturato utilizzato per un manoscritto,
# per esempio ‘ocellus nominum’, o soprannome
msName = ET.SubElement(msIdentifier, 'msName')
msName.text = "VAR Titolo spangolo? VAR"
msName.set("xml:lang",'la') # settare la lingua
idno = ET.SubElement(msIdentifier, 'idno')
idno.text = var['descrizione_esterna']['Segnatura']


altIdentifier = ET.SubElement(msIdentifier, 'altIdentifier')
altIdentifier.set('type','SC')
# collocazione!
# Not mandatory
#head = ET.SubElement(sourceDesc, 'head')
#head.text('Marsilius de Inghen, Abbreviata phisicorum Aristotelis; Italy,1463.')
#MS CONTENTS
msContents = ET.SubElement(sourceDesc, 'msContents ')
summary = ET.SubElement(msContents, 'summary ')
summary.text = "VAR un manoscritto importnate VAR"
items = ['VAR_descrizione_intere_VAR']
# Descrizione interna
items = var['descrizione_interna']
for ind,item in enumerate(items):
    msItem = ET.SubElement(msContents, 'msItem')
    msItem.set("n",str(ind+1))
    locus = ET.SubElement(msItem, 'locus')
    locus.text = item['carte']
    locus.text = item['carte']
    locus.set("from",item['carte'].split("-")[0])
    locus.set("to",item['carte'].split("-")[1])
    title = ET.SubElement(msItem, 'title')
    title.text = item['titolo']
    author = ET.SubElement(msItem, 'author')
    author.text = item['author']
    author.set("xml:lang",'la')
    incipit = ET.SubElement(msItem, 'incipit')
    incipit.text = item['incipit']
    incipit.set("xml:lang",'la')
    explicit = ET.SubElement(msItem, 'explicit')
    explicit.text = item['explicit']
    explicit.set("xml:lang",'la')
    rubric = ET.SubElement(msItem, 'rubric')
    rubric.text = item['rubric']
    # si potrebbe aggiungere la bibliografia
    # bibl = ET.SubElement(msItem, 'bibl')

physDesc = ET.SubElement(sourceDesc , 'physDesc')
history = ET.SubElement(sourceDesc, 'history')
additional = ET.SubElement(sourceDesc, 'additional')
msPart = ET.SubElement(sourceDesc, 'msPart')
msFrag = ET.SubElement(sourceDesc, 'msFrag')
