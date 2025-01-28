import gzip
import glob
import shutil
import os

# Specify the input and output file names
input_dir = 'db_dump/compressed/'
output_dir = 'db_dump/uncompressed/'

file_list = glob.glob(input_dir+"*.gz")

for file in file_list:
    # Open the compressed file for reading
    with gzip.open(file, 'rb') as f_in:
        # Open the output file for writing
        out_file_name=output_dir+os.path.splitext(os.path.basename(file))[0]
        
        with open(out_file_name, 'wb') as f_out:
            # Copy the contents from the compressed file to the output file
            shutil.copyfileobj(f_in, f_out)
        print("File: "+file, " done!")

