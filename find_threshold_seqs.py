from Bio import SeqIO
import multiprocessing
import math
import argparse as ap
import sys
import matplotlib.pyplot as plt
import numpy as np

#CREATES LIST OF SEQUENCES THAT WILL BE KEPT GIVEN THRESHOLDS FOR CUT OFF

#have to add parameters for dictionaries that will be changed
def build_kmers(func_input):
    id_name, sequence, qual_scores, ksize, threshold, kept_id_filepath = func_input
    kept_kmers = dict()
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
        #include if score above threshold
                #include if score above threshold

        if score != 0:
            sum_score = sum_score + math.log(score)
        else:
            sum_score = sum_score

    avg_score = sum_score / len(sequence)
    if sum_score >= float(threshold):
        with open(kept_id_filepath, "a") as myfile:
            myfile.write(id_name)
            myfile.write("\n")

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
   
   kept_id_filepath = "Kept_IDS.txt"
   for record in records:
       id_name = record.id
       seq = record.seq
       qual = record.letter_annotations["phred_quality"]
       ksize = ksize
       cut_off = threshold
           #also have to pass in dictionaries that will be changed
       info = (id_name, seq, qual, ksize, cut_off, kept_id_filepath)
       func_input.append(info)

   pool.map(build_kmers, func_input)
   pool.close()
   pool.join()
   print("Pools closed")

