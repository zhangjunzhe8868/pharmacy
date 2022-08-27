'''
output drug_name, num_prescriber, total_cost
select drug_name, sum(drug_cost), count(*) from table group by drug_name order by sum(drug_cost) desc, count(*) desc

'''

data=[]
drugList={}
drugCost={}
outList=[]

with open('itcont.txt', 'r') as f:
    lines = f.readlines()
    firstLine=lines[0].replace('\n','')
    title=firstLine.split(',')
    for i in range(1, len(lines)):
        temp=lines[i].replace('\n','')
        data.append(temp.split(','))

drugNameIdx=title.index('drug_name')
drugCostIdx=title.index('drug_cost')

for i in range(len(data)):
    drugList[data[i][drugNameIdx]]=drugList.get(data[i][drugNameIdx],0)+1
    drugCost[data[i][drugNameIdx]]=drugCost.get(data[i][drugNameIdx],0)+int(data[i][drugCostIdx])

#combine to a tuple, then double sort
for name in range(len(drugList)):
    outList.append((list(drugList.keys())[name], drugList[list(drugList.keys())[name]], drugCost[list(drugList.keys())[name]]))
outList.sort(key=lambda x:[x[2],x[1],x[0]], reverse=True)

with open('top_cost_drug.txt','w') as f:
    f.write('drug_name,num_prescriber,total_cost\n')
    for row in range(len(drugList)):
        rowtxt = '{},{},{}\n'.format(outList[row][0],outList[row][1],outList[row][2])
        f.write(rowtxt)
    f.close()
