import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
	df = pd.read_csv('./vehicles.csv')
	print((df.columns))
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("scaterplot_vehicles.png",bbox_inches='tight')
	sns_plot.savefig("scaterplot_vehicles.pdf",bbox_inches='tight')

	data = df.values.T[1]
	data = data[~np.isnan(data)]
	
	plt.clf()
	sns_plot2 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('Current fleet') 
	axes.set_ylabel('New fleet')

	sns_plot2.savefig("histogram_vehicles.png",bbox_inches='tight')
	sns_plot2.savefig("histogram_vehicles.pdf",bbox_inches='tight')

	
	#Calculate the Standard deviation of both samples
	#__Current fleet__
	data1 = df.values.T[0]
	print((("Mean: %f")%(data1[~np.isnan(data1)].mean())))
	print((("Median: %f")%(np.median(data1[~np.isnan(data1)]))))
	print((("Var: %f")%(data1[~np.isnan(data1)].var())))
	print((("std: %f")%(data1[~np.isnan(data1)].std())))
	print((("MAD: %f")%(mad(data1[~np.isnan(data1)]))))
	
	#__New fleet__
	data2 = df.values.T[1]
	print((("Mean: %f")%(data2[~np.isnan(data2)].mean())))
	print((("Median: %f")%(np.median(data2[~np.isnan(data2)]))))
	print((("Var: %f")%(data2[~np.isnan(data2)].var())))
	print((("std: %f")%(data2[~np.isnan(data2)].std())))
	print((("MAD: %f")%(mad(data2[~np.isnan(data2)]))))

	

	
