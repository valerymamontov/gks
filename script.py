import xml.dom.minidom

dom = xml.dom.minidom.parse("data.xml")
dom.normalize()



# -------------- формирование списка регионов
dictRegions = {}
for i in dom.getElementsByTagName("structure:CodeList")[0].getElementsByTagName("structure:Code"):
    if i.getAttribute("value") in ['643', '030', '14000000000', '15000000000', '17000000000', '20000000000',
                                   '24000000000', '29000000000', '34000000000', '38000000000', '42000000000',
                                   '46000000000', '54000000000', '61000000000', '66000000000', '68000000000',
                                   '28000000000', '70000000000', '78000000000', '45000000000']:
        if i.getAttribute("value") == '45000000000':
            dictTemp = {"%s" % i.getAttribute("value"):"Город Москва"}
        else:
            dictTemp = {"%s" % i.getAttribute("value"):"%s" % i.getElementsByTagName("structure:Description")[0].firstChild.data}
        dictRegions.update(dictTemp)


# -------------- открытие текстового файл и запись в него заголовка
file = open("data.csv", "a")
file.write("Регион;Структура населения;Тип поселения;%s" % ';'.join(str(e) for e in range(1990, 2018)))


# -------------- создание всех возможных наборов данных
# всё население, Оба пола           -- всё население, Женщины           -- всё население, Мужчины
# городское население, Оба пола     -- городское население, Женщины     -- городское население, Мужчины
# сельское население, Оба пола      -- сельское население, Женщины      -- сельское население, Мужчины

sl = [["w2:p_mest:11", "12"], ["w2:p_mest:11", "2"], ["w2:p_mest:11", "3"],
      ["w2:p_mest:12", "11"], ["w2:p_mest:12", "2"], ["w2:p_mest:12", "3"],
      ["w2:p_mest:13", "11"], ["w2:p_mest:13", "2"], ["w2:p_mest:13", "3"]]


# -------------- последовательный перебор всех наборов данных
for m in range(len(sl)):

    # -------------- условия --------------
    if sl[m][0] == "w2:p_mest:11": population = "всё население"
    elif sl[m][0] == "w2:p_mest:12": population = "городское население"
    elif sl[m][0] == "w2:p_mest:13": population = "сельское население"
    else: population = ""

    if sl[m][1] == "12": gender = "Оба пола"
    elif sl[m][1] == "2": gender = "Женщины"
    elif sl[m][1] == "3": gender = "Мужчины"
    else: gender = ""

    # -------------- перебор всех Регионов
    for key in dictRegions.keys():
        genSeries = dom.getElementsByTagName("generic:Series")

        oneString = ""

        for g in genSeries:
            codeOrg = g.getElementsByTagName("generic:Value")[0].getAttribute("value")
            codeGender = g.getElementsByTagName("generic:Value")[1].getAttribute("value")
            codePopulation = g.getElementsByTagName("generic:Value")[2].getAttribute("value")

            if codeOrg == key and codeGender == sl[m][1] and codePopulation == sl[m][0]:
                if len(oneString) == 0:
                    oneString = "\n%s;%s;%s;%s" % (
                        dictRegions[key],
                        gender,
                        population,
                        g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
                else:
                    oneString += ";%s" % g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value")

        # -------------- запись строки с данными по одному Региону в файл
        file.write(oneString)


file.close()