#!/bin/bash
#SBATCH -J BLAST # Job name
#SBATCH -o blast_0.01.o # Name of output file
#SBATCH -e blast_0.01.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=01:00:00
#SBATCH --partition=cbcb
#SBATCH --account=cbcb
#SBATCH --ntasks=16
#SBATCH --qos=high
#SBATCH --mem=32gb

module load conda
source activate /fs/cbcb-scratch/imittra/long-read-data/SCRAPT/SCRAPT

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/ncbi-blast-2.15.0+/bin/makeblastdb -in /fs/cbcb-scratch/imittra/long-read-data/sampled_data_0.01.fasta -dbtype nucl

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/ncbi-blast-2.15.0+/bin/blastn -query sampled_data_0.01.fasta -db /fs/cbcb-scratch/imittra/long-read-data/sampled_data_0.01.fasta -outfmt 6 -out blast_0.01_align.txt -num_threads 8
