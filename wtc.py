import urllib.request
import sys
from pyproj import Transformer
from osgeo import gdal, osr
with open("C:\lispovska\koordinata.txt") as f:
    lista = f.readline()
    listica = str(lista).split("|")
    xminhtrs = listica[0]
    yminhtrs = listica[1]
    xmaxhtrs = listica [2]
    ymaxhtrs = listica [3]
    kvaliteta = int(float(listica[4].strip()))
    if kvaliteta < 11:
        transformer = Transformer.from_crs("epsg:3765", "epsg:3857")
        xminpm, yminpm = transformer.transform(xminhtrs, yminhtrs)
        xmaxpm, ymaxpm = transformer.transform(xmaxhtrs, ymaxhtrs)
        xminzaopm = str(round(float(xminpm)))
        yminzaopm = str(round(float(yminpm)))
        xmaxzaopm = str(round(float(xmaxpm)))
        ymaxzaopm = str(round(float(ymaxpm)))


        duzinay = int(float(ymaxzaopm) - float(yminzaopm))
        duzinax = int(float(xmaxzaopm) - float(xminzaopm))
        duzinastrx = str(duzinax*4*kvaliteta)
        duzinastry = str(duzinay*4*kvaliteta)
        print(xminzaopm, yminzaopm, xmaxzaopm, ymaxzaopm, duzinastrx, duzinastry)
    else:
        sys.exit()

ime= "C:\lispovska\{}-EPSG3857.tiff".strip()
url = "http://xxxxxxx.xx/geoserver/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&LAYERS=xxx&TILED=true&STYLES=&CRS=EPSG:3857&BBOX={},{},{},{}&WIDTH={}&HEIGHT={}&FORMAT=image/geotiff&TRANSPARENT=TRUE&EXCEPTIONS=XML" #x part has to be replaced with actual wms geoserver domain
urllib.request.urlretrieve(url.format(xminzaopm,yminzaopm,xmaxzaopm,ymaxzaopm,duzinastrx,duzinastry),ime.format(xminzaopm))
alfa = gdal.Open(ime.format(xminzaopm))
imeb = "C:\lispovska\{}-EPSG3765.tiff"
ds = gdal.Warp(imeb.format(xminhtrs),alfa,dstSRS='EPSG:3765',dstAlpha=False, dstNodata=255)
alfahtrs = gdal.Open(imeb.format(xminhtrs))
beta = gdal.Info(alfahtrs)
print(beta)
gama = beta.find("Pixel Size")
pixsiz = beta[gama+14:gama+31]
delta = beta.find("Lower Left")
lowleftx = beta[delta+15:delta+25]
lowlefty = beta[delta+27:delta+38]
fa = open("C:\lispovska\koordinataizlaz.txt", 'w+')
fa.write(lowleftx+"\n")
fa.write(lowlefty+"\n")
fa.write(pixsiz)
fa.close()
