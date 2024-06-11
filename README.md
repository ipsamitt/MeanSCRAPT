MeanSCRAPT is based on the original SCRAPT algorithm found at https://github.com/hsmurali/SCRAPT. This is an outline for the files included and their uses.

WITHIN MAIN DIRECTORY:

blast_0.001.sh: bash script to run blast on sample size of 0.1% of whole data set

blast_0.01.sh: bash script to run blast on sample size of 1% of whole data set

blast_0.1.sh: bash script to run blast on sample size of 10% of whole data set

blast_all_data.sh: bash script to run blast on whole data set

blast_clusters.py: python script to get DNACLUST output formatting from BLAST output, given a percentage identity threshold

blast_clusters.sh: bash script that calls blast_clusters.py

dnaclust_0.001.sh: bash script to run dnaclust on sample size of 0.1% of whole data set

dnaclust_0.01.sh: bash script to run dnaclust on sample size of 1% of whole data set

dnaclust_0.1.sh: bash script to run dnaclust on sample size of 10% of whole data set

dnaclust_all.sh: bash script to run dnaclust on whole data set

filter_seqs.sh: bash script that calls find_threshold_seqs.py

find_threshold_seqs.py: python script that finds sequences that have a quality score above given threshold and outputs list Kept_IDS.txt of qualifying seqs

fragment_clusters.py: python script that creates fragmentation curve plot of BLAST, DNACLUST, MINIMAP clusters

k_threshold.py: python script that creates plots of quality score distribution of all sequences in dataset and scatter plot of remover and kept k-mers within a dataset given quality threshold

kmer_curve.py: python script that creates distribution plot of k-mer quality scores within dataset

length_dist.py: python script that creates distribution of sequence lengths in dataset

minimap_0.001.sh: bash script to run minimap on sample size of 0.1% of whole data set

minimap_0.01.sh: bash script to run minimap on sample size of 1% of whole data set

minimap_0.1.sh: bash script to run minimap on sample size of 10% of whole data set

minimap_all.sh: bash script to run minimap on whole data set

minimap_clusters.py: python script to get DNACLUST output formatting from MINIMAP output, given a percentage identity threshold

minimap_clusters.sh: bash script that calls minimap_clusters.py

plot.sh: bash script that calls k-threshold.py

preprocess.py: python script that makes hash information of k-mer in dataset

preprocess_and_mean.py: python script that makes hash for all k-mer information and finds sequest closest to average representative sequence
preprocess.sh: bash script that calls preprocess_and_mean.py

sample_plots.sh: bash script that calls find_threshold_seqs.py


WITHIN MeanSCRAPT DIRECTORY:
This directory should be an almost complete copy of the original SCRAPT program. It is easier to download the original SCRAPT and change files within the src directory than implement SCRAPT through this github. The entire directory of SCRAPT should be replaced with the src.zip directory found within this github.
