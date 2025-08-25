1-  security.W009) : LA SECRET_KEY est trop courte 
2- security.W018 : debug toujours a true (fuite d'info)
3-  security.W012 : cookie session n'est pas securisé

Debug a false en prod :
Avec DEBUG=True, Django affiche les pages d’erreurs détaillées 
(stack trace, variables de contexte, chemins du serveur, configuration, parfois même la SECRET_KEY