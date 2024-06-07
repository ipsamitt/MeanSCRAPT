import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#change filenames to match the names of the clusters created for minimap and blast and dnaclust

def fragment(filename):
    array_2d = []
    total_seqs = 0
    with open(filename, 'r') as file:
        for line in file:
            #print(line)
            words = line.split()
            #print(len(words))
            total_seqs = total_seqs + len(words)
            array_2d.append(len(words))  # Append the list of words as a row in the 2D array
    array_2d = sorted(array_2d)

    keys_set = set(array_2d)
    sizes = {key: 0 for key in keys_set}
    for i in range (len(array_2d)):
        for key in keys_set:
            if array_2d[i] >= key:
                sizes[key] = sizes[key] + array_2d[i]

   # print(sizes)
    return sizes

filename = 'blast_clusters_10p_80.txt'
blast_vals = fragment(filename)


blast_x_values = list(blast_vals.keys())
blast_y_values = list(blast_vals.values())
scatter = plt.scatter(blast_x_values, blast_y_values, color = 'blue', s =20, marker='*', label = 'BLAST')
model = np.poly1d(np.polyfit(blast_x_values, blast_y_values,1))
polyline = np.linspace(1, 500, 30)
#plt.plot(polyline, model(polyline), color = 'blue')
ax = scatter.axes
ax.invert_xaxis()
#ax.invert_yaxis()
plt.xlabel('Cluster Size (# of seqs in cluster)')
plt.ylabel('# of sequences in cluster >= x')

filename = 'dnaclust_0.1_80_msa_results_32.txt'
dnaclust_vals = fragment(filename)
dnaclust_x_values = list(dnaclust_vals.keys())
dnaclust_y_values = list(dnaclust_vals.values())
plt.scatter(dnaclust_x_values, dnaclust_y_values, color = 'green', s = 20, marker = 'o', label='DNACLUST')
model = np.poly1d(np.polyfit(dnaclust_x_values, dnaclust_y_values, 1))
polyline = np.linspace(1, 5000, 30)
#plt.plot(polyline, model(polyline), color='green')

filename = 'minimap_clusters_10p_80.txt'
mini_vals = fragment(filename)
mini_x_values = list(mini_vals.keys())
mini_y_values = list(mini_vals.values())
plt.scatter(mini_x_values, mini_y_values, color = 'red', s = 100, marker = '*', label='MiniMap2')


filename = '/fs/cbcb-scratch/imittra/long-read-data/MeanSCRAPT/output_10p_80/centroid_sum.csv'
df = pd.read_table(filename)
clust_sizes = df['Cluster Density'].to_numpy()
array_2d = sorted(clust_sizes)
keys_set = set(array_2d)
sizes = {key: 0 for key in keys_set}
for i in range (len(array_2d)):
    for key in keys_set:
        if array_2d[i] >= key:
            sizes[key] = sizes[key] + array_2d[i]
scrapt_x_vals = list(sizes.keys())
scrapt_y_vals = list(sizes.values())
plt.scatter(scrapt_x_vals, scrapt_y_vals, color = 'brown', s = 20, marker = 'o', label = 'MeanSCRAPT')
model = np.poly1d(np.polyfit(scrapt_x_vals, scrapt_y_vals, 1))
polyline = np.linspace(1, 8125, 30)
#plt.plot(polyline, model(polyline), color = 'brown')
plt.legend()
plt.yscale("log")
plt.title("Fragmentation Curve")
plt.savefig("BLAST_Curve")
