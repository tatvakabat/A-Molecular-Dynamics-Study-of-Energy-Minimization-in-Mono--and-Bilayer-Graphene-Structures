import os
import matplotlib.pyplot as plt

# Define the bond lengths and corresponding log file names with the correct extension
bond_lengths = [1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
log_files = [f'log_{bl:.1f}.lammps' for bl in bond_lengths]

# Path to the directory containing the log files
log_directory = r'enter your path here'

def extract_potential_energy(log_path):
    try:
        with open(log_path, 'r') as file:
            lines = file.readlines()
        
        steps = []
        potential_energies = []
        header_line_found = False

        for line in lines:
            if 'Step' in line and 'PotEng' in line:
                # Find the header line
                header_line = line.strip().split()
                if 'Step' in header_line and 'PotEng' in header_line:
                    step_index = header_line.index('Step')
                    pe_index = header_line.index('PotEng')
                    header_line_found = True
                continue
            if header_line_found and len(line.split()) > 1 and line.split()[0].isdigit():
                # Extract data based on indices
                data = line.strip().split()
                steps.append(int(data[step_index]))
                potential_energies.append(float(data[pe_index]))

        return potential_energies

    except Exception as e:
        print(f"Error reading {log_path}: {e}")
        return []

# Lists to store the extracted data
potential_energies = []
for bl, log_file in zip(bond_lengths, log_files):
    log_path = os.path.join(log_directory, log_file)
    print(f"Processing file: {log_path}")  # Debugging statement
    energies = extract_potential_energy(log_path)
    if energies:
        potential_energies.append((bl, energies[0]))  # Just taking the first energy for simplicity
    else:
        print(f"No potential energy found for {log_file}")

# Unzip the bond_lengths and potential_energies for plotting
if potential_energies:
    bond_lengths, energies = zip(*potential_energies)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(bond_lengths, energies, marker='o', linestyle='-', color='b')
    plt.xlabel('Bond Length (Å)')
    plt.ylabel('Potential Energy (eV)')
    plt.title('Bond Length vs. Potential Energy')
    plt.grid(True)
    plt.show()
else:
    print("No valid data to plot.")
