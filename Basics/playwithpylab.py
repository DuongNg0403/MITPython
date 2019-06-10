import pylab

#set line width
pylab.rcParams['lines.linewidth'] = 4
#set font size for titles
pylab.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
pylab.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
pylab.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
pylab.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
pylab.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
pylab.rcParams['ytick.major.size'] = 7
#set size of markers
pylab.rcParams['lines.markersize'] = 10

principal = 10000
interest_Rate = 0.05
years = 20
value = []
for i in range(years + 1):
    value.append(principal)
    principal+=principal*interest_Rate

pylab.plot(value, 'b-', linewidth = 15)
pylab.title("5% Compound Interest", fontsize = "xx-large")
pylab.xlabel("Years", fontsize = 'x-small')
pylab.ylabel("Principal", size = 'xx-large')
pylab.show()