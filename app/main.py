import os
import subprocess


root_path = './data/'
outputs_str = ['password_df', 'sequences_password_df', 'sp_chars', 'rmv_leaked', 'rmv_rock']
# list data directory to check for existance of pickled data

files_exist = set([t + '.pkl' for t in outputs_str]) == set([t for t in os.listdir(root_path) if t.endswith('pkl')])

if files_exist:
    print("Pickled data files exist in the data directory.")
    pass

else:
    print("Pickled data files do not exist in the data directory. Running the data script.")
    subprocess.run(['python3', 'data_script.py'], check=True)