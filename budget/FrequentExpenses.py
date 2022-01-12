from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()
expenses.read_expenses("data/spending_data.csv")

spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)

# get top 5 categories
top5 = spending_counter.most_common(5)

# split dictionary into two lists
categories,count = zip(*top5)

# generate bar chart with expenses
fig,ax = plt.subplots()
ax.bar(categories, count)
ax.set_title("# of Purchases by Category")
plt.show()