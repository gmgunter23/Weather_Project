from calendar import month
import csv
from typing import Dict
import matplotlib.pyplot as plt

ALTU = []
BEAV = []
NRMN = []
TISH = []
TULN = []

days = 0
days_2 = []

username = input("Hello, what is your name? > ")
question = input(f"{username}, what data would you like to be shown? (TMAX, TMIN, RAIN, WSMX) > ")
question2 = input(f"{username}, would you like to be shown data from a month or the year?")
if question2 == 'month':
    question_month = input("What month would you like to be shown? (Type as a number, ex. 1, 2, 3...)")

with open('2016VizData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    running = True
    while running == True:
        for row in reader:
            if question2 == 'Year' or question2 == 'year':
                if float(row('TMAX')) != -996 and float(row('TMAX')) != 996 and float(row('TMAX')) != -996 and float(row('TMAX')) != 996:
                    if row('STID') == 'ALTU':
                        ALTU.append(question)
                    if row('STID') == 'BEAV':
                        BEAV.append(question)
                    if row('STID') == 'NRMN':
                        NRMN.append(question)
                    if row('STID') == 'TISH':
                        NRMN.append(question)
                    if row('STID') == 'TULN':
                        TULN.append(question)
            if question2 == 'Month' or question2 == 'month':
                if row[month] == question_month:
                    if row('STID') == 'ALTU':
                        ALTU.append(question)
                    if row('STID') == 'BEAV':
                        BEAV.append(question)
                    if row('STID') == 'NRMN':
                        NRMN.append(question)
                    if row('STID') == 'TISH':
                        NRMN.append(question)
                    if row('STID') == 'TULN':
                        TULN.append(question)
                