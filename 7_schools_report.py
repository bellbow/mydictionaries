"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the AAC, Big 12, Big Ten, and SEC divisons. This
information can be found in the ValueLabels file.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 50%
Display report for all universities that have a total price for in-state students living off campus over $50,000



"""

import json

infile = open('school_data.json','r')
schools = json.load(infile)
confrence_schools = [372,108,107,130]

print('AAC, Big 12, Big Ten, or SEC:')
for school in schools:
    if school['NCAA']['NAIA conference number football (IC2020)'] in confrence_schools:
        print(school['instnm'])   

print('\nWomen grad rate over 50:')
for school in schools:
    if type(school['Graduation rate  women (DRVGR2020)']) == int:
        if school['Graduation rate  women (DRVGR2020)'] > 50:
            print(school['instnm'])

print('\nIn-state price over 50000:')
for school in schools:
    if type(school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)']) == int:
        if school['Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)'] > 50000:
            print(school['instnm'])