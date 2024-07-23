import numpy as np

# Define Mass
C_mass = 12.011

# Define lattice constants of Graphene
latt_c = 1.40  # length between nearest C-C

# Define length of unit cell of graphene
ux = latt_c * np.cos(np.pi / 3) + latt_c + latt_c * np.cos(np.pi / 3) + latt_c
uy = latt_c * np.sin(np.pi / 3) + latt_c * np.sin(np.pi / 3)

# Define coordinates of the unit cell
u = latt_c * np.array([[0.0, 0.0],
                       [np.cos(np.pi / 3), np.sin(np.pi / 3)],
                       [1 + np.cos(np.pi / 3), np.sin(np.pi / 3)],
                       [1 + 2 * np.cos(np.pi / 3), 0.0]])

no_atom_unit = len(u)

# Define number of repetitions in X and Y direction to generate Graphene Structure
num_xdir = int(input('Enter the number of repetitions in X: '))
num_ydir = int(input('Enter the number of repetitions in Y: '))

# Total number of atoms in graphene
tot_atoms = num_xdir * num_ydir * no_atom_unit

# Allocate a matrix to store carbon atoms for graphene
store_Catoms = np.zeros((tot_atoms, 3))

# Length of the Graphene
tot_Lx = ux * num_xdir  # Total Length in X Direction
tot_Ly = uy * num_ydir  # Total Length in Y Direction

# Define Graphene Coordinates
C_ID = 0  # Initialize the Carbon Atom ID
cord_z = 1  # All carbon atoms have same z coordinate

for j in range(num_ydir):
    for i in range(num_xdir):
        for c in range(no_atom_unit):
            C_ID += 1
            store_Catoms[C_ID - 1, 0] = u[c, 0] + i * ux
            store_Catoms[C_ID - 1, 1] = u[c, 1] + j * uy
            store_Catoms[C_ID - 1, 2] = cord_z

# Write in the format for Molecular Dynamics (MD) simulation
filename = 'data.graphene_MD'

with open(filename, 'w') as fid:
    fid.write('LAMMPS readable file \n\n')
    fid.write(f'\t\t{tot_atoms} atoms\n\n')
    fid.write('\t\t1 atom types\n\n')

    x_lo = np.min(store_Catoms[:, 0])
    x_hi = x_lo + tot_Lx

    y_lo = np.min(store_Catoms[:, 1])
    y_hi = y_lo + tot_Ly

    z_lo = cord_z - 4
    z_hi = cord_z + 4

    fid.write(f'\t{x_lo:.8f} {x_hi:.8f} \txlo xhi\n')
    fid.write(f'\t{y_lo:.8f} {y_hi:.8f} \tylo yhi\n')
    fid.write(f'\t{z_lo:.8f} {z_hi:.8f} \tzlo zhi\n\n')

    fid.write('Masses\n\n')
    fid.write(f'\t\t1 {C_mass:.8f}\n\n')

    fid.write('Atoms\n\n')
    
    for num, atom in enumerate(store_Catoms, start=1):
        fid.write(f'\t{num} 1 {atom[0]:.8f} {atom[1]:.8f} {atom[2]:.8f}\n')
