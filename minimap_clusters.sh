#!/bin/bash
#SBATCH -J MINCLUST # Job name
#SBATCH -o minimap_clust.o # Name of output file
#SBATCH -e minimap_clust.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=04:00:00
#SBATCH --partition=cbcb
#SBATCH --account=cbcb
#SBATCH --ntasks=16
#SBATCH --qos=high
#SBATCH --mem=64gb

module load conda
cd /fs/cbcb-scratch/imittra/long-read-data/
source activate ENV

/usr/bin/time -v python minimap_clusters.py ./minimap_0.1_32.paf 80
