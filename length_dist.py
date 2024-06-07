import matplotlib.pyplot as plt
from Bio import SeqIO

#creates graph to examine distribution of sequences in file

# Define the FASTQ file path
fastq_file = "all_data.fastq"

# Initialize an empty list to store sequence lengths
sequence_lengths = []

# Iterate through the FASTQ file and extract sequence lengths
for record in SeqIO.parse(fastq_file, "fastq"):
    sequence_lengths.append(len(record.seq))

# Create a histogram
plt.hist(sequence_lengths, bins=50, color='blue', alpha=0.7)
plt.xlabel('Sequence Length')
plt.ylabel('Frequency')
plt.title('Histogram of Sequence Lengths')
plt.grid(True)

# Show the histogram
plt.savefig("Length_Distribution.png")
