import xml.dom.minidom

dom = xml.dom.minidom.parse("data.xml")
dom.normalize()

# -------------- условия --------------
# if codeGender == "12": gender = "Оба пола"
# elif codeGender == "2": gender = "Женщины"
# elif codeGender == "3": gender = "Мужчины"
#
# if codePopulation == "w2:p_mest:11": population = "всё население"
# elif codePopulation == "w2:p_mest:12": population = "городское население"
# elif codePopulation == "w2:p_mest:13": population = "сельское население"
# -------------- ******* --------------

def funcAddInList(codeOrg, key, codeGender, codePopulation):
    if codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:11":
        if len(allPop_allGender) == 0:
            allPop_allGender.append(dictRegions[key])
            allPop_allGender.append("Оба пола")
            allPop_allGender.append("всё население")
            allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            return allPop_allGender
        else:
            allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            return allPop_allGender

    elif codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:11":
        if len(allPop_women) == 0:
            allPop_women.append("%s,Женщины,всё население,%s" % (dictRegions[key], g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value")))
            return allPop_women
        else:
            allPop_women.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            return allPop_women

    elif codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:11":
        if len(allPop_men) == 0:
            allPop_men.append("%s,Мужчины,всё население,%s" % (dictRegions[key], g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value")))
            return allPop_men
        else:
            allPop_men.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            return allPop_men

    elif codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:12":
        if len(cityPop_allGender) == 0:
            cityPop_allGender.append("%s,Оба пола,городское население,%s" % (dictRegions[key], g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value")))
            return cityPop_allGender
        else:
            cityPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            return cityPop_allGender

    elif codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:12":
        if len(cityPop_women) == 0:
            cityPop_women.append("%s,Женщины,городское население,%s" % (dictRegions[key], g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value")))
            return cityPop_women
        else:
            cityPop_women.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            return cityPop_women

    elif codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:12":
        if len(cityPop_men) == 0:
            cityPop_men.append("%s,Мужчины,городское население,%s" % (dictRegions[key], g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value")))
            return cityPop_men
        else:
            cityPop_men.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            return cityPop_men

    elif codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:13":
        if len(ruralPop_allGender) == 0:
            ruralPop_allGender.append("%s,Оба пола,сельское население,%s" % (dictRegions[key], g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value")))
            return ruralPop_allGender
        else:
            ruralPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            return ruralPop_allGender

    elif codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:13":
        if len(ruralPop_women) == 0:
            ruralPop_women.append("%s,Женщины,сельское население,%s" % (dictRegions[key], g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value")))
            return ruralPop_women
        else:
            ruralPop_women.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            return ruralPop_women

    elif codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:13":
        if len(ruralPop_men) == 0:
            ruralPop_men.append("%s,Мужчины,сельское население,%s" % (dictRegions[key], g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value")))
            return ruralPop_men
        else:
            ruralPop_men.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            return ruralPop_men


dictRegions = {}
for i in dom.getElementsByTagName("structure:CodeList")[0].getElementsByTagName("structure:Code"):
    dictTemp = {"%s" % i.getAttribute("value"):"%s" % i.getElementsByTagName("structure:Description")[0].firstChild.data}
    dictRegions.update(dictTemp)

file = open("data.txt", "a")
file.write("Регион;Структура населения;Тип поселения;%s\n" % ';'.join(str(e) for e in range(1990, 2018)))

for key in dictRegions.keys():
    if key in ['643', '030', '14000000000', '15000000000', '17000000000', '20000000000', '24000000000', '29000000000',
               '34000000000', '38000000000', '42000000000', '46000000000', '54000000000', '61000000000', '66000000000',
               '68000000000', '28000000000', '70000000000', '78000000000', '45000000000']:

        allPop_allGender = []
        allPop_women = []
        allPop_men = []
        cityPop_allGender = []
        cityPop_women = []
        cityPop_men = []
        ruralPop_allGender = []
        ruralPop_women = []
        ruralPop_men = []

        genSeries = dom.getElementsByTagName("generic:Series")
        for g in genSeries:
            codeOrg = g.getElementsByTagName("generic:Value")[0].getAttribute("value")
            codeGender = g.getElementsByTagName("generic:Value")[1].getAttribute("value")
            codePopulation = g.getElementsByTagName("generic:Value")[2].getAttribute("value")
            funcAddInList(codeOrg, key, codeGender, codePopulation)
            # if codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:11":
            #     if len(allPop_allGender) == 0:
            #         # allPop_allGender.append(dictRegions[key])
            #         # allPop_allGender.append("Оба пола")
            #         # allPop_allGender.append("всё население")
            #         # allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            #         allPop_allGender.append("%s,Оба пола,всё население,%s" % (dictRegions[key], g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value")))
            #     else:
            #         allPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))

            # if codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:11":
            # # elif codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:11":
            #     # allPop_women.append("%s;Женщины;всё население" % dictRegions[key])
            #     allPop_women.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            # elif codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:11":
            #     # allPop_men.append("%s;Мужчины;всё население" % dictRegions[key])
            #     allPop_men.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            # elif codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:12":
            #     # cityPop_allGender.append("%s;Оба пола;городское население" % dictRegions[key])
            #     cityPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            # elif codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:12":
            #     # cityPop_women.append("%s;Женщины;городское население" % dictRegions[key])
            #     cityPop_women.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            # elif codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:12":
            #     # cityPop_men.append("%s;Мужчины;городское население" % dictRegions[key])
            #     cityPop_men.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            # elif codeOrg == key and codeGender == "12" and codePopulation == "w2:p_mest:13":
            #     # ruralPop_allGender.append("%s;Оба пола;сельское население" % dictRegions[key])
            #     ruralPop_allGender.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            # elif codeOrg == key and codeGender == "2" and codePopulation == "w2:p_mest:13":
            #     # ruralPop_women.append("%s;Женщины;сельское население" % dictRegions[key])
            #     ruralPop_women.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
            # elif codeOrg == key and codeGender == "3" and codePopulation == "w2:p_mest:13":
            #     # ruralPop_men.append("%s;Мужчины;сельское население" % dictRegions[key])
            #     ruralPop_men.append(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))

        if allPop_allGender:
            file.write("%s\n" % ';'.join(allPop_allGender))
        if allPop_women: file.write("%s\n" % ';'.join(allPop_women))
        if allPop_men: file.write("%s\n" % ';'.join(allPop_men))
        if cityPop_allGender: file.write("%s\n" % ';'.join(cityPop_allGender))
        if cityPop_women: file.write("%s\n" % ';'.join(cityPop_women))
        if cityPop_men: file.write("%s\n" % ';'.join(cityPop_men))
        if ruralPop_allGender: file.write("%s\n" % ';'.join(ruralPop_allGender))
        if allPop_allGender: file.write("%s\n" % ';'.join(ruralPop_women))
        if allPop_allGender: file.write("%s\n" % ';'.join(ruralPop_men))


# print(len(allPop_allGender), " - ", len(allPop_allGender1))
# for row in allPop_allGender1:
#     for elem in row:
#         file.write("%s\n" % elem)
# file.write(allPop_women1)
file.close()