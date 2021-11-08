#Task in Codecademy Analysing Stock Data

#Microsoft (NASDAQ:MSFT)
#Amazon (NASDAQ:AMZN)
#Apple (NASDAQ:AAPL)
#Alphabet (NASDAQ:GOOG)
#Facebook (NASDAQ:FB).

#Import Data Manipulation Packages
import pandas as pd
import numpy as np
import pandas_datareader as web
import matplotlib.pyplot as plt
#2)
#import the pandas data reader
# module as web. (Ensure the module is installed with pip install pandas-datareader on the command line)

#Step 1: Define Stocks
#Create a list named symbols containing the symbols for the top 5 tech stocks.

#Step 2: Create Dates
#Create a datetime object representing January 1st, 2019 named start_date and a datetime object representing July 1st, 2019 named end_date.

#Step 3: Retrieve Data
#Call the function web.get_data_yahoo() with arguments symbols, start_date and end_date and save the result to stock_data.

#Step 4: View Data
#View both stock_data and stock_data['Adj Close']. What information is stored in these DataFrames?

symbols = ['MSFT','AMZN','AAPL','GOOG','FB']
#datum
from datetime import datetime
start_date = datetime(2019,1,1)
end_date = datetime(2019,6,1)

#yahoo API
stock_data = web.get_data_yahoo(symbols,start_date,end_date)
print(stock_data)
print(stock_data['Adj Close'])

#3) 3. Plot the adjusted closing prices over time.
#Create a plot with matplotlib that shows the adjusted closing prices of each stock over time. Set the x label to "Date".
#Set the y label to "Adjusted Closing Price Over Time". Set the graph title to "Tech Stocks Adjusted Price".

stock_data['Adj Close'].plot()
plt.xlabel("Date")
plt.ylabel('Tech Stocks Adjusted Price')
plt.title('Tech Stocks Adjusted Price')
plt.show()

#4. Calculate and plot the daily simple rate of return over time.

stock_data['Adj Close'].pct_change().plot()

#5. Create subplots of daily simple rate of return

fig = plt.figure(figsize=(15,15))
ax1 = fig.add_subplot(321)
ax2 = fig.add_subplot(322)
ax3 = fig.add_subplot(323)
ax4 = fig.add_subplot(324)
ax5 = fig.add_subplot(325)
ax1.plot(stock_data['Adj Close']['AMZN'].pct_change())
ax1.set_title("Amazon")
ax2.plot(stock_data['Adj Close']['AAPL'].pct_change())
ax2.set_title("Apple")
ax3.plot(stock_data['Adj Close']['FB'].pct_change())
ax3.set_title("Facebook")
ax4.plot(stock_data['Adj Close']['MSFT'].pct_change())
ax4.set_title("Microsoft")
ax5.plot(stock_data['Adj Close']['GOOG'].pct_change())
ax5.set_title("Google")
plt.tight_layout()
plt.show()

#6. Calculate and plot the mean of each tech stock's daily simple rate of return
#Step 1: Calculate mean rate of return
#For each stock, calculate the mean daily simple rate of return.

#Step 2: Plot bar chart
#Use matplotlib to create a bar chart comparing the mean daily simple rate of return for each stock. Label the chart appropriately

#Step 3: Analyze mean rate of return
#Based on the mean rate of return, which stock would be the best option to invest in?

#mean rate of return
ror_AMZN = stock_data['Adj Close']['AMZN'].pct_change().mean()
ror_AAPL = stock_data['Adj Close']['AAPL'].pct_change().mean()
ror_FB = stock_data['Adj Close']['FB'].pct_change().mean()
ror_MSFT = stock_data['Adj Close']['MSFT'].pct_change().mean()
ror_GOOG = stock_data['Adj Close']['GOOG'].pct_change().mean()
ror_gesamt = [ror_AMZN,ror_AAPL,ror_FB,ror_MSFT,ror_GOOG]

#Alternativ in einer Zeile
stock_data_daily_returns = stock_data['Adj Close'].pct_change()

plt.bar(range(len(ror_gesamt)),ror_gesamt)
ax = plt.subplot()
ax.set_xticks(range(len(ror_gesamt)))
ax.set_xticklabels(["Amazon","Apple","Facebook", "Microsoft", "Google"])
plt.show()

#7. Calculate and plot the variance
#Step 1: Calculate the variance
#For each stock, calculate the variance of the mean daily simple rate of return.

#Step 2: Plot bar chart
#Use matplotlib to create a bar chart comparing the variance for each stock. Label the chart appropriately

#Step 3: Analyse the variance
#Based on the variance, which stock would be the riskiest to invest in?

#step 1
stock_var = stock_data_daily_returns.var()
stock_var

a_stock_var = []
for key in stock_var.keys():
    a_stock_var.append(stock_var[key])

plt.bar(range(len(stock_var)), a_stock_var)

plt.xticks(range(len(a_stock_var)), stock_var.keys())

# label chart
plt.xlabel("Tech_Stocks")
plt.ylabel("daily variance")
plt.title("daily variance")

# show graphic
plt.show()

#8. Calculate and plot the standard deviation
#Step 1: Calculate the standard deviation
#For each stock, calculate the standard deviation of the mean daily simple rate of return.

#Step 2: Plot the bar chart
#Use matplotlib to create a bar chart comparing the standard deviation of the mean daily simple rate of return of each stock. Label the chart appropriately

#Step 3: Analyze the standard deviation
#Based on the standard deviation of the rates of return, which stock would you choose to invest in and why?

#standard deviation
stock_std = stock_data_daily_returns.std()

#Step 2
#arrange Array

stock_data_std = []
for key in stock_std.keys():
    stock_data_std.append(stock_std[key])
stock_data_std

#Plot Std
plt.bar(range(len(stock_data_std)),stock_data_std)

plt.xticks(range(len(stock_data_std)), stock_std.keys())

# label chart
plt.xlabel("Tech_Stocks")
plt.ylabel("daily standard deviation")
plt.title("Daily Standard Seviation")

# show graphic
plt.show()

#9. Calculate the correlations
stock_data_daily_returns.corr()