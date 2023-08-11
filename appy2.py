import geopandas as gpd
from shapely.geometry import Polygon

# Carregar o shapefile contendo o polígono
shapefile_path = './poligono/poligono.shp'
gdf = gpd.read_file(shapefile_path)

# Suponha que o shapefile contenha apenas um polígono
poligono = gdf['geometry'][0]

# Dividir o polígono em 4 partes iguais
subpoligonos = poligono.divide(4)

# Criar um novo GeoDataFrame com os subpolígonos
gdf_subpoligonos = gpd.GeoDataFrame({'geometry': subpoligonos}, crs=gdf.crs)

# Salvar o GeoDataFrame resultante em um novo shapefile
output_shapefile_path = './subpoligonos.shp'
gdf_subpoligonos.to_file(output_shapefile_path)
