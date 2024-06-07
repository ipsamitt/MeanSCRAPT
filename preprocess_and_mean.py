from hash_table import HashTable
from Bio import SeqIO
import multiprocessing
import sys
import numpy as np
#import xxhash
#import threading


def generate_kmers(prefix, length, nucleotides):
    if length == 0:
        return [prefix]
    else:
        result = []
        for nucleotide in nucleotides:
            result.extend(generate_kmers(prefix + nucleotide, length - 1, nucleotides))
        return result


def make_seq_hash(info):
    id_name, sequence, k, seqs_to_add = info
 
#    print(len(seqs_to_add))
    ht = [0] * len(seqs_to_add)

    for i in range(len(sequence) - k + 1):
        kmer = sequence[i:i + k]
        ind = seqs_to_add.index(kmer)
        ht[ind] = ht[ind] + 1
        

    non_zero_counts = {}
    for i in range (len(ht)):
        if ht[i] != 0:
            non_zero_counts[i] = ht[i]
    ret_arr = []
    ret_arr.append(id_name)
    ret_arr.append(non_zero_counts)
    
    return ret_arr

def MAKE_KMER_HASH(seq_path, ksize, thread_count):
    pool = multiprocessing.Pool(thread_count)
        
    func_input = []

        
    records = SeqIO.parse(seq_path,"fastq")
        
    seqs_to_add = generate_kmers('',ksize, 'ACGT')
    for record in records:
        id_name = record.id
        seq = record.seq
        ksize = ksize
        info = (id_name, seq, ksize, seqs_to_add)
        
        func_input.append(info)
#    print(func_input)
    result = pool.map(make_seq_hash, func_input)
    pool.close()
    pool.join()
    #result = make_seq_hash(func_input[0])
    print("Pools closed")
    result = np.array(result, dtype=[(name, object) for name in ['ID', 'K-MER COUNTS']])
    print(result)
  
  #  print(sys.getsizeof(result))

#get artificial sequence from kmer counts
    counts_dict = {}
    
    for item in result:
        key = item[0]
        value = item[1]
        counts_dict[key] = value
    
    #print(counts_dict.values())

    summed_counts = [0]* (4**ksize)

    for i in range(len(result)):
        seq = result[i][0]
        counts = result[i][1]
        for key in counts:
            summed_counts[key] = summed_counts[key] + counts[key]

    
    avg_counts = [value / len(result) for value in summed_counts]

   # print(avg_counts)

    
#get closest real seq
    smallest_dist = 100000
    closest_seq = ""
    for i in range(len(result)):
        seq = result[i][0]
        counts = result[i][1]
        curr_dist = 0
        for j in range(len(avg_counts)):
            if j in counts:
                curr_dist = curr_dist + (avg_counts[j] - counts[j])**2
            if j not in counts:
                curr_dist = curr_dist + (avg_counts[j])**2
        curr_dist = curr_dist ** (1/2)
        #print(curr_dist)
        if (curr_dist < smallest_dist):
            smallest_dist = curr_dist
            closest_seq = seq
        
    print(smallest_dist)
    print(closest_seq)



print(MAKE_KMER_HASH("/fs/cbcb-scratch/imittra/long-read-data/align_sample.fastq", 5, 8))

