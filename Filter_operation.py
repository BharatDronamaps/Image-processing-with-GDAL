## Filtering operation

import cv2
import numpy as np
from osgeo import gdal
from scipy.ndimage.filters import median_filter, sobel

Filepath_Filter = 'imgs/Example-filter.tif'

# initialize driver
driver = gdal.GetDriverByName('GTiff')

# read file
dataset = gdal.Open("Orthomosaic_export.tif")

# extract band
band = dataset.GetRasterBand(1)

# extract array from band
arr = band.ReadAsArray()

# write the filtered array
dataset_split = driver.Create(Filepath_Filter, dataset.RasterXSize, dataset.RasterYSize)
dataset_split.GetRasterBand(1).WriteArray(median_filter(arr, size=(5,5)))


