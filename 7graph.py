import numpy as np
import matplotlib.pyplot as plt


with open("settings.txt","r") as settings:
    settings = [float(i) for i in settings.read().split("\n")]


k = settings[2]
nt = settings[1]
print(nt,k)


data_new_array = np.loadtxt("data.txt",dtype = int)*k
data_time = np.array([i*nt*3.3/255 for i in range(data_new_array.size)])


fig, ax = plt.subplots(figsize=(8,8),dpi = 120)


ax.set_title("Процесс зарядки и разрядки конденсатора в RC-цепи",fontsize=15)
ax.set_ylabel("Напряжение на конденсаторе U,B",fontsize=10, fontweight="bold")
ax.set_xlabel("Время t,с",fontsize=10, fontweight="bold")


ax.grid(True)
ax.minorticks_on()
ax.grid(which='minor', color = 'lightgray', linestyle = '--')
ax.grid(which='major', color = 'dimgray', linestyle = '--')


ax.plot(data_time, data_new_array, linewidth=1, label = 'U(t)', marker = "D",ms = 3,markevery = 10,mec = "red")
ax.legend()

plt.show()

fig.savefig('graphic.png')
fig.savefig('graphic.svg')