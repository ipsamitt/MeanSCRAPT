#!/bin/bash
#SBATCH -J BLAST_32 # Job name
#SBATCH -o blast_0.1_32.o # Name of output file
#SBATCH -e blast_0.1_32.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=12:00:00
#SBATCH --partition=cbcb
#SBATCH --account=cbcb
#SBATCH --ntasks=8
#SBATCH --qos=huge-long
#SBATCH --mem=32gb

module load conda
source activate /fs/cbcb-scratch/imittra/long-read-data/SCRAPT/SCRAPT

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/ncbi-blast-2.15.0+/bin/makeblastdb -in /fs/cbcb-scratch/imittra/long-read-data/filtered_seqs_10p.fasta -dbtype nucl

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/ncbi-blast-2.15.0+/bin/blastn -query /fs/cbcb-scratch/imittra/long-read-data/filtered_seqs_10p.fasta -db /fs/cbcb-scratch/imittra/long-read-data/filtered_seqs_10p.fasta -outfmt 6 -out blast_0.1_filtered_align.txt -num_threads 8
