#!/bin/bash
#SBATCH -J Minimap2 # Job name
#SBATCH -o minimap_0.1.o # Name of output file
#SBATCH -e minimap_0.1.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=06:00:00
#SBATCH --partition=cbcb 
#SBATCH --account=cbcb 
#SBATCH --ntasks=8
#SBATCH --qos=huge-long
#SBATCH --mem=32gb

module load conda
source activate /fs/cbcb-scratch/imittra/long-read-data/SCRAPT/SCRAPT


/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/MeanSCRAPT/SCRAPT/minimap2-2.28_x64-linux/minimap2 -t 8 /fs/cbcb-scratch/imittra/long-read-data/filtered_seqs_10p.fasta /fs/cbcb-scratch/imittra/long-read-data/filtered_seqs_10p.fasta > minimap_0.1_32.paf
