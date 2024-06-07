#! /bin/bash
#SBATCH -J plots # Job name
#SBATCH -o plots.o # Name of output file
#SBATCH -e plots.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=2:00:00
#SBATCH --ntasks=16
#SBATCH --nodes=1
#SBATCH --mem=512gb
#SBATCH --partition=cbcb
#SBATCH --account=cbcb
#SBATCH --qos=highmem


cd /fs/cbcb-scratch/imittra/long-read-data/

module load conda
source activate ENV

/usr/bin/time -v python3 /fs/cbcb-scratch/imittra/long-read-data/k-threshold.py -f /fs/cbcb-scratch/imittra/long-read-data/all_data.fastq -t 16 -c 14 -k 5

~               
