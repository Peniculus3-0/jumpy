Installation OpenCR via le questionnaire de cartes : 

1.	Une fois l'IDE Arduino exécuté, cliquez sur Fichier → Préférences dans le menu supérieur de l'IDE. Lorsque la fenêtre Préférences apparaît, copiez et collez le lien suivant dans la zone de texte URL supplémentaires du gestionnaire de cartes. (Cette étape peut prendre environ 20 minutes.)

https://raw.githubusercontent.com/ROBOTIS-GIT/OpenCR/master/arduino/opencr_release/package_opencr_index.json

2.	Cliquez sur Outils → Tableau → Gestionnaire de carte.
3.	Tapez OpenCR dans la zone de texte pour trouver le package OpenCR by ROBOTIS. Une fois trouvé, cliquez sur Installer.
4.	Après l'installation, "INSTALLÉ" apparaîtra.
5.	Vérifiez si la carte OpenCR est maintenant dans la liste Outils → Carte. Cliquez dessus pour importer la source de la carte OpenCR.

Pour plus d’information :
https://emanual.robotis.com/docs/en/parts/controller/opencr10/#install-on-windows


Installation des librairies :

1.	Cliquez sur Croquis → Inclure une bibliothèque → Gérer les bibliothèques.
2.	Tapez Dynamixel2Arduino dans la zone de texte pour trouver la bibliothèque by ROBOTIS. Une fois trouvé, cliquez sur Installer.
3.	Après l'installation, "INSTALLÉ" apparaîtra.

Utilisation du code Arduino :

Il n’y a que trois commandes possibles pour utiliser le code à partir du moniteur série :
-	« j » pour sauter sans tourner.
-	« l » pour sauter et tourner vers la gauche.
-	« r » pour sauter et tourner vers la droite. 
L’instruction « w » est juste un état qui ne fais rien en attendant la prochaine instruction.

Une fois qu’un saut est initié, il y a trois façons possibles de terminer une boucle de saut :
-	Le saut est détecté par une baisse soudaine de courant.
-	L’arrêt d’urgence est activé à cause d’un courant trop élevé
-	L’arrêt manuel est activé en envoyant n’importe quel caractère dans le moniteur série. 

 
