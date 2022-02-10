import csv
from typing import Dict
import matplotlib.pyplot as plt

ALTU_y = []
ALTU_x = []
BEAV_y = []
BEAV_x = []
NRMN_y = []
NRMN_x = []
TISH_y = []
TISH_x = []
TULN_y = []
TULN_x = []

days = 0
days_2 = []

username = input("Hello, what is your name? > ")
question = input(f"{username}, what data would you like to be shown? (TMAX, TMIN, RAIN, WSMX, HAVG) > ")
question2 = input(f"{username}, would you like to be shown data from a month or the year? > ")
if question2 == 'month':
    question_month = input("What month would you like to be shown? (Type as a number, ex. 1, 2, 3...) > ")

with open('2016VizData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if question2 == 'Year' or question2 == 'year':
            if float(row['TMAX']) != -996 and float(row['TMIN']) != 996 and float(row['WSMX']) != -996 and float(row['HAVG']) != -996 and float(row['RAIN']) != -996:
                if row['STID'] == 'ALTU':
                    ALTU_y.append(float(row[question])) 
                    ALTU_x.append(row['DAY'])
                if row['STID'] == 'BEAV':
                    BEAV_y.append(float(row[question]))
                    BEAV_x.append(row['DAY'])
                if row['STID'] == 'NRMN':
                    NRMN_y.append(float(row[question]))
                    NRMN_x.append(row['DAY'])
                if row['STID'] == 'TISH':
                    TISH_y.append(float(row[question]))
                    TISH_x.append(row['DAY'])
                if row['STID'] == 'TULN':
                    TULN_y.append(float(row[question]))
                    TULN_x.append(row['DAY'])
        if question2 == 'Month' or question2 == 'month':
            if float(row['TMAX']) != -996 and float(row['TMIN']) != 996 and float(row['WSMX']) != -996 and float(row['HAVG']) != -996 and float(row['RAIN']) != -996:
                if row["MONTH"] == question_month:
                    if row['STID'] == 'ALTU':
                        ALTU_y.append(float(row[question]))
                        ALTU_x.append(row['DAY'])
                    if row['STID'] == 'BEAV':
                        BEAV_y.append(float(row[question]))
                        BEAV_x.append(row['DAY'])
                    if row['STID'] == 'NRMN':
                        NRMN_y.append(float(row[question]))
                        NRMN_x.append(row['DAY'])
                    if row['STID'] == 'TISH':
                        TISH_y.append(float(row[question]))
                        TISH_x.append(row['DAY'])
                    if row['STID'] == 'TULN':
                        TULN_y.append(float(row[question]))
                        TULN_x.append(row['DAY'])

plt.plot(ALTU_x, ALTU_y, marker='o')
plt.plot(BEAV_x, BEAV_y, marker='o')
plt.plot(NRMN_x, NRMN_y, marker='o')
plt.plot(TISH_x, TISH_y, marker='o')
plt.plot(TULN_x, TULN_y, marker='o')
plt.title(f"{question}", fontsize = 14)
plt.xlabel('Day', fontsize = 14)
if question == 'TMAX' or question == 'TMIN':
    plt.ylabel('Temperature(F)', fontsize = 14)
if question == 'RAIN':
    plt.ylabel('Rain Total', fontsize = 14)
if question == 'WSMX':
    plt.ylabel('Wind Speed Max', fontsize = 14)
if question == 'HAVG':
    plt.ylabel('Humidity totals', fontsize = 14)
plt.legend(['ALTU', 'BEAV', 'NRMN', 'TISH', 'TULN'])
plt.show()