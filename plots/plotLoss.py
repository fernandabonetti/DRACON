import json
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import numpy as np

def main():
	if len(sys.argv) < 1:
		exit(1)

	x= []
	y = []
	with open('loss.csv', 'r') as fp:
		for line in fp.readlines():
			y.append(float(line))  
	
	mean = []
	top = 100
	eps = []
	i = 0
	while i <= len(y)-100:
		mean.append(sum(y[x] for x in range(i,top))/100)
		eps.append(i+100)
		i+=100
		top+=100

	[print(d) for d in mean]	
	x = np.arange(0, len(y), 1)

	plt.plot(x, y)
	plt.xticks(fontsize=14)
	plt.yticks(fontsize=14)

	plt.margins(x=0)				#remove the ugly inner side margin
	plt.margins(y=0.01) 

	plt.ylabel('Loss', fontsize=24)
	plt.xlabel('Episode', fontsize=24)
	plt.subplots_adjust(bottom=0.11, left=0.035, right=0.99, hspace=0.2, wspace=0.2)
	plt.show()

if __name__ == '__main__':
	main()