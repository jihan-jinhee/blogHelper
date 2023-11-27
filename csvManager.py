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

    def deleteNeighborCSV(Count: int):
        resultPath = os.getcwd() + "\\result"
        if os.path.exists(resultPath):
            with open('./result/neighbor.csv', 'r') as file:
                # CSV 파일 읽기
                reader = _csv.reader(file)

                # 특정 행을 제외한 나머지 행들을 저장할 리스트
                rows = []

                # 각 행에 대해 작업 수행
                i = 0
                for row in reader:
                    i += 1
                    if i > Count:
                        rows.append(row)

            # 수정된 데이터로 CSV 파일 쓰기
            with open('./result/neighbor.csv', 'w', newline='') as file:
                # CSV 파일 작성
                writer = _csv.writer(file)

                # 수정된 데이터 작성
                writer.writerows(rows)

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