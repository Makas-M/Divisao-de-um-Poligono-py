import fiona
from shapely.geometry import Polygon, mapping
import matplotlib.pyplot as plt
from descartes import PolygonPatch
import geopandas as gpd


polyShp = fiona.open('./poligono/poligono.shp')

# Suponha que o shapefile contenha apenas um polígono
# polyShp = gdf['geometry'][0]

# Dividir o polígono em 4 partes iguais
subpoligonos = polyShp.divide(4)
# mostrar lista de coordenadas do poligonos
polyList = []
polyProperties = []

for poly in polyShp:
    polyGeom = Polygon(poly['geometry']['coordinates'][0])
    polyList.append(polyGeom)
    polyProperties.append(poly['properties'])

print(polyList[0])
print(polyProperties[0])
