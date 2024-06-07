from Bio import SeqIO
import multiprocessing
import math
import argparse as ap
import sys
import matplotlib.pyplot as plt
import numpy as np

#creates graphs for quality scores of all sequences in the file and kept sequence k-mers versus all sequences

#have to add parameters for dictionaries that will be changed
def build_kmers(func_input):
    id_name, sequence, qual_scores, ksize, threshold = func_input
    kept_kmers = dict()
    n_kmers = len(sequence) - ksize + 1
    removed_kmer_count = 0
    all_qual_scores = []
    array_kept_ids = []
    sum_score = 0
    for i in range(n_kmers):
        #get kmer
        kmer = sequence[i:i + ksize]
        #get array of quality scores for kmer
        kmer_q_score = qual_scores[i:i + ksize]
        #calculate score
        score = calc_score(kmer_q_score)
        #include if score above threshold
        if (score >= threshold):
           if (kmer in kept_kmers.keys()):
               kept_kmers[kmer] += 1
           else:
               kept_kmers[kmer] = 1
        #count how many kmers were rejected due to threshold score
        else:
             removed_kmer_count = removed_kmer_count + 1

        if score != 0:
           sum_score = sum_score + math.log(score) 
        else:
           sum_score = sum_score
        all_qual_scores.append(score)
    #score = sum(math.log(x) for x in all_qual_scores)
    sum_score = sum_score / len(sequence)
    count_info = (removed_kmer_count, n_kmers)
    return (sum_score, count_info)

#score is log of sum of scores rounded to integer
def calc_score(qual_scores):
    sum_score = 0
    print(qual_scores)
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
   requiredNamed.add_argument("-c","--cutoff_threshold", help="Quality Score Threshold", required = True)
   requiredNamed.add_argument("-k", "--kmer_size", help="K-mer size", required=True)

   args = parser.parse_args()
   seq_path = args.filepath
   thread_count = int(args.thread_count)
   threshold = float(args.cutoff_threshold)
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
   
#   kept_id_filepath = "Kept_IDS.txt"
   for record in records:
       id_name = record.id
       seq = record.seq
       qual = record.letter_annotations["phred_quality"]
       ksize = ksize
       cut_off = threshold
           #also have to pass in dictionaries that will be changed
       info = (id_name, seq, qual, ksize, cut_off)
       func_input.append(info)

   result = pool.map(build_kmers, func_input)
   pool.close()
   pool.join()
   print("Pools closed")

   for i in range(len(result)):
       qual_score, count_info = result[i]
       qual_score_arr.append(qual_score)
       count_info_arr.append(count_info)
   
   removed_kmer_counts = []
   total_kmer_counts = []
   for i in range(len(count_info_arr)):
       removed, total = count_info_arr[i]
       removed_kmer_counts.append(removed)
       total_kmer_counts.append(total)

   plt.hist(qual_score_arr, cumulative=True, density = True, bins = 50)
   plt.xlabel('Quality Score of Whole Sequence')
   plt.ylabel('Normalized Frequency')
   plt.savefig('Quality_Score_Seq')
   
   total_np = np.array(total_kmer_counts)
   removed_np = np.array(removed_kmer_counts)
   variance = np.var(removed_np)
   plt.scatter(total_kmer_counts, removed_kmer_counts, alpha = 0.5)

   plt.plot(total_kmer_counts, total_kmer_counts)
   plt.ylim([0,2000])
   plt.xlim([0,2000])
   plt.xlabel("Total K-mer counts")
   plt.ylabel("Removed K-mer counts")
   plt.savefig('K-mer_Count_Dist_Whole_14c')
   #print proportions of removed_counts
   #make distribution plot of quality scores
   #scatter plot with # of kmers removed vs total # of kmers
