import pandas as pd
import numpy
import types
import time


def dealExcel(fileInput):
    print(fileInput)
    fileInput = "upload/"+fileInput
    print(fileInput)

    # frame = pd.read_excel("test.xls")
    frame = pd.read_excel(fileInput)
    # print(frame)
    for index, row in frame.iterrows():
        # print(row['Unnamed: 6'])  # 输出每行的索引值
        data = row['Unnamed: 6']
        if(type(data) == type("a")):
            dlist = list(data)
            if(len(dlist) == 10):
                # print(dlist)
                if((dlist[1] == '1') & (dlist[2] == '7')):
                    # print(dlist)
                    continue
                else:
                    frame.drop(index, axis=0, inplace=True)
            else:
                frame.drop(index, axis=0, inplace=True)
        else:
            frame.drop(index, axis=0, inplace=True)

    # print(frame)

    localtime = time.localtime(time.time())
    print(str(localtime.tm_mon)+"."+str(localtime.tm_mday) +
          " "+str(localtime.tm_hour)+str(localtime.tm_min))
    fileName = str(localtime.tm_mon)+"."+str(localtime.tm_mday) + \
        " "+str(localtime.tm_hour)+str(localtime.tm_min)
    frame.to_excel("output/"+fileName+".xlsx")
    fileNameNow = fileName+".xlsx"
    return fileNameNow


if __name__ == '__main__':
    dealExcel("1.29.xls")
