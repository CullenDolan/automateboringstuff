#! python 3
#import packages to handle dates
import time, datetime
#import packages to pull down data
import webbrowser #, requests, bs4

#constants for future calculations (Charles Schwabb)
contract_fee = 0.65
commission = 4.95
shares_contract = 100

#Gather user inputs
print('What stock ticker do you want to find? ')
in_stock = input()
#add the yahoo api to print the price
#
#
print('How many contracts will you buy (1 contract = 100 shares)? ')
in_contracts = int(input())
print('How much do you want to pay per share on the option contract? ')
in_buy = float(input())
print('What is the strike price? ')
in_strike = float(input())
#Get the expiration date and make sure its friday
print('What expiration date to you want, make sure to pick a Friday (MM/DD/YYYY)? ' )
in_date = input()
#set up for an while statement
in_date = datetime.datetime.strptime(in_date, '%m/%d/%Y')
#checks if it is a friday
n = in_date.weekday()
while n !=4:
   print('Make sure you pick a friday. What date do you want (MM/DD/YYYY)? ')
   in_date = input()
   in_date = datetime.datetime.strptime(in_date, '%m/%d/%Y')
   n = in_date.weekday()  
   in_date = str(in_date)
   in_date = time.mktime(datetime.datetime.strptime(in_date, "%Y-%m-%d %H:%M:%S").timetuple())
   in_date = in_date - 21600 #used to be 18000
   in_date = int(in_date)
   
print('What price do you want to sell your shares at? ')
in_sell = float(input())
#repeat the inputs to the user 
print('To Confirm: You want to buy ' + str(in_contracts) + ' contracts of ' 
      + str(in_stock) + ' stock, at a strike price of $' + str(in_strike) 
      + ' and you do not want to pay more than $' + str(in_buy) + ' per share.' )
#it would be interesting to add conditional statements that allowed the user to go back
#
#
#Calculate what they would make based on the information provided
#Option Purchase Price
opt_price = contract_fee * in_contracts + commission + in_buy * shares_contract * in_contracts
stock_purchase = commission + in_strike * in_contracts * shares_contract
print('And it will cost you a total of $' + str(opt_price) + 
      ' to buy the option and $' + str(stock_purchase) + 
      ' to purchase the stock at the strike price.')
#Stock Purchase price
stock_sale = in_sell * in_contracts * shares_contract - commission
profit = stock_sale - stock_purchase
roi = profit/stock_purchase * 100
print('If you sell at your target sell price, you will make a profit of $' 
      + str(int(profit)) + ' with an ROI of ' + str(round(roi,2)) + '%')
#Maybe also include the tax braket question and factor that in
#Will you hold this for longer than a year?
#What tax bracket are you in?
#calculate capital gains or income tax level 
#
webbrowser.open('https://finance.yahoo.com/quote/' + in_stock + '/options?p=' 
                + in_stock + '&date=' + str(in_date) + '&straddle=true')
