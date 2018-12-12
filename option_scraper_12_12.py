#! python3
import webbrowser, time, datetime, requests, bs4

#create constants for calculation
contract_fee = 0.75
commission = 6.95
shares_contract = 100

#Gather user inputs
print('What stock ticker do you want to find? ')
in_stock = input()
print('How many contracts will you buy (1 contract = 100 shares)? ')
in_contracts = int(input())
print('What is the purchase price? ')
in_buy = float(input())
print('What is the strike price? ')
in_strike = float(input())
print('What end date to you want (DD/MM/YYYY)? ' )
in_date = input()
in_date = time.mktime(datetime.datetime.strptime(in_date, "%d/%m/%Y").timetuple())
in_date = in_date - 18000
in_date = int(in_date)
print('What do you want to sell it at? ')
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
#
#
webbrowser.open('https://finance.yahoo.com/quote/' + in_stock + '/options?p=' 
                + in_stock + '&date=' + str(in_date))

res = requests.get('https://finance.yahoo.com/quote/' + in_stock + '/options?p=' 
                + in_stock + '&date=' + str(in_date))
res.status_code == requests.codes.ok
res.raise_for_status()
type(res)
len(res.text)
option_soup = bs4.BeautifulSoup(res.text)
type(option_soup)
option_soup.select('<td class="data-col1"')