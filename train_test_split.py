import os
import random
import shutil

# Set the directory paths
parent_dir = "Dataset/Hiragana/model4"
train_dir = os.path.join(parent_dir, "train")
test_dir = os.path.join(parent_dir, "test")

# Create the train and test directories if they don't exist
if not os.path.exists(train_dir):
    os.makedirs(train_dir)
if not os.path.exists(test_dir):
    os.makedirs(test_dir)

# Loop through the subfolders (a, b, c, d)
for subfolder in ["か","き","ち","に"]:
    # Set the directory paths for this subfolder
    subfolder_dir = os.path.join(parent_dir, subfolder)
    subfolder_train_dir = os.path.join(train_dir, subfolder)
    subfolder_test_dir = os.path.join(test_dir, subfolder)

    # Create the subfolder train and test directories if they don't exist
    if not os.path.exists(subfolder_train_dir):
        os.makedirs(subfolder_train_dir)
    if not os.path.exists(subfolder_test_dir):
        os.makedirs(subfolder_test_dir)

    # Get a list of all the images in the subfolder
    images = os.listdir(subfolder_dir)
    num_images = len(images)

    # Randomly select 10 images for the test set
    test_images = random.sample(images, 10) #change the numbr 10 to what u need

    # Move the test images to the test directory
    for image in test_images:
        src_path = os.path.join(subfolder_dir, image)
        dest_path = os.path.join(subfolder_test_dir, image)
        shutil.move(src_path, dest_path)

    # Move the remaining images to the train directory
    for image in images:
        if image not in test_images:
            src_path = os.path.join(subfolder_dir, image)
            dest_path = os.path.join(subfolder_train_dir, image)
            shutil.move(src_path, dest_path)





