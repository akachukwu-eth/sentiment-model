# import os
# from sklearn.datasets import load_files
# from tqdm import tqdm

# # Replace 'path/to/dataset' with the path to the directory where the extracted IMDB dataset is located
# IMDB_DIR = r'C:\Users\Akachukwu Egboluche\Downloads\aclImdb'

# # Load the dataset
# reviews_train = load_files(os.path.join(IMDB_DIR, "train"))
# reviews_test = load_files(os.path.join(IMDB_DIR, "test"))

# # Print some basic information about the dataset
# print("Number of training reviews: {}".format(len(reviews_train.data)))
# print("Number of testing reviews: {}".format(len(reviews_test.data)))

# # Show progress bar while loading files
# print("Loading training reviews...")
# for path in tqdm(reviews_train.filenames):
#     with open(path, encoding="utf8") as f:
#         text = f.read()

# print("Loading testing reviews...")
# for path in tqdm(reviews_test.filenames):
#     with open(path, encoding="utf8") as f:
#         text = f.read()


import os
from sklearn.datasets import load_files
from tqdm import tqdm

IMDB_DIR = r'C:\Users\Akachukwu Egboluche\Downloads\aclImdb'

def load_data(container_path, categories=None, shuffle=True, random_state=42):
    data = load_files(container_path, categories=categories, shuffle=shuffle, random_state=random_state)
    files = data['filenames']
    targets = data['target']
    target_names = data['target_names']
    # Add progress bar to monitor file loading
    files = [str(f) for f in tqdm(files)]
    return files, targets, target_names

# Load the dataset
train_files, train_targets, target_names = load_data(os.path.join(IMDB_DIR, "train"))
test_files, test_targets, _ = load_data(os.path.join(IMDB_DIR, "test"), categories=target_names)

# Print some basic information about the dataset
print("Number of training reviews: {}".format(len(train_files)))
print("Number of testing reviews: {}".format(len(test_files)))
