# Eric Messerich
# HW #3

import pandas as pd
import os

file_path = os.path.join("Resources","budget_data.csv")
#file_path = "Resources/budget_data.csv"

f = file("Budget_Data_Results.txt", "w")

df = pd.read_csv(file_path)

print >> f,("Eric Messerich")
print >> f,("HW #3")
print >> f,("")

num_months = len(df["Date"].value_counts())
print("Total Months: " + str(num_months))
print >> f,("Total Months: " + str(num_months))

total_profit = df["Profit/Losses"].sum()
print("Total: $" + str(total_profit))
print >> f,("Total: $" + str(total_profit))

profit_change = df["Profit/Losses"].diff()

df["Profit Change"] = profit_change

avg_profit_change = round((df["Profit Change"].sum())/(num_months -1),2)
print("Average  Change: $" + str(avg_profit_change))
print >> f,("Average  Change: $" + str(avg_profit_change))

df_greatest_increase = df.sort_values("Profit Change", ascending=False)
df_greatest_increase = df_greatest_increase.reset_index()
max_month = df_greatest_increase.loc[0,"Date"]
greatest_increase = df_greatest_increase.loc[0,"Profit Change"]
print("Greatest Increase in Profits: " + max_month + " ($" +str(greatest_increase) + ")")
print >> f,("Greatest Increase in Profits: " + max_month + " ($" +str(greatest_increase) + ")")

df_greatest_decrease = df.sort_values("Profit Change", ascending=True)
df_greatest_decrease = df_greatest_decrease.reset_index()
min_month = df_greatest_decrease.loc[0,"Date"]
greatest_decrease = df_greatest_decrease.loc[0,"Profit Change"]
print("Greatest Decrease in Profits: " + min_month + " ($" +str(greatest_decrease) + ")")
print >> f,("Greatest Decrease in Profits: " + min_month + " ($" +str(greatest_decrease) + ")")

f.close()
