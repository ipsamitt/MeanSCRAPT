#!/bin/bash
#SBATCH -J DNACLUST_all # Job name
#SBATCH -o DNACLUST_all.o # Name of output file
#SBATCH -e DNACLUST_all.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=3-00:00:00
#SBATCH --partition=cbcb 
#SBATCH --account=cbcb 
#SBATCH --ntasks=16
#SBATCH --qos=huge-long
#SBATCH --mem=256gb

module load conda
cd /fs/cbcb-scratch/imittra/long-read-data/
source activate ENV

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/MeanSCRAPT/SCRAPT/dnaclust/bin/dnaclust -i /fs/cbcb-scratch/imittra/long-read-data/MeanSCRAPT/output_all_527_8_threads/filtered_seqs.fasta -s 0.80 -t 16 -m > dnaclust_all_80_msa_results.txt 
