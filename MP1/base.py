#Lista de dependencias :

# import numpy as np
# import pandas as pd
# import sklearn as sk
# import pprint as pp
#
# from sklearn.cluster import KMeans
# from sklearn.datasets import make_blobs
#
# import tkinter
# import matplotlib as mp
# from itertools import permutations

import datetime
import re

class DataRead(object):

        def __init__(self):
            self.file = "CSV/noshows-edit.csv"
            self.info = []

        def read(self):

            info_raw = open(self.file, "r")

            for line in info_raw:
                self.info.append(line.split(","))

            info_raw.close()

        def check(self):

            print(len(self.info))
            print(self.info[0])
            print(self.info[10])

        def save(self):

            info_clean = open("CSV/noshows-edit-test2.csv", "w+")

            for line in self.info:

                line = str(line)
                line = re.sub("]", "", line)
                line = re.sub("\[", "", line)
                line = re.sub("'", "", line)
                line = re.sub(" ", "", line)
                line = line + "\n"
                info_clean.write(line)

            info_clean.close()

        def dataclean(self):

            info = []

            for line in self.info:

                # line[10] = line[10][0:1]

                if line == self.info[0]:
                    line.append("NProblens")
                    line.append("Have_problem")
                    line.append("SD_Y")
                    line.append("SD_M")
                    line.append("SD_D")
                    line.append("AD_Y")
                    line.append("AD_M")
                    line.append("AD_D")
                    line.append("AD-SD")


                    info.append(line)

                else:
                    line[10] = line[10][0:1]
                    x = int(line[6])+int(line[7])+int(line[8])+int(line[9])
                    line.append(x)
                    if x != 0:
                        line.append(1)
                    else:
                        line.append(0)
                    for i in range(6, 10):
                        for ii in range(6, 10):
                            if int(line[ii]) != 0:
                                line[i] = int(line[i]) + (x / 4) ** 2
                    data = datetime.datetime.strptime(line[1], '%Y-%m-%dT%H:%M:%SZ')
                    data2 = datetime.datetime.strptime(line[2], '%Y-%m-%dT%H:%M:%SZ')
                    data3 = data2 - data
                    line.append(data.year)
                    line.append(data.month)
                    line.append(data.day)
                    line.append(data2.year)
                    line.append(data2.month)
                    line.append(data2.day)
                    line.append(data3.days)

                    info.append(line)


            self.info = info

teste = DataRead()
teste.read()
teste.check()
teste.dataclean()
teste.check()
teste.save()
