import matplotlib.pyplot as plt
import pandas as pd
from math import pi


def radar(data, maxval):
    # Code from https://python-graph-gallery.com/391-radar-chart-with-several-individuals/

    plt.clf()
    df = pd.DataFrame(data)

    # number of variable
    categories = list(df)[1:]
    N = len(categories)
    usernames = data['group']

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories)

    # Draw ylabels
    ax.set_rlabel_position(0)

    plt.yticks([25, 50, 75], ["25%", "50%", "75%"], color="grey", size=7)
    plt.ylim(0, maxval+10)

    # ------- PART 2: Add plots

    # Plot each individual = each line of the data
    # I don't do a loop, because plotting more than 3 groups makes the chart unreadable

    colours = ['b', 'g', 'r', 'c', 'm', 'y']

    for i in range(len(usernames)):
        values = df.loc[i].drop('group').values.flatten().tolist()
        values += values[:1]
        ax.plot(angles, values, colours[i], linewidth=1, linestyle='solid', label=usernames[i])
        ax.fill(angles, values, colours[i], alpha=0.1)

    # Add legend
    plt.legend(loc='lower right', bbox_to_anchor=(0.1, 0.1))
    plt.savefig('plot.png')
