import numpy as np
import matplotlib.pyplot as plt

# Création des valeurs x de -2pi à 2pi
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Calcul des valeurs des fonctions sinus en phase et en opposition de phase
y1 = np.sin(x)
y2 = np.sin(x + np.pi)

# Création de la figure et des sous-graphiques
plt.figure(figsize=(8, 6))

# Sous-graphique 1
plt.subplot(2, 1, 1)
plt.plot(x, y1, label='Sinus en phase')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Sous-graphique 2
plt.subplot(2, 1, 2)
plt.plot(x, y2, label='Sinus en opposition de phase')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

# Affichage du graphique
plt.tight_layout()
plt.show()