import matplotlib.pyplot as plt

# Data to plot
labels = ['White', 'Hispanic', 'African-American', 'Asian', 'Multiracial', 'Native American or Alaska Native', 'Native Hawaiian or Pacific Islander']
sizes = [249925000, 57850000, 43225000, 18525000, 8450000, 4225000, 650000]
colors = ['blue', 'green', 'red', 'yellow', 'magenta', 'orange', 'cyan']
explode = (0, 0, 0, 0, 0, 0, 0)  # explode 1st slice

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
