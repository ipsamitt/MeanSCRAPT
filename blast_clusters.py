#process blast file to make big array with blast info
#read dnaclust file
#find corresponding seqs in big array


import sys
import numpy as np

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            return lines
    except FileNotFoundError:
        print("File not found.")
        return []


if __name__ == "__main__":
    #parameters to script are BLAST file, threshold for percentage, output file name
    if len(sys.argv) != 3:
        print("Usage: python blast_clusters.py <file1>")
        sys.exit(1)

    blast_file = sys.argv[1]
    percent_threshold = int(sys.argv[2])
    filename = sys.argv[3]


    lines_blast = read_file(blast_file)
    whole_blast_pid = []
    
    for line in lines_blast:
        line = (line.split())
        #length of query - mismatches/ length of query
        if ((int(line[8]) - int(line[7])) != 0): 
           pid = ((int(line[3])))/(int(line[8])-int(line[7])) * 100
           length = (int(line[8]) - int(line[7]))
           row = [line[0], line[1], length, pid]
           whole_blast_pid.append(row)

    paf_info = sorted(whole_blast_pid, key=lambda x: x[2], reverse=True)


    clusters = []
    length = len(paf_info[0])

    added = []
    centroids = []

    for i in range(len(paf_info)):
        if float(paf_info[i][length - 1]) >= percent_threshold:
            #if this is a high similarity pair that has never been seen in clusters organization
           if (not (paf_info[i][0] in centroids) and not(paf_info[i][1] in added)):
               new_cluster = set()
               new_cluster.add(paf_info[i][0])
               new_cluster.add(paf_info[i][1])
               centroids.append(paf_info[i][0])
               clusters.append(new_cluster)
               added.append(paf_info[i][0])
               added.append(paf_info[i][1])
           elif ((paf_info[i][0] in centroids) and (paf_info[i][1] not in added)):
               for j in range(len(clusters)):
                   curr_cluster = clusters[j]
                   if (paf_info[i][0] in curr_cluster):
                      curr_cluster.add(paf_info[i][1])
                      added.append(paf_info[i][1])
                

      
     

# Open the file in write mode
    with open(filename, 'w') as file:
    # Iterate over each set and write it to the file
        for s in clusters:
        # Convert the set to a string representation
            line = ' '.join(str(x) for x in s)
        # Write the string representation to a new line in the file
            file.write(line + '\n')           


