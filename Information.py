## Extraction of data from raster file

from osgeo import gdal
import sys

dataset = gdal.Open("Orthomosaic_export.tif")

if dataset is None:
      print('Could not open "open.tif" file')
      sys.exit( 1 )

print "Driver: %s/%s" % (dataset.GetDriver().ShortName, dataset.GetDriver().LongName)
print "Size is %d, %d" %(dataset.RasterXSize, dataset.RasterYSize)
print "Bands = %d" % dataset.RasterCount
print "Coordinate System is:", dataset.GetProjectionRef ()
print "GetGeoTransform() = ", dataset.GetGeoTransform ()
print "GetMetadata() = ", dataset.GetMetadata ()
