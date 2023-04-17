### Fonctionnalités

- Affichage de l'interface utilisateur avec un thème clair, sombre ou système.
- Recherche de dispositifs Bluetooth à proximité à l'aide du module bleak.
- Connexion à un dispositif Bluetooth sélectionné dans une liste déroulante.
- Animation du robot qui saute
- Lance le saut à distance par Bluetooth
- Affichage en temps réel de la vitesse et du couple actuels du moteur.

### Requis

1. Un ordinateur avec Python 3.x installé.
2. Un dispositif Bluetooth compatible pour contrôler le moteur.
3. Les modules Python suivants installés : customtkinter, PIL (Pillow), bleak, threading, os, logging, asyncio et turtle.
4. Lien vers les images des animations : https://drive.google.com/drive/folders/1fHX3-iR9xY-f3sybb7qTc169rCVtT3Wu?usp=sharing

  `pip install requirements.txt`
  
  ### Procédure
  
1. Assurez-vous que tous les prérequis sont satisfaits.
3. Exécutez le fichier UI.py pour lancer l'application.
4. L'application affichera l'interface utilisateur avec les options de recherche de dispositifs Bluetooth.
5. Sélectionnez un dispositif Bluetooth dans la liste déroulante et connectez-vous.

  ### Classe animation
  
- Affiche l'animation de repos et de saut du robot dans un frame custom Tkinter à une fréquence spécifié en bouclant les images en mémoire
- Charge les images dans des dictionnaires pour améliorer les performances

  


