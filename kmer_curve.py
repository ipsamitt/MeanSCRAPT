from Bio import SeqIO
import multiprocessing
import math
import argparse as ap
import sys
import matplotlib.pyplot as plt
import numpy as np

#creates distribution of individual kmer scores

#have to add parameters for dictionaries that will be changed
def kmer_props(func_input):
    id_name, sequence, qual_scores, ksize = func_input
    n_kmers = len(sequence) - ksize + 1
    removed_kmer_count = 0
    all_qual_scores = []
    array_kept_ids = []
    for i in range(n_kmers):
        #get kmer
        kmer = sequence[i:i + ksize]
        #get array of quality scores for kmer
        kmer_q_score = qual_scores[i:i + ksize]
        #calculate score
        score = calc_score(kmer_q_score)
        

        all_qual_scores.append(score)

    proportions = {}
    for i in range(len(all_qual_scores)):
        lower_bound = 0
        upper_bound = sorted(all_qual_scores)[i]
        within_range_count = 0
        for value in all_qual_scores:
            if lower_bound <= value <= upper_bound:
                within_range_count += 1
        #print (within_range_count)
        proportions[upper_bound] = (within_range_count / n_kmers)
 
    return proportions

#score is log of sum of scores rounded to integer
def calc_score(qual_scores):
    sum_score = 0
    #should be log of probability of quality scores
    for i in range(len(qual_scores)):
        sum_score = sum_score + math.log(qual_scores[i])
    return sum_score


if __name__ == "__main__":
   parser = ap.ArgumentParser(description="K-mer Threshold Counts")
   requiredNamed = parser.add_argument_group('required named arguments')
   optionalNamed = parser.add_argument_group('optional named arguments')
   requiredNamed.add_argument("-f", "--filepath", help="FASTQ File", required=True)
   requiredNamed.add_argument("-t", "--thread_count", help="Thread Count", required=True)
   requiredNamed.add_argument("-k", "--kmer_size", help="K-mer size", required=True)

   args = parser.parse_args()
   seq_path = args.filepath
   thread_count = int(args.thread_count)
   ksize = int(args.kmer_size)

#change it to 8 threads
   pool = multiprocessing.Pool(thread_count)
        #dictionary of each sequence's removed counts and total counts
   count_info_arr = []
        #dictionary of all quality scores
   qual_score_arr = []


   func_input = []

        #array of sequences with quality strings
   records = SeqIO.parse(seq_path,"fastq")
        #HELP have to be able to chance all_kmers and removed_counts
   
   
   for record in records:
       id_name = record.id
       seq = record.seq
       qual = record.letter_annotations["phred_quality"]
       ksize = ksize
           #also have to pass in dictionaries that will be changed
       info = (id_name, seq, qual, ksize)
    #   print(info)
       func_input.append(info)

   result = pool.map(kmer_props, func_input)
   pool.close()
   pool.join()
   print("Pools closed")

   
   x = []
   y = []
   for i in range(len(result)):
       curr_seq_props = result[i]
       for key, value in curr_seq_props.items():
           x.append(key)
           y.append(value)


   plt.plot(x,y)
   plt.xlabel("K-mer Quality Score")
   plt.ylabel("Fraction of K-mers in Sequence")
   plt.savefig('K-mer_Score_Props.png')
   #print proportions of removed_counts
   #make distribution plot of quality scores
   #scatter plot with # of kmers removed vs total seqs
