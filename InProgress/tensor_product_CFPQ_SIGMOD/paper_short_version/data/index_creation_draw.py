import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy.stats 


lubm_graphs = ["LUBM1k_stat.csv","LUBM3.5k_stat.csv","LUBM5.9k_stat.csv","LUBM1M_stat.csv","LUBM1.7M_stat.csv","LUBM2.3M_stat.csv"]
other_graphs = ["proteomes_stat.csv","uniprotkb_stat.csv","geospecies_stat.csv","mappingbased_properties_stat.csv", "taxonomy_stat.csv"]


styles = [['o','r'],['v','g'],['X','b'],['s','y'],['^','k'],['d','m']]

q_order=['q_1','q_2','q_3',
         'q_4_2','q_4_3','q_4_4','q_4_5',
         'q_5','q_6','q_7','q_8',
         'q_9_2','q_9_3','q_9_4','q_9_5',
         'q_10_2','q_10_3','q_10_4','q_10_5',
         'q_11_2','q_11_3','q_11_4','q_11_5',
         'q_12','q_13','q_14','q_15','q_16']

q_labels=['$Q_1$','$Q_2$','$Q_3$',
         '$Q_4^2$','$Q_4^3$','$Q_4^4$','$Q_4^5$',
         '$Q_5$','$Q_6$','$Q_7$','$Q_8$',
         '$Q_9^2$','$Q_9^3$','$Q_9^4$','$Q_9^5$',
         r'$Q_{10}^2$',r'$Q_{10}^3$',r'$Q_{10}^4$',r'$Q_{10}^5$',
         r'$Q_{11}^2$',r'$Q_{11}^3$',r'$Q_{11}^4$',r'$Q_{11}^5$',
         r'$Q_{12}$',r'$Q_{13}$',r'$Q_{14}$',r'$Q_{15}$',r'$Q_{16}$']


def draw (graphs, out_file):
	dfs = [[g[:-9],pd.read_csv(g)[['grammar','mean']]] for g in graphs]

	for df in dfs:
		for i, row in df[1].iterrows():
			x = row['grammar'][:-2].replace('q_','q').replace('q','q_')
			df[1].at[i,'grammar'] = x

	fig = plt.figure()
	#plt.yscale('log')
	i = 0
	
	for df in dfs:
		df[1]['grammar']=pd.Categorical(df[1]['grammar'],categories=q_order)
		df[1]=df[1].sort_values(['grammar'])
		plt.scatter(df[1]['grammar'], df[1]['mean'], label=df[0], marker = styles[i][0], facecolors='none', edgecolors = styles[i][1])
		i = i + 1

	axs = plt.axes()
	leg = axs.legend();

	# adding horizontal grid lines
	axs.yaxis.grid(True)
	plt.xticks(q_order, q_labels, rotation=60, fontsize=8)
	#axs.set_xticks([y + 1 for y in range(len(d[1]))])
	axs.set_xlabel('Query')
	axs.set_ylabel('Time in seconds')
	fig.tight_layout()
	plt.savefig(out_file)
	plt.show()

draw(lubm_graphs, "LUBM_all.pdf")