import xml.dom.minidom
from typing import TextIO

dom = xml.dom.minidom.parse("data.xml")
dom.normalize()

codeList = dom.getElementsByTagName("structure:CodeList")[0]

myListOfRegions = ['643', '030', '14000000000', '15000000000', '17000000000', '20000000000', '24000000000', '29000000000', '34000000000', '38000000000', '42000000000', '46000000000', '54000000000', '61000000000', '66000000000', '68000000000', '28000000000', '70000000000', '78000000000', '45000000000']
# этот "список" используется в качестве некого фильтра

myListOfYears = range(1990, 2018)
# этот "список" задаёт диапазон годов

dictRegions = {}
for i in codeList.getElementsByTagName("structure:Code"):
    dictTemp = {"%s" % i.getAttribute("value"):"%s" % i.getElementsByTagName("structure:Description")[0].firstChild.data}
    dictRegions.update(dictTemp)

file: TextIO = open("data.txt", "a")

file.write("Регион;Структура населения;Тип поселения;%s\n" % ';'.join(str(e) for e in myListOfYears))
# формирует заголовок

for key in dictRegions.keys():
    if key in myListOfRegions:

        allPop_allGender = [dictRegions[key]]
        allPop_women = [dictRegions[key]]
        allPop_men = [dictRegions[key]]
        cityPop_allGender = [dictRegions[key]]
        cityPop_women = [dictRegions[key]]
        cityPop_men = [dictRegions[key]]
        ruralPop_allGender = [dictRegions[key]]
        ruralPop_women = [dictRegions[key]]
        ruralPop_men = [dictRegions[key]]

        genSeries = dom.getElementsByTagName("generic:Series")
        for g in genSeries:
            codeOrg = g.getElementsByTagName("generic:Value")[0].getAttribute("value")
            codeGender = g.getElementsByTagName("generic:Value")[1].getAttribute("value")
            codePopulation = g.getElementsByTagName("generic:Value")[2].getAttribute("value")

            if codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:11":
                # allPop_allGender.append("%s;Оба пола;всё население" % dictRegions[key])
                allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:11":
                # allPop_women.append("%s;Женщины;всё население" % dictRegions[key])
                allPop_women.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:11":
                # allPop_men.append("%s;Мужчины;всё население" % dictRegions[key])
                allPop_men.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:12":
                # cityPop_allGender.append("%s;Оба пола;городское население" % dictRegions[key])
                cityPop_allGender.append(";%s" % g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:12":
                # cityPop_women.append("%s;Женщины;городское население" % dictRegions[key])
                cityPop_women.append(";%s" % g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:12":
                # cityPop_men.append("%s;Мужчины;городское население" % dictRegions[key])
                cityPop_men.append(";%s" % g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:13":
                # ruralPop_allGender.append("%s;Оба пола;сельское население" % dictRegions[key])
                ruralPop_allGender.append(";%s" % g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:13":
                # ruralPop_women.append("%s;Женщины;сельское население" % dictRegions[key])
                ruralPop_women.append(";%s" % g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            elif codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:13":
                # ruralPop_men.append("%s;Мужчины;сельское население" % dictRegions[key])
                ruralPop_men.append(";%s" % g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))

        if allPop_allGender is True: file.write("%s\n" % ';'.join(allPop_allGender))
        if allPop_women: file.write("%s\n" % ';'.join(allPop_women))
        if allPop_men: file.write("%s\n" % ';'.join(allPop_men))
        if cityPop_allGender: cityPop_allGender.append("\n")
        if cityPop_women: cityPop_women.append("\n")
        if cityPop_men: cityPop_men.append("\n")
        if ruralPop_allGender: ruralPop_allGender.append("\n")
        if allPop_allGender: ruralPop_women.append("\n")
        if allPop_allGender: ruralPop_men.append("\n")

file.close()