#!/bin/bash
#SBATCH -J BLAST # Job name
#SBATCH -o blast_all_2.o # Name of output file
#SBATCH -e blast_all_2.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=3-00:00:00
#SBATCH --partition=cbcb
#SBATCH --account=cbcb
#SBATCH --ntasks=16
#SBATCH --qos=huge-long
#SBATCH --mem=256gb

module load conda
source activate /fs/cbcb-scratch/imittra/long-read-data/SCRAPT/SCRAPT

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/ncbi-blast-2.15.0+/bin/makeblastdb -in /fs/cbcb-scratch/imittra/long-read-data/MeanSCRAPT/output_all_527_8_threads/filtered_seqs.fasta -dbtype nucl -title all_filtered.fasta

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/ncbi-blast-2.15.0+/bin/blastn -query filtered_seqs.fasta -db all_filtered.fasta -outfmt 6 -out blast_filtered_data_align.txt -num_threads 16
