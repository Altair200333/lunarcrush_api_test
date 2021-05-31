import matplotlib.pyplot as plt
import numpy as np

#takes plots to draw as array of dictionaries with fileds: ['data', 'label', <x>, <same>, <sc>]
#Optional arguments:
#x - axis to use as X
#same - draw current plot on top of previous
#sc - scatter plot
def showPlots(plots):
    colors = ['#06d6a0', '#ee6c4d', '#277da1','#5a189a','#f3722c']
    plotCount = 0
    
    for i in range(len(plots)):
        if 'same' not in plots[i] or plots[i]['same'] == False:
            plotCount+=1
            
    fig, axs = plt.subplots(plotCount)
    if plotCount == 1:
        axs = [axs]
    pid = 0
    for i in range(len(plots)):
        if 'same' in plots[i] and plots[i]['same'] == True and pid > 0:
            pid -= 1   
        else:
            axs[pid].grid()
        if 'x' not in plots[i]:
            if 'sc' in plots[i] and plots[i]['sc'] == True:
                axs[pid].scatter(plots[i]['data'], label = plots[i]['label'], color = colors[i%len(colors)])
            else:
                axs[pid].plot(plots[i]['data'], label = plots[i]['label'], color = colors[i%len(colors)])
        else:
            if 'sc' in plots[i] and plots[i]['sc'] == True:
                axs[pid].scatter(plots[i]['x'][:len(plots[i]['data'])], plots[i]['data'], label = plots[i]['label'], color = colors[i%len(colors)])
            else:
                axs[pid].plot(plots[i]['x'][:len(plots[i]['data'])], plots[i]['data'], label = plots[i]['label'], color = colors[i%len(colors)])

        
        axs[pid].legend(loc = 'upper right')
        
        pid+=1