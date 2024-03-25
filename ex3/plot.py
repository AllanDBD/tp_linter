import numpy as np
import matplotlib.pyplot as plt

# Définition de la fonction
def function(x, y):
    return np.sin(x) * np.sin(y)

# Génération de valeurs pour x et y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = function(X, Y)

# Tracé du graphique 2D
plt.figure(figsize=(8, 6))
plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(label='sin(x)*sin(y)')
plt.title('Plot 2D de sin(x)*sin(y)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
