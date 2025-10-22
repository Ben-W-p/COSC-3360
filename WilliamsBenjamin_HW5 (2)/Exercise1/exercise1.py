import matplotlib.pyplot as plt

min = int(input('Enter min value for the x: '))
max = int(input('Enter max value for the x: '))

x = list(range(min, max + 1))

y = [X if X >= 0 else -X for X in x] 

color = input("Enter color: ")
marker = input("Enter marker: ")
markersize = int(input("Enter marker size: "))
linestyle = input("Enter linestyle: ")
linewidth = float(input("Enter linewidth: "))
label = input("Enter label: ")
loc = input("Enter legend location: ")
xlabel = input("Enter x-label: ")
ylabel = input("Enter y-label: ")
title = input("Enter title: ")

plt.plot(x, y, color=color, marker=marker, markersize=markersize,
         linestyle=linestyle, linewidth=linewidth, label=label)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.title(title)
plt.legend(loc=loc)
plt.show()