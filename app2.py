import geopandas as gpd

shapefile_path = 'poligono/poligono.shp'
gdf = gpd.read_file(shapefile_path)

# Dividir o shp
half_size = len(gdf) // 20000
# esquerda
part1 = gdf.iloc[:half_size]
# direita
part2 = gdf.iloc[half_size:]
# Salvar
part1.to_file('part1.shp')
part2.to_file('part2.shp')