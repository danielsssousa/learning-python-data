class DroneKamikaze:
    def __init__(self, carga, velocidade, distancia):
        self.carga = carga
        self.velocidade = velocidade
        self.distancia = distancia



drones = DroneKamikaze('50 Lbs', '100 Km/h', "500 KM")

print(f'Drone de Carga explosiva de:',drones.carga, 'Velocidade de:',  drones.velocidade,'E distancia aproxidmada:', drones.distancia)
