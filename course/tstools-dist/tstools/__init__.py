# tstools/__init__.py
from os.path import basename
from .moments import get_mean_and_var
from .vis import plot_histogram, plot_trajectory_subset

filename = basename(__file__)
print(f"Hello from {filename}")