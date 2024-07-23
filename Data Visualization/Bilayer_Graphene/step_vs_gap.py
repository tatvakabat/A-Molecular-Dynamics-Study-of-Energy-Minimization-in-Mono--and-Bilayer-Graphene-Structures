import os
import re
import matplotlib.pyplot as plt

def extract_data_from_log(file_path):
    steps = []
    gaps = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if "Step" in line or "thermo_style" in line:
            continue  # Skip the header line
        columns = line.split()
        if len(columns) >= 3:  # Ensure there are enough columns
            try:
                step = int(columns[0])
                gap = float(columns[2])
                steps.append(step)
                gaps.append(gap)
            except ValueError as e:
                print(f"ValueError: {e} for line: {line.strip()}")
        else:
            print(f"Skipping line with insufficient columns: {line.strip()}")
    return steps, gaps

def plot_step_vs_gap(directory, gap_values):
    plt.figure(figsize=(10, 6))
    
    for gap_value in gap_values:
        log_files = [f for f in os.listdir(directory) if f.endswith('.lammps')]
        for log_file in log_files:
            file_path = os.path.join(directory, log_file)
            # Extract bilayer gap from file name using regex
            gap_match = re.search(r'log_(\d+\.\d+)\.lammps', log_file)
            if gap_match and float(gap_match.group(1)) == gap_value:
                steps, gaps = extract_data_from_log(file_path)
                if steps and gaps:
                    plt.plot(steps, gaps, 'o-', label=f'Gap {gap_value}')
                else:
                    print(f"No valid data to plot for Gap {gap_value}.")
                break  # We found the matching file, no need to check further
        else:
            print(f"No log file found for Gap {gap_value}.")
    
    plt.axhline(y=3.3, color='black', linestyle='--', label='Ideal Gap Length')
    plt.xlabel('Step')
    plt.ylabel('Bilayer Gap')
    plt.title('Step vs Bilayer Gap for Different Gaps')
    plt.legend()
    plt.grid(True)
    plt.show()

# Specify the directory containing the log files
directory = r'enter your path here'

# Plot for Gap 2.0 and Gap 4.0 on the same graph
plot_step_vs_gap(directory, [2.0, 4.0])
