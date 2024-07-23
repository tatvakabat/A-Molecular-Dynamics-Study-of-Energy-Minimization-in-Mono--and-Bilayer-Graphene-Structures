import os
import re
import matplotlib.pyplot as plt

def extract_data_from_log(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    steps = []
    gaps = []
    potentials = []

    for line in lines:
        if "Step" in line:  # Skip header lines
            continue
        columns = line.split()
        if len(columns) >= 4:  # Ensure there are enough columns to process
            try:
                step = int(columns[0])
                gap = float(columns[2])
                potential = float(columns[3])
                steps.append(step)
                gaps.append(gap)
                potentials.append(potential)
            except ValueError:
                # Handle lines that do not contain float or int values
                continue

    return gaps, potentials

def plot_bilayer_gap_vs_potential_energy(directory):
    log_files = [f for f in os.listdir(directory) if f.endswith('.lammps')]

    gaps_2_0 = []
    potentials_2_0 = []
    gaps_4_0 = []
    potentials_4_0 = []

    for log_file in log_files:
        file_path = os.path.join(directory, log_file)
        # Extract bilayer gap from file name using regex
        gap_match = re.search(r'log_(\d+\.\d+)\.lammps', log_file)
        if gap_match:
            gap_value = float(gap_match.group(1))
            gaps, potentials = extract_data_from_log(file_path)
            
            if gap_value == 2.0:
                gaps_2_0 = gaps
                potentials_2_0 = potentials
            elif gap_value == 4.0:
                gaps_4_0 = gaps
                potentials_4_0 = potentials

    plt.figure(figsize=(12, 8))
    if gaps_2_0 and potentials_2_0:
        plt.plot(gaps_2_0, potentials_2_0, 'o-', label='Gap 2.0')
    if gaps_4_0 and potentials_4_0:
        plt.plot(gaps_4_0, potentials_4_0, 's-', label='Gap 4.0')
    
    plt.xlabel('Bilayer Gap')
    plt.ylabel('Potential Energy')
    plt.title('Bilayer Gap vs Potential Energy')
    plt.ylim(-1500, -700)
    plt.legend()
    plt.grid(True)
    plt.show()

# Specify the directory containing the log files
directory = 'enter your path to the files here'

# Plot for both Gap 2.0 and Gap 4.0
plot_bilayer_gap_vs_potential_energy(directory)
