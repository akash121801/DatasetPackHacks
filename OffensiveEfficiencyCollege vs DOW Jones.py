import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.style.use('ggplot')
from sklearn import linear_model
import sys

time=[2013, 2014, 2015, 2016, 2017, 2018,2019]
ADJOE=[106.788, 108.455, 108.04, 109.892, 109.6, 110.07, 108.926]
DOW=[15009, 16777, 17587, 17927, 21750, 25046, 26379]

fig, ax1=plt.subplots()
ax2=ax1.twinx()
ax1.scatter(time,ADJOE, label='ADJOE', color='green')
ax2.scatter(time,DOW, label='DOW', color='blue')
ax1.set_ylabel('ADJOE', color='g')
ax2.set_ylabel('DOW', color='b')
plt.title('Scoring Effciency VS Economy')
ax1.set_xlabel('Time')
ax1.set_ylim([106, 111])
ax2.set_ylim([15000, 27000])
plt.show()

#Linear Regression model to calculate DOW based on ADJOE

df=pd.DataFrame(list(zip(ADJOE, DOW)), columns=['ADJOE', 'DOW'])

x=df[['DOW']]
y=df[['ADJOE']]

regr=linear_model.LinearRegression()
regr.fit(x,y)

D = sys.argv[1]
print("Expected ADJOE for this year: ")
print(regr.predict([[float(D)]])[0])
