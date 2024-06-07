#!/bin/bash
#SBATCH -J Minimap_all_2 # Job name
#SBATCH -o minimap_all.o # Name of output file
#SBATCH -e minimap_all.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=06:00:00
#SBATCH --partition=cbcb 
#SBATCH --account=cbcb 
#SBATCH --ntasks=32
#SBATCH --qos=huge-long
#SBATCH --mem=32gb

module load conda
source activate /fs/cbcb-scratch/imittra/long-read-data/SCRAPT/SCRAPT


/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/minimap2-2.28_x64-linux/minimap2 -t 32 /fs/cbcb-scratch/imittra/long-read-data/MeanSCRAPT/output_test_removed_80_2/filtered_seqs.fasta /fs/cbcb-scratch/imittra/long-read-data/filtered_seqs.fasta > minimap_filtered.paf
