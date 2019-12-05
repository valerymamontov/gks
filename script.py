import xml.dom.minidom

dom = xml.dom.minidom.parse("data.xml")
dom.normalize()

# -------------- формирование списка регионов --------------
code_list = ['643', '030', '14000000000', '15000000000', '17000000000', '20000000000', '24000000000',
             '29000000000', '34000000000', '38000000000', '42000000000', '46000000000', '54000000000',
             '61000000000', '66000000000', '68000000000', '28000000000', '70000000000', '78000000000', '45000000000']

dictRegions = {}
for i in dom.getElementsByTagName("structure:CodeList")[0].getElementsByTagName("structure:Code"):
    code = str(i.getAttribute("value"))
    if code in code_list:
        if code == '45000000000':
            dictRegions[code] = "Город Москва"
        else:
            dictRegions[code] = str(i.getElementsByTagName("structure:Description")[0].firstChild.data)


# -------------- открытие текстового файл и запись в него заголовка --------------
file = open("data.csv", "a")
file.write("Регион;Структура населения;Тип поселения;%s" % ';'.join(str(e) for e in range(1990, 2018)))


# -------------- создание всех возможных наборов данных --------------
# 1.всё население, Оба пола           2. всё население, Женщины           3. всё население, Мужчины
# 4.городское население, Оба пола     5. городское население, Женщины     6. городское население, Мужчины
# 7.сельское население, Оба пола      8. сельское население, Женщины      9. сельское население, Мужчины

sl = [["w2:p_mest:11", "12"], ["w2:p_mest:11", "2"], ["w2:p_mest:11", "3"],
      ["w2:p_mest:12", "11"], ["w2:p_mest:12", "2"], ["w2:p_mest:12", "3"],
      ["w2:p_mest:13", "11"], ["w2:p_mest:13", "2"], ["w2:p_mest:13", "3"]]


# -------------- последовательный перебор всех наборов данных --------------
for m in range(len(sl)):

    # -------------- условия --------------
    if sl[m][0] == "w2:p_mest:11":
        population = "всё население"
    elif sl[m][0] == "w2:p_mest:12":
        population = "городское население"
    elif sl[m][0] == "w2:p_mest:13":
        population = "сельское население"
    else:
        population = ""

    if sl[m][1] == "12":
        gender = "Оба пола"
    elif sl[m][1] == "2":
        gender = "Женщины"
    elif sl[m][1] == "3":
        gender = "Мужчины"
    else:
        gender = ""

    # -------------- перебор всех Регионов --------------
    for key in dictRegions.keys():
        genSeries = dom.getElementsByTagName("generic:Series")

        oneString = ""

        for g in genSeries:
            codeOrg = g.getElementsByTagName("generic:Value")[0].getAttribute("value")
            codeGender = g.getElementsByTagName("generic:Value")[1].getAttribute("value")
            codePopulation = g.getElementsByTagName("generic:Value")[2].getAttribute("value")

            if codeOrg == key and codeGender == sl[m][1] and codePopulation == sl[m][0]:
                if len(oneString) == 0:
                    oneString = "\n{a};{b};{c};{d}".format(
                        a=dictRegions[key],
                        b=gender,
                        c=population,
                        d=g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))
                else:
                    oneString += ";{}".format(g.getElementsByTagName("generic:ObsValue")[0].getAttribute("value"))

        # -------------- запись строки с данными по одному Региону в файл --------------
        file.write(oneString)

file.close()
