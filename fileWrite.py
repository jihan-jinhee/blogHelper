import os
import _csv

class ExcelWrite():
    def neighborListCSV(neighborList: list):
        resultPath = os.getcwd() + "\\result"
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        f = open('./result/neighbor.csv', 'w', newline='')
        wr = _csv.writer(f)
        for neighbor in neighborList:
            try:
                wr.writerow([neighbor])
            except:
                # 이상한 문자
                pass

        f.close()