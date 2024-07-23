import os
import re
import matplotlib.pyplot as plt

# Directory containing the log files
log_dir = r"enter your path here"

# Regular expressions to extract step and bond length
step_pattern = re.compile(r'\s*(\d+)\s+[\d.-]+\s+[\d.-]+\s+[\d.-]+\s+([\d.-]+)')

# Lists to store bond length and step data
steps = []
bond_lengths = []

# Function to read the log files and extract data
def read_log_file(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            step_match = step_pattern.match(line)
            if step_match:
                steps.append(int(step_match.group(1)))
                bond_lengths.append(float(step_match.group(2)))

# Read all log files in the directory
for filename in os.listdir(log_dir):
    if filename.endswith('.lammps'):
        filepath = os.path.join(log_dir, filename)
        read_log_file(filepath)

# Plot bond length vs. step
plt.figure(figsize=(10, 6))
plt.plot(steps, bond_lengths, label='Bond Length')
plt.xlabel('Step')
plt.ylabel('Bond Length (Å)')
plt.title('Bond Length vs. Step')
plt.legend()
plt.grid(True)
plt.show()
