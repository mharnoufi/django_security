# Variable pour activer le mode sécurisé -> Active le mode sécurisé si la variable d'env DJANGO_SECURE=true
# Permet de différencier facilement environnement dev (DEBUG=True)
# et prod (DEBUG=False).
DJANGO_SECURE = os.getenv("DJANGO_SECURE","false").lower() == "true"

# En production, DEBUG doit être False ->  DEBUG doit absolument être False en production pour éviter de divulguer
# des informations sensibles dans les pages d'erreur Django.
DEBUG = not DJANGO_SECURE

# Domaine autorisés -> Liste des domaines autorisés pour éviter les attaques Host header injection.
ALLOWED_HOSTS = ["127.0.0.1","localhost"]

# Pour HTTPS local sur port 8443 -> Protection CSRF : définit les origines de confiance acceptées
# (utile pour POST en HTTPS depuis ces hôtes).
CSRF_TRUSTED_ORIGINS = [
    "https://127.0.0.1",
    "https://localhost",
    "https://127.0.0.1:8443",
]

# Cookies en HTTPS uniquement cookies accessibles uniquement en HTTPS -> empêche leur interception en clair.
SESSION_COOKIE_SECURE = DJANGO_SECURE
CSRF_COOKIE_SECURE = DJANGO_SECURE

# HTTPONLY : interdit l’accès aux cookies depuis JavaScript → réduit le risque XSS.
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True  

# # SameSite : empêche que les cookies soient envoyés depuis des sites tiers,
# réduisant le risque de CSRF. Mode "Lax" = compromis sécurité / compatibilité.
SESSION_COOKIE_SAMESITE = "Lax"  # adapte si besoin (iframe/OAuth)
CSRF_COOKIE_SAMESITE = "Lax"

# HTTPS et HSTS 
SECURE_SSL_REDIRECT = DJANGO_SECURE # Force la redirection en HTTPS en prod.

# Strict-Transport-Security : impose HTTPS au navigateur pendant 1 an (31536000s).
# Active uniquement si DJANGO_SECURE=True (prod).
SECURE_HSTS_SECONDS = 31536000 if DJANGO_SECURE else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = True # False si sous domaine en HTTP
SECURE_HSTS_PRELOAD = DJANGO_SECURE # True en prod si 100% HTTPS

# Protection contre le MIME sniffing -> Interdit au navigateur de "deviner" le type MIME -> évite attaques de type
# Content Sniffing (ex : interprétation d’un .txt comme du JS)
SECURE_CONTENT_TYPE_NOSNIFF = True

# Contrôle du header Referer -> # Politique de Referer → contrôle quelles infos de provenance sont envoyées.
# "strict-origin-when-cross-origin" = bon compromis (protection vie privée + compatibilité).
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"

# Protection contre le clickjacking (interdiction d’inclure le site dans une iframe).
X_FRAME_OPTIONS = "DENY"


#CSP stricte : n'autorise que les ressources de notre domaine
# CSP = protège contre XSS en limitant les ressources autorisées.
# Ici : n’autorise que les scripts/styles venant du domaine courant ('self').
CONTENT_SECURITY_POLICY = {
    "EXCLUDE_URL_PREFIXES": ["/admin"], 
    "DIRECTIVES": {
        "default-src": [SELF],     
        "script-src": [SELF],          
        "style-src": [SELF],              
        # "img-src": [SELF, "data:"],
    },
}

# En prod : la SECRET_KEY est chargée depuis l’environnement (.env).
# La valeur par défaut ("dev-only-insecure-key") ne doit JAMAIS être utilisée en prod
SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-insecure-key")

# Application definition

# Ajout du middleware CSP (Content Security Policy)
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "csp.middleware.CSPMiddleware", #middleware csp
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]