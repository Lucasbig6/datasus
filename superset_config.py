import os

# Chave de segurança
SECRET_KEY = os.environ.get("SUPERSET_SECRET_KEY", "chave_secreta_monisus_ambiente_dev_123")

# Aponta para o container PostgreSQL do Docker Compose
POSTGRES_USER = os.environ.get("POSTGRES_USER", "superset")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "superset_password")
POSTGRES_DB = os.environ.get("POSTGRES_DB", "superset")

SQLALCHEMY_DATABASE_URI = os.environ.get(
    "SQLALCHEMY_DATABASE_URI",
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}"
)

# Configurações de idioma
BABEL_DEFAULT_LOCALE = "pt_BR"

LANGUAGES = {
    "pt_BR": {"flag": "br", "name": "Português (Brasil)"},
    "en": {"flag": "us", "name": "English"},
}

# Upload de CSV
UPLOAD_FOLDER = "/app/superset_home/uploads"

# Permitir SQLite (apenas para desenvolvimento)
PREVENT_UNSAFE_DB_CONNECTIONS = False
