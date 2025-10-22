import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cars.csv", usecols=["Car", "Model", "CO2"])

ford = df[df["Car"] == "Ford"].copy()
merc = df[df["Car"] == "Mercedes"].copy()

avgFord = ford["CO2"].mean()
avgMerc = merc["CO2"].mean()

print("Ford CO₂ average:", avgFord)
print("Mercedes CO₂ average:", avgMerc)

fig, ax = plt.subplots(1, 2, figsize=(12, 4), sharey=True)

ax[0].plot(ford["Model"], ford["CO2"], marker="o", linestyle="-", label="Ford CO₂")
ax[0].axhline(y=avgFord, linestyle="--", color="gray", label="Average")
ax[0].set_title("Ford CO₂ Emissions")
ax[0].set_xlabel("Model")
ax[0].set_ylabel("CO₂")
ax[0].set_ylim(50, 150)
ax[0].tick_params(axis="x", rotation=60)
ax[0].legend()

ax[1].plot(merc["Model"], merc["CO2"], marker="o", color='red', linestyle="-", label="Mercedes CO₂")
ax[1].axhline(y=avgMerc, linestyle="--", color="gray", label="Average")
ax[1].set_title("Mercedes CO₂ Emissions")
ax[1].set_xlabel("Model")
ax[1].set_ylim(50, 150)
ax[1].tick_params(axis="x", rotation=60)
ax[1].legend()

plt.tight_layout()
plt.show()
