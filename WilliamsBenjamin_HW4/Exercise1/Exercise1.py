import matplotlib.pyplot as plt
import numpy as np

fruitName = ['Apples','Oranges','Cherries','Watermelon']
fruitQuantity_2020 = [25, 25, 10, 18]
fruitQuantity_2021 = [22, 18, 9, 19]

fig, ax = plt.subplots(2, 2, figsize=(9, 7))
fig.suptitle("Fruit Quantities (2020 vs 2021)")

# (0,0) Line plot
ax[0][0].plot(fruitName, fruitQuantity_2020, color='red', label='2020')
ax[0][0].plot(fruitName, fruitQuantity_2021, color='blue', label='2021')
ax[0][0].set_title("Line Plot")
ax[0][0].set_ylabel("Quantity")
ax[0][0].legend()
ax[0][0].grid(True, alpha=0.3)

# (0,1) Scatter
ax[0][1].scatter(fruitName, fruitQuantity_2020, label='2020', marker='o')
ax[0][1].scatter(fruitName, fruitQuantity_2021, label='2021', marker='s')
ax[0][1].set_title("Scatter Plot")
ax[0][1].legend()
ax[0][1].grid(True, alpha=0.3)

# (1,0) Stack plot (area)
q2020 = np.array(fruitQuantity_2020)
q2021 = np.array(fruitQuantity_2021)

ax[1][0].stackplot(fruitName, q2020, q2021, labels=['2020', '2021'], colors=['b', 'c'])
ax[1][0].set_title("Stack Plot")
ax[1][0].set_ylabel("Quantity")
ax[1][0].legend(loc="upper right")

# (1,1) Pie chart
totals = (q2020 + q2021).tolist()
ax[1][1].pie(totals, labels=fruitName, autopct='%1.1f%%', startangle=90)
ax[1][1].set_title("Pie (2020+2021)")

plt.tight_layout()
plt.show()S
