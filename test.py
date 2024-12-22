import os
import itertools
import string
import time
from tqdm import tqdm

# Define the characters and output file
chars = string.ascii_letters + '123456789'
output_file = r'C:\Users\HP 15s-du3023TX\Desktop\folder\gen.txt'
output_dir = os.path.dirname(output_file)

# Create the directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Calculate the total number of combinations
total_combinations = len(chars) ** 8
batch_size = 100000  # Save every 1 million combinations

# Open the file and write combinations with a progress bar
start_time = time.time()
with open(output_file, "w") as file:
    with tqdm(total=total_combinations, desc="Generating", unit="combos") as pbar:
        batch = []
        for count, combo in enumerate(itertools.product(chars, repeat=8), start=1):
            batch.append(''.join(combo) + '\n')
            
            # Write to file every batch_size combinations
            if count % batch_size == 0:
                file.writelines(batch)  # Save batch to file
                batch.clear()  # Clear batch from memory
                pbar.update(batch_size)
        
        # Save any remaining combinations in the batch
        if batch:
            file.writelines(batch)
            pbar.update(len(batch))
    elapsed_time = time.time() - start_time

print(f"File saved to: {output_file}")
print(f"Time taken: {elapsed_time:.2f} seconds")
