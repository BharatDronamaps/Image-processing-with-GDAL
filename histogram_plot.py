## Histogram plot

import numpy as np
import matplotlib.pyplot as plt
from osgeo import gdal, gdalconst

# read image file inside array
dataset = gdal.Open("open.tif")
band = dataset.GetRasterBand(1)
arr = band.ReadAsArray()

# plot histogram
# plt.hist(arr)
# plt.show()

fig = plt.hist(arr, histtype='step')
plt.title('Mean')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.savefig("histogram.png")
plt.show()
