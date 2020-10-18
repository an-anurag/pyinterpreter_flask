import mpld3
import matplotlib
import matplotlib.pyplot as plt



labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'

sizes = [15, 30, 45, 10]

explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')



fig, ax = plt.subplots()

ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',

        shadow=True, startangle=90)

ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

fig_var = [x[0] for x in locals().items() if isinstance(x[1], matplotlib.pyplot.Figure)][0]
print(fig_var)
globals()[fig_var] = matplotlib.pyplot.Figure
mpld3.save_json(fig_var, fileobj='json_fig.json')
