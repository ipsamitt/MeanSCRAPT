#!/bin/bash
#SBATCH -J BLAST # Job name
#SBATCH -o blast_0.001.o # Name of output file
#SBATCH -e blast_0.001.e # Name of error file
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

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/ncbi-blast-2.15.0+/bin/makeblastdb -in /fs/cbcb-scratch/imittra/long-read-data/align_sample.fasta -dbtype nucl

/usr/bin/time -v /fs/cbcb-scratch/imittra/long-read-data/ncbi-blast-2.15.0+/bin/blastn -query align_sample.fasta -db /fs/cbcb-scratch/imittra/long-read-data/align_sample.fasta -outfmt "6 qseqid sseqid pident nident length mismatch gapopen qstart qend sstart send evalue bitscore" -out blast_0.001_align.txt -num_threads 8
