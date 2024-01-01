"""
Author: Jacob Jones
Date: 11/10/23
"""

import numpy as np
import matplotlib.pyplot as plt
# Task 1: Create a list of demands normally distributed with mean 150 and stdev 20
demand_list = np.random.normal(150,20,1000) ## normal distribution of 1000 random #s with mean 150 and stdev 20
demand_list = demand_list.tolist() # creates list of demand instances from array

# convert demand instances to int using for loop
for x in range(0, len(demand_list)):
    demand_list[x] = int(demand_list[x])

# 2nd list, sales list: replace elements in the list which are greater than # manufacured in stock


# create a function which gives expected profit for a givel level on manufactured

def compute_profit(manufactured,unit_price,retail_price,disposal_cost):
    
    sales_list=[None]*len(demand_list)
     
    for x in range(0, len(demand_list)):
        if demand_list[x] > manufactured:
             sales_list[x] = manufactured
        else:
            sales_list[x] = demand_list[x]
            
    
    # total cost of manufacturing: $28.50
    # retail price: $150.00
    # Dispose of inventory end of each month: $8.50 per unit
    # total cost of disposing each extra unit of inventory (manufacturing + disposal cost): $37
    # Profit for each earbud sold (retail-total cost to manufacture): $121.50

    # 4th list, profit list: revenue - cost
    over_production = [None]*len(demand_list)
   # cost_price = 28.50
    profit= [None]*len(demand_list) #creates blank list size of demand list
    for x in range(0,len(demand_list)):
        if sales_list[x] < manufactured:
            over_production[x] = manufactured - sales_list[x]
            profit[x] = sales_list[x] * (retail_price - unit_price) - (disposal_cost * over_production[x])
        elif sales_list[x] > manufactured:
            profit[x] = sales_list[x] * (retail_price - unit_price) 
        else:
            profit[x] = manufactured*(retail_price-unit_price)
     
    average_profit = sum(profit)/len(profit)
    return average_profit

# Manual input for manufactured and cost prices
print('Please enter the following information, int or float type please:')
manufactured= int(input("Enter the number of units manufactured: "))
unit_price = float(input("Enter the production cost per unit: "))
retail_price =  float(input("Enter the retail price per unit: "))
disposal_cost = float(input("Enter the disposal cost per unit: "))

mean_profit = compute_profit(manufactured,unit_price,retail_price,disposal_cost) # call function with manual input values 


print('If you manufacture',manufactured, 'units with a unit price of',unit_price, ', a retail price of',retail_price, 
      ', and a disposal cost of',disposal_cost, '. The average profit is',mean_profit,'.')


# how many units should I manufacture?


#If I manufacture 200 units, I make $16,332.95   
#If I manufacture 150 units, I make $16,872.62 
#If I manufacture 100 units, I make $12,149.36
manufacture_list = range(140, 200)  # Our optimal value is between 140-190 units
profit_list = [None] * len(manufacture_list)  # avg profit of each of the potential manufacture values

for x in range(len(manufacture_list)):
    units = manufacture_list[x]
    profit_list[x] = compute_profit(units, unit_price, retail_price, disposal_cost)

max_profit = max(profit_list)
max_profit_index = profit_list.index(max_profit)
optimal_units = manufacture_list[max_profit_index]

print('A maximum profit of' ,max_profit, 'is achieved with' ,optimal_units, 'units')

plt.subplots(dpi = 100)
plt.scatter(manufacture_list,profit_list,  c= profit_list, cmap = 'Spectral', marker ='.') # c designates the values which will be colored
plt.title('Manufacturing Level Simulation')
plt.xlabel('Manufacture Level')
plt.ylabel('Profit')
plt.colorbar()
plt.grid(True)
