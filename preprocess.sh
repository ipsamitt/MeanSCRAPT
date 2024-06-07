#!/bin/bash
#SBATCH -J PREP_Filter # Job name
#SBATCH -o prep_filter.o # Name of output file
#SBATCH -e prep_filter.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=10:00:00
#SBATCH --partition=cbcb
#SBATCH --account=cbcb
#SBATCH --ntasks=8
#SBATCH --qos=highmem
#SBATCH --mem=128gb

module load conda
#source activate /fs/cbcb-scratch/imittra/long-read-data/SCRAPT/SCRAPT
cd /fs/cbcb-scratch/imittra/long-read-data/
source activate ENV

/usr/bin/time -v python /fs/cbcb-scratch/imittra/long-read-data/preprocess_and_mean.py
