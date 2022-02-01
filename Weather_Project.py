import csv
from typing import Dict
import matplotlib.pyplot as plt

TMAX = []
TMIN = []
WSMX = []
HAVG = []
RAIN = []

username = input("Hello, what is your name? > ")

with open('2016VizData.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    running = True
    while running == True:
        question = input(f"{username}, what data would you like to be shown? (TMAX, TMIN, RAIN, WSMX) > ")
        question2 = input(f"{username}, would you like to be shown data from a month or the year?")
        if question2 == 'month':
            question_month = input("What month would you like to be shown? (Type as a number, ex. 1, 2, 3...)")
        for row in reader:
            if question == 'TMAX' or question == 'TMIN' or question == 'RAIN' or question == 'WSMX':
                if question2 == 'year' or question2 == 'Year':
                    
