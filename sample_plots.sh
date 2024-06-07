#! /bin/bash
#SBATCH -J sample_plots_dec # Job name
#SBATCH -o sample_plots_dec.o # Name of output file
#SBATCH -e sample_plots_dec.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=12:00:00
#SBATCH --ntasks=8
#SBATCH --nodes=1
#SBATCH --mem=60gb
#SBATCH --partition=cbcb
#SBATCH --account=cbcb
#SBATCH --qos=medium

cd /fs/cbcb-scratch/imittra/long-read-data/

module load conda
source activate ENV

/usr/bin/time -v python3 /fs/cbcb-scratch/imittra/long-read-data/find_threshold_seqs.py -f /fs/cbcb-scratch/imittra/long-read-data/align_sample.fastq -t 8 -c 15 -k 7

~               
