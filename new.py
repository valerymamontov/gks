import xml.dom.minidom
dom = xml.dom.minidom.parse("data.xml")
dom.normalize()

codeList = dom.getElementsByTagName("structure:CodeList")[0]

myListOfRegions = ['643', '030', '14000000000', '15000000000', '17000000000', '20000000000', '24000000000', '29000000000', '34000000000', '38000000000', '42000000000', '46000000000', '54000000000', '61000000000', '66000000000', '68000000000', '28000000000', '70000000000', '78000000000', '45000000000']
dictRegions = {}
for i in codeList.getElementsByTagName("structure:Code"):
    dictTemp = {"%s" % i.getAttribute("value"):"%s" % i.getElementsByTagName("structure:Description")[0].firstChild.data}
    dictRegions.update(dictTemp)

allPop_allGender = []
allPop_women = []
allPop_men = []
cityPop_allGender = []
cityPop_women = []
cityPop_men = []
ruralPop_allGender = []
ruralPop_women = []
ruralPop_men = []

file = open("gks.txt", "a")
for key in dictRegions.keys():
    if key in myListOfRegions:
        file.write("%s; " % dictRegions[key])
        genSeries = dom.getElementsByTagName("generic:Series")
        for g in genSeries:
            codeOrg = g.getElementsByTagName("generic:Value")[0].getAttribute("value")
            codeGender = g.getElementsByTagName("generic:Value")[1].getAttribute("value")
            codePopulation = g.getElementsByTagName("generic:Value")[2].getAttribute("value")
            if (codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:11"):
                # file.write("%s; " % g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
                allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif (codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:11"):
                allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif (codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:11"):
                allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif (codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:12"):
                allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif (codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:12"):
                allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif (codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:12"):
                allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif (codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:13"):
                allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif (codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:13"):
                allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif (codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:13"):
                allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
        file.write("\n")
file.close()