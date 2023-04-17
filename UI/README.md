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

  `pip install requirements.txt`
  
  ### Procédure
  
1. Assurez-vous que tous les prérequis sont satisfaits.
3. Exécutez le fichier UI.py pour lancer l'application.
4. L'application affichera l'interface utilisateur avec les options de recherche de dispositifs Bluetooth.
5. Sélectionnez un dispositif Bluetooth dans la liste déroulante et connectez-vous.

  ### Classe animation
  
- Affiche l'animation de repos et de saut du robot dans un frame custom Tkinter à une fréquence spécifié en bouclant les images en mémoire
- Charge les images dans des dictionnaires pour améliorer les performances
  
Voici les attributs et les méthodes :
  
  1. fps_idle : Nombre d'images secondes de l'animation au repos
  2. fps_jump : Nombre d'images secondes de l'animation de saut
  3. bool : booléen pour changer entre les animations
  4. num_frames_jump : Nombres d'images dans l'animaton de saut
  5. num_frames_idle : Nombres d'images dans l'animaton de repos
  6. size_x/size_y : Dimensions de l'animation
  7. folder_name : Path du dossie avec les images
  8. frames : Nom des dictionnaires
  9. idle() : Affiche l'animation au repos
  10. jump() : Affiche l'anomation de saut
  11. boolean()/boolean_false() : Modifie bool

