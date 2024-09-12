'''Python code to create an array with random elments'''
import subprocess

def random_array(arr):
    '''This function creates a random array'''
    shuffled_num = None
    for i,_ in enumerate(arr):
        shuffled_num = subprocess.run(["shuf", "-i1-20", "-n1"], capture_output=True, check=False)
        arr[i] = int(shuffled_num.stdout)
    return arr
