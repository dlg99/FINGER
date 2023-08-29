import h5py
import numpy as np
import shutil
import argparse
import os

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('source', help='the path of the hdf5 file')
parser.add_argument('destination', help='the destination directory')
args = parser.parse_args()

# Open the HDF5 file
with h5py.File(args.source, 'r') as f:
    print("Keys: %s" % f.keys())
    # Extract the data
    train_data = np.array(f['train'])
    test_data = np.array(f['test'])
    neighbor_data = np.array(f['neighbors'])

# Save the data in .npy format
np.save('X.trn.npy', train_data)
np.save('X.tst.npy', test_data)
np.save('Yi.tst.npy', neighbor_data)

# Move the .npy files to the destination directory
shutil.move('X.trn.npy', os.path.join(args.destination, 'X.trn.npy'))
shutil.move('X.tst.npy', os.path.join(args.destination, 'X.tst.npy'))
shutil.move('Yi.tst.npy', os.path.join(args.destination, 'Yi.tst.npy'))
