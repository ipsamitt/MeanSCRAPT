from hash_table import HashTable
from Bio import SeqIO
import multiprocessing
import sys
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
    print(sys.getsizeof(result))


    with open("preprocess_align_all.txt", 'w') as file:
        for item in result:
            file.write(','.join(map(str, item)) + '\n')


result = MAKE_KMER_HASH("/fs/cbcb-scratch/imittra/long-read-data/filtered_seqs.fastq", 5, 16)

