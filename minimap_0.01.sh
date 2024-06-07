#!/bin/bash
#SBATCH -J Minimap2 # Job name
#SBATCH -o minimap_0.01.o # Name of output file
#SBATCH -e minimap_0.01.e # Name of error file
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


/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/minimap2-2.26_x64-linux/minimap2 -t 8 /fs/cbcb-scratch/imittra/long-read-data/sampled_data_0.01.fasta /fs/cbcb-scratch/imittra/long-read-data/sampled_data_0.01.fasta > minimap_0.01.paf
