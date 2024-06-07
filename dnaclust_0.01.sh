#!/bin/bash
#SBATCH -J DNACLUST # Job name
#SBATCH -o DNACLUST_0.01.o # Name of output file
#SBATCH -e DNACLUST_0.01.e # Name of error file
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

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/SCRAPT/dnaclust/bin/dnaclust -i /fs/cbcb-scratch/imittra/long-read-data/sampled_data_0.01.fasta -s 0.90 -t 8 -m > dnaclust_0.1_msa_results.txt 
