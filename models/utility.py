import os
import sys
from sklearn.model_selection import train_test_split

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def split_data(X, y, test_size=0.3):
    return train_test_split(X, y, test_size=test_size)
