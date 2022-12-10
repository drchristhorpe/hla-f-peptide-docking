import os


peptide_sequence = 'GLGTDEDTLIEILASR'


hla_f_filename = '../structures/5iue_1_emptied.pdb'
peptide_filename = f'../peptides/{peptide_sequence}.pdb'
autobox_filename = '../structures/5iue_1_peptide.pdb'
docked_filename = f'../predictions/gnina/{peptide_sequence.lower()}.sdf'



gnina_command = f'./gnina -r {hla_f_filename} -l {peptide_filename} --autobox_ligand {autobox_filename} -o {docked_filename} --flexdist_ligand {autobox_filename} --flexdist 3.5 --seed 0'



os.system(gnina_command)
