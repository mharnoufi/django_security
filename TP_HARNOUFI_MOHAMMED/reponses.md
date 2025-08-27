# Réponses TP Sécurité Django

## Question Étape 3
Les 3 warnings que j'ai identifé:
1-  security.W009 : LA SECRET_KEY est trop courte 
2- security.W018 : debug toujours a true (fuite d'info)
3-  security.W012 : cookie session n'est pas securisé en utilisatn SESSIONS_COOKIE_SECURE -> pas d'envoi de session sur une connexion HTTP non chiffrée

## Question Étape 4
Debug doit être à false en prod car avec DEBUG=True, Django affiche les pages d’erreurs détaillées 
stack trace, variables de contexte, chemins du serveur, configuration, parfois même la SECRET_KEY donc un gros risque de sécurité.

## Question Étape 7
Le clickjacking est un site malveillant qui charge le site dans une iframe caché et place des boutons/image/pub par dessus
X_FRAME_OPTIONS = "DENY" -> interdit à notre site d'etre affiché dans une <iframe>