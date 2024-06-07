#!/bin/bash
#SBATCH -J DNACLUST_10p_32 # Job name
#SBATCH -o DNACLUST_10p_32.o # Name of output file
#SBATCH -e DNACLUST_10p_32.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=24:00:00
#SBATCH --partition=cbcb 
#SBATCH --account=cbcb 
#SBATCH --ntasks=32
#SBATCH --qos=huge-long
#SBATCH --mem=32gb

module load conda
source activate ENV

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/MeanSCRAPT/SCRAPT/dnaclust/bin/dnaclust -i /fs/cbcb-scratch/imittra/long-read-data/MeanSCRAPT/output_10p_80/filtered_seqs.fasta -s 0.80 -t 32 -m > dnaclust_0.1_80_msa_results_32.txt 
