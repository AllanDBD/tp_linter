import matplotlib.pyplot as plt

# Lecture des données depuis le fichier city.dat
file_path = "ex3/city.dat"
data = []

with open(file_path, "r") as file:
    next(file)  # Ignorer la première ligne d'en-tête
    for line in file:
        city, population, surface_area = line.split()
        data.append((city, int(population), float(surface_area)))

# Extraction des données pour les tracés
cities = [city for city, _, _ in data]
population = [pop for _, pop, _ in data]
surface_area = [area for _, _, area in data]

# Tracer le graphique à barres
plt.figure(figsize=(10, 6))
plt.bar(cities, population, color='skyblue', label='Population')
plt.bar(cities, surface_area, color='orange', alpha=0.5, label='Surface Area (sq km)')
plt.xlabel('Villes')
plt.ylabel('Population / Surface Area (sq km)')
plt.title('Population vs. Surface Area of Cities')
plt.xticks(rotation=45, ha='right')
plt.legend()
plt.tight_layout()
plt.show()
