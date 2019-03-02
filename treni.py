import requests
import json
import xlsxwriter
import datetime

today = datetime.date.today()

head = 'http://www.viaggiatreno.it/viaggiatrenonew/resteasy/viaggiatreno/soluzioniViaggioNew/4731/4732/'
sep = str(today)
tail = 'T00:00:00'

arrivals = []

for i in range(1, 100):

    url = head + sep + tail

    response = requests.get(url)
    json_data = json.loads(response.text)

    for index, items in enumerate(json_data['soluzioni']):
        for i, item in enumerate(items['vehicles']):
            data = item['orarioArrivo'][:10]
            ora = item['orarioArrivo'][11:]
            arrivals.append(data + " " + ora)

    today = today + datetime.timedelta(days=1)

    sep = str(today)

workbook = xlsxwriter.Workbook('arriviTreniMonterosso.xlsx')
Report_Sheet = workbook.add_worksheet()

date_format = workbook.add_format({'num_format': 'dd/mm/yy hh:mm:ss'})

Report_Sheet.write_column(0, 0, arrivals, date_format)

workbook.close()