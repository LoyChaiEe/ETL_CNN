import os
import random
import shutil

# Set the paths for your input and output folders
input_folder = "う"
output_folder = "tmp/images"

# Set the number of images you want to select
num_images = 60

# Get the list of file names in the input folder
file_names = os.listdir(input_folder)

# Shuffle the file names randomly
random.shuffle(file_names)

# Select the first num_images file names from the shuffled list
selected_files = file_names[:num_images]

# Copy the selected files to the output folder
for file_name in selected_files:
    input_path = os.path.join(input_folder, file_name)
    output_path = os.path.join(output_folder, file_name)
    shutil.copy(input_path, output_path)

