import csv
import json
import itertools
import os

path = os.getcwd() + "/output"
print(path)

try: 
    os.mkdir(path) 
except OSError as error: 
    print(error)  
    

with open('input.csv', 'rU') as csvfile:
    all = list(csv.DictReader(csvfile))
    
data = []
rowcount = 1
for key, group in itertools.groupby(
    all, 
    key=lambda r: (r['docName'], r['templateName'], r['type'], r['url'], r['recipientName'], r['issuedByName'], r['docstoreName'], r['docStore'], r['idProofType'], r['idProofLocation'])):
    data.append({
    'name': key[0],           #docName
    '$template':{
        'name': key[1],
        'type': key[2],
         'url': key[3]
        },
        'recipient':{
        'name': key[4]            #recipientName      
    },
    'issuedBy':{
        'name': key[5]            #issuedByName            
    },
    'issuers':[{
        "name": key[6],           #docstoreName
        "documentStore": key[7],
        "identityProof": {
            "type": key[8],
            "location": key[9]
        }
    }]
    })

    mystr = json.dumps(data, indent=4)
    mystrAfterTruncate = mystr[1:-1]

    with open('tmp.json', 'w') as outfile:
        json.dump(data, outfile)

    #print( json.dumps(data, indent=4))
    #print('Truncation')
    #print(mystrAfterTruncate)
    
    text_file = open(os.path.join(path, "rawFile%s.json" %rowcount), "w")
    n = text_file.write(mystrAfterTruncate)
    text_file.close()
    
    rowcount+=1
    data.pop()

if os.path.exists("tmp.json"):
  os.remove("tmp.json")
else:
  print("The file does not exist")

print("End of program.")