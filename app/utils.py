import os
import random
import string
import pickle
from zxcvbn import zxcvbn

def run_zxcvbn(psswd):
    if not psswd:
        return None
    if len(psswd) > 72:
        return zxcvbn(psswd[:72])
    return zxcvbn(psswd)


def find_non_ascii_char(passwords,non_ascii_chars):
    sp_pswd_lst = []
    for p in passwords:
        for sp in non_ascii_chars:
            if sp in p:
                sp_pswd_lst.append(p)
    
    sp_pswd_set = list(set(sp_pswd_lst))
    clean_pswd = [pswd for pswd in passwords if pswd not in sp_pswd_set]

    return clean_pswd, sp_pswd_set


def generate_random_password(length):
    """Generates a random password of specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def simulate_passwords(num_passwords, min_length, max_length):
    """Simulates a given number of passwords with varying lengths."""
    passwords = []
    for _ in range(num_passwords):
        length = random.randint(min_length, max_length)
        password = generate_random_password(length)
        passwords.append(password)
    return passwords


def read_file(file_path):
    with open(file_path, 'r') as f:
        count = 1
        words = []
        try:
            for l in f:
                if len(l) > 150:
                    continue
                count += 1
                words.append(l.strip())
        except UnicodeDecodeError as e:
            pass
            
    return words



def pickle_dataframe(dataframe=None, filepath: str = 'data.pkl', mode: str = 'save'):
    """
    Saves a Pandas DataFrame to a pickle file or loads a DataFrame from a pickle file.

    Args:
        dataframe (pd.DataFrame, optional): The DataFrame to be saved.
                                            Required if mode is 'save'. Defaults to None.
        filepath (str): The path to the pickle file. Defaults to 'data.pkl'.
        mode (str): The operation mode. Must be 'save' or 'load'. Defaults to 'save'.

    Returns:
        pd.DataFrame or None: If mode is 'load', returns the loaded DataFrame.
                              If mode is 'save' or an error occurs, returns None.

    Raises:
        ValueError: If an invalid mode is provided or if 'save' mode is
                    called without a DataFrame.
    """
    if mode not in ['save', 'load']:
        raise ValueError("Invalid mode. Must be 'save' or 'load'.")

    if mode == 'save':
        if dataframe is None:
            raise ValueError("DataFrame must be provided when mode is 'save'.")
        try:
            with open(filepath, 'wb') as file:
                pickle.dump(dataframe, file)
            print(f"DataFrame successfully saved to '{filepath}'")
            return None
        except Exception as e:
            print(f"Error saving DataFrame to '{filepath}': {e}")
            return None
    elif mode == 'load':
        if not os.path.exists(filepath):
            print(f"Error: File '{filepath}' not found.")
            return None
        try:
            with open(filepath, 'rb') as file:
                loaded_df = pickle.load(file)
            print(f"DataFrame successfully loaded from '{filepath}'")
            return loaded_df
        except Exception as e:
            print(f"Error loading DataFrame from '{filepath}': {e}")
            return None
        