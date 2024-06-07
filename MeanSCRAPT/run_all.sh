#! /bin/bash
#SBATCH -J mean_scrapt_test_all_527_32_threads # Job name
#SBATCH -o mean_scrapt_test_all_527_32_threads.o # Name of output file
#SBATCH -e mean_scrapt_test_all_527_32_threads.e # Name of error file
#SBATCH --mail-user=imittra@terpmail.umd.edu # Email for job info
#SBATCH --mail-type=all # Get email for begin, end, and fail
#SBATCH --time=3-00:00:00
#SBATCH --partition=cbcb
#SBATCH --account=cbcb
#SBATCH --qos=huge-long
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --nodes=1
#SBATCH --mem=256gb

module load conda
cd /fs/cbcb-scratch/imittra/long-read-data/
source activate ENV

data_path=/fs/cbcb-scratch/imittra/long-read-data/all_data.fastq

prog_path=/fs/cbcb-scratch/imittra/long-read-data/MeanSCRAPT/SCRAPT/src/
outdir=/fs/cbcb-scratch/imittra/long-read-data/MeanSCRAPT/output_all_527_32_threads/

rm -rf ${outdir}

/usr/bin/time -v python ${prog_path}SCRAPT.py -f ${data_path} -o ${outdir} -n 50 -t 32 -m True -r 0.8 -e 2.35 -s 0.01
