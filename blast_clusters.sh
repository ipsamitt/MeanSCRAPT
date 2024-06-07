#!/bin/bash
#SBATCH -J BLAST # Job name
#SBATCH -o blast_clusters.o # Name of output file
#SBATCH -e blast_clusters.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=12:00:00
#SBATCH --partition=cbcb
#SBATCH --account=cbcb
#SBATCH --ntasks=16
#SBATCH --qos=highmem
#SBATCH --mem=512gb

module load conda
source activate /fs/cbcb-scratch/imittra/long-read-data/SCRAPT/SCRAPT

/usr/bin/time -v python blast_clusters.py ./blast_0.1_filtered_align.txt 80
