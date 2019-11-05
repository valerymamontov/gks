## Парсинг XML-файла с помощью xml.dom.minidom
Есть сайт (fedstat.ru) с различными индикаторами и статистическими данными.
Например, можно посмотреть как в течение последних 27 лет изменялась "Ожидаемая продолжительность жизни"
в отдельно взятом регионе и по всей России.

Сайт работает нестабильно и попытка зарегистрироваться на нём не увенчалась успехом.

Без регистрации выгрузить статданные в эксель нельзя. Только в XML.
Вот так выглядит страница сайта:

![Image alt](https://github.com/valerymamontov/screenshots/blob/master/fedstat-001.png)

Если открыть XML-файл, то можно увидеть, что в самом начале он содержит три справочника:
1. список регионов
2. структура населения
3. тип поселения

![Image alt](https://github.com/valerymamontov/screenshots/blob/master/fedstat-002.png)

Ниже, после справочников, идут статданные. Видно, что они структурированы, т.е. представлены в виде "блоков":

---
		<generic:SeriesKey>
			<generic:Value concept="s_OKATO" value="643"/>
			<generic:Value concept="S_GRUP_2" value="2"/>
			<generic:Value concept="s_mest" value="w2:p_mest:11"/>
		</generic:SeriesKey>
		<generic:Attributes>
			<generic:Value concept="EI" value="год"/>
			<generic:Value concept="PERIOD" value="значение показателя за год"/>
		</generic:Attributes>
		<generic:Obs>
			<generic:Time>1991</generic:Time>
			<generic:ObsValue value="74,2"/>
		</generic:Obs>
---

![Image alt](https://github.com/valerymamontov/screenshots/blob/master/fedstat-003.png)

### Решение:
Для парсинга XML-файла я использовал python 3.7 и модуль xml.dom.minidom. 

Скрипт (script.py) обрабатывает XML, извлекает данные и сохраняет в CSV-файл.

Затем этот файл можно открыть в экселе и навести красоту. Поставить фильтры на заголовки.
Выделить заголовки цветом и т.д.
![Image alt](https://github.com/valerymamontov/screenshots/blob/master/fedstat-004.png)

Скрипт писался для обработки статданных по регионам, входящим в ЦФО. Для анализа выгружались данные за весь период, за все годы.

Если нужно обработать другие регионы и изменить годы, то сначала на сайте [fedstat.ru](https://www.fedstat.ru/indicator/31293) требуется:
- поставить нужные фильтры в столбце регионы
- выбрать годы
- скачать новый XML-файл

Затем в скрипте (script.py) модифицировать код в следующих строках:
- 3, где указано имя XML-файла
- 11-16, где перечисляется список регионов
- 24, где формируется заголовок и с помощью функции range идёт перечисление 1990-2018 годов

Скрипт писался в бесплатной IDE - PyCharm 2019.1.1 (Community Edition)
