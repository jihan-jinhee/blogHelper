import os
import _csv

class csvWrite():
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

class csvRead():
    def neighborListCSV():
        neighborListCSVPath = os.getcwd() + "\\result\\neighbor.csv"
        if not os.path.isfile(neighborListCSVPath):
            return None
        f = open(neighborListCSVPath, 'r', newline='')
        rdr = _csv.reader(f)
        neighborList = []
        for line in rdr:
            try:
                neighborList.append(line[0])
            except:
                # 이상한 문자
                pass

        return neighborList
        f.close()