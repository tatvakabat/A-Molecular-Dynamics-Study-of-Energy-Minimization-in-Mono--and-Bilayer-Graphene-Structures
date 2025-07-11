import os
import re
import matplotlib.pyplot as plt

# Directory containing the log files
log_dir = r"ADD PATH HERE"

# Regular expression to extract step and bond length
step_pattern = re.compile(r'\s*(\d+)\s+[\d.-]+\s+[\d.-]+\s+[\d.-]+\s+([\d.-]+)')

# Function to read a log file and extract steps and bond lengths
def read_log_file(filepath):
    file_steps = []
    file_bond_lengths = []
    with open(filepath, 'r') as file:
        for line in file:
            step_match = step_pattern.match(line)
            if step_match:
                file_steps.append(int(step_match.group(1)))
                file_bond_lengths.append(float(step_match.group(2)))
    return file_steps, file_bond_lengths

# Plot setup
plt.figure(figsize=(10, 6))

# Read and plot each file
for filename in os.listdir(log_dir):
    if filename.endswith('.lammps'):
        filepath = os.path.join(log_dir, filename)
        steps, bond_lengths = read_log_file(filepath)
        
        # Format the label: e.g., "log_1.7.lammps" → "C–C 1.7"
        base_name = os.path.splitext(filename)[0]  # "log_1.7"
        bond_length = base_name.replace("log_", "")  # "1.7"
        label = f"C–C {bond_length}"  # Use en dash (–) for clarity
        
        plt.plot(steps, bond_lengths, label=label)

# Final plot styling
plt.xlabel('Step')
plt.ylabel('Bond Length (Å)')
plt.title('Bond Length vs. Step per Initial Bond')
plt.legend(title="Initial Bond Length", loc='best')
plt.grid(True)
plt.tight_layout()
plt.show()
