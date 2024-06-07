#!/bin/bash
#SBATCH -J NGLMR # Job name
#SBATCH -o nglmr_0.01.o # Name of output file
#SBATCH -e nglmr_0.01.e # Name of error file
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

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/ngmlr-0.2.7/ngmlr -t 8 -r sampled_data_0.01.fasta -q sampled_data_0.01.fastq -o nglmr_0.01.sam
