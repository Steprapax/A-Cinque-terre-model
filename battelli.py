import requests
import json
import xlsxwriter
import datetime
import xlrd

today = datetime.date.today()

for i in range(1, 100):

    sep = str(today)

    riomaggioreArrivals = []

    workbook = xlsxwriter.Workbook('arriviMonterosso' + sep + '.xlsx')
    Report_Sheet = workbook.add_worksheet()

    date_format = workbook.add_format({'num_format': 'dd/mm/yy hh:mm:ss'})

    response = requests.get(urlRiomaggiore)
    json_data = json.loads(response.text)

    riomaggioreArrivals.append("...")

    Report_Sheet.write_column(0, 0, riomaggioreArrivals, date_format)

    today = today + datetime.timedelta(days = 1)

    workbook.close()