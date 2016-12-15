import requests
from openpyxl import load_workbook

import os
# Python Image Library haven't been supported on Python3.X yet
# from PIL import Image
from io import BytesIO

from people.candidate import Candidate


def download_avatar(candidate, download_dir):
    if not os.path.exists(download_dir + os.path.sep + str(candidate.gender) + os.path.sep + str(candidate.province)):
        os.mkdir(download_dir + os.path.sep + str(candidate.gender) + os.path.sep + str(candidate.province))

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2882.4 Safari/537.36",
        "Accept - Encoding": "gzip, deflate, sdch"
    }
    response = requests.get(candidate.image, headers=headers)
    if response.status_code == 200:
        with open(download_dir, mode='wb') as f:
            f.write(BytesIO(response.content))
            f.flush()
            f.close()
    elif response.status_code == 403:
        print('Access Denied!')
    else:
        print('ERROR!')


def read_excel(excel_path):
    candidate_list = list()
    wb = load_workbook(excel_path)
    ws = wb.active
    for i in range(2, ws.max_row - 1):  # -1 means that the last row is null
        candidate = Candidate(uid=ws.cell(row=i, column=1).value, nickname=ws.cell(row=i, column=2).value,
                              age=ws.cell(row=i, column=3).value, height=ws.cell(row=i, column=4).value,
                              image=ws.cell(row=i, column=5).value, marriage=ws.cell(row=i, column=6).value,
                              education=ws.cell(row=i, column=7).value, work_location=ws.cell(row=i, column=8).value,
                              work_sublocation=ws.cell(row=i, column=9).value,
                              shortnote=ws.cell(row=i, column=10).value,
                              matchCondition=ws.cell(row=i, column=11).value,
                              randListTag=ws.cell(row=i, column=12).value,
                              province=ws.cell(row=i, column=13).value, gender=ws.cell(row=i, column=14).value)
        candidate_list.append(candidate)
        print(candidate)

    return candidate_list


if __name__ == '__main__':
    read_excel("D:/JiaYuan_Excel/女性用户-北京.xlsx")
