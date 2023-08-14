import geopandas as gpd
from shapely.geometry import Polygon


shapefile_path = 'poligono/poligono.shp'
gdf = gpd.read_file(shapefile_path)

# Calcular a area total do shp
total_extent = gdf.total_bounds

# Calcular o ponto medio
midpoint_x = (total_extent[0] + total_extent[2]) / 2
midpoint_y = (total_extent[1] + total_extent[3]) / 2

# Criar dois polígonos
polygon1 = Polygon([(total_extent[0], total_extent[1]), (midpoint_x, total_extent[1]), (midpoint_x, total_extent[3]), (total_extent[0], total_extent[3])])
polygon2 = Polygon([(midpoint_x, total_extent[1]), (total_extent[2], total_extent[1]), (total_extent[2], total_extent[3]), (midpoint_x, total_extent[3])])

# Filtrar os dados do shp
parte1 = gdf[gdf.geometry.intersects(polygon1)]
parte2 = gdf[gdf.geometry.intersects(polygon2)]

# guardar
parte1.to_file('parte1.shp')
parte2.to_file('parte2.shp')