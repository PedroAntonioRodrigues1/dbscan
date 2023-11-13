import matplotlib.pyplot as plt
from geopy.distance import great_circle
from shapely.geometry import MultiPoint
from sklearn.cluster import DBSCAN
import numpy as np
import pandas as pd

coordenadas = np.array([
    [-15.7942, -47.8825],  # Brasília, DF
    [-23.5505, -46.6333],  # São Paulo, SP
    [-22.9068, -43.1729],  # Rio de Janeiro, RJ
    [-25.4284, -49.2733],  # Curitiba, PR
    [-30.0346, -51.2177],  # Porto Alegre, RS
    [-19.9208, -43.9378],  # Belo Horizonte, MG
    [-8.0476, -34.8770],   # Recife, PE
    [-12.9777, -38.5016],  # Salvador, BA
    [-3.7319, -38.5267],   # Fortaleza, CE
    [-16.6799, -49.2550],  # Goiânia, GO
    [-5.7936, -35.1986],   # Natal, RN
    [-1.4554, -48.4902],   # Belém, PA
    [-20.2976, -40.2958],  # Vitória, ES
    [-9.6498, -35.7089],   # Maceió, AL
    [-3.1019, -60.0250],   # Manaus, AM
])

kms_per_radian = 6371.0088
epsilon = 1.5 / kms_per_radian
db = DBSCAN(eps=epsilon, min_samples=1, algorithm='ball_tree', metric='haversine').fit(np.radians(coordenadas))
print(db.labels_)
