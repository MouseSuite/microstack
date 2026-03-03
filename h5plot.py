#!/usr/bin/env python3
import h5py
import matplotlib.pyplot as plt
import time
import numpy as np

# filename='/data2/Rodent/big.h5'
filename='/nafs/shattuck/RodentToolsData/Ex_488_Em_525_stitched.h5'
#filename='/data2/Rodent/Ex_488_Em_525_stitched_32nc.h5'

total_time = time.perf_counter()
# cache_size_bytes=269*229*32*32*32*2*2
# with h5py.File(filename,'r', rdcc_nbytes=cache_size_bytes) as slab:
with h5py.File(filename,'r') as slab:
  axial=np.zeros((8587,7321),np.uint16)
  for z in range(1792,1842,1):
    start_time = time.perf_counter()
    axial=axial+slab['stack'][z,:,:]
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"slice time (z={z}): {elapsed_time:.4f} seconds")
  print(f"total time: {time.perf_counter()-total_time:.4f} seconds")
  imgplot = plt.imshow(axial)
  plt.show()

with h5py.File(filename,'r') as slab:#,rdcc_nbytes=cache_size_bytes)
  coronal=np.zeros((3600,7321),np.uint16)
  for y in range(4160,4210,1):
    start_time = time.perf_counter()
    coronal=coronal+slab['stack'][:,y,:]
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"slice time (y={y}): {elapsed_time:.4f} seconds")
  print(f"total time: {time.perf_counter()-total_time:.4f} seconds")
  imgplot = plt.imshow(coronal)
  plt.show()

with h5py.File(filename,'r') as slab:#,rdcc_nbytes=cache_size_bytes)
  sagittal=np.zeros((3600,8587),np.uint16)
  for x in range(3520,3570,1):
    start_time = time.perf_counter()
    sagittal=sagittal+slab['stack'][:,:,x]
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"slice time (x={x}): {elapsed_time:.4f} seconds")
  print(f"total time: {time.perf_counter()-total_time:.4f} seconds")
  imgplot = plt.imshow(sagittal)
  plt.show()


