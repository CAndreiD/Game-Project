"""
Configurație aplicație Flask
"""

import os


class Config:
    """Configurație implicită"""
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False


class DevelopmentConfig(Config):
    """Configurație pentru dezvoltare"""
    DEBUG = True
    TESTING = False


class TestingConfig(Config):
    """Configurație pentru testare"""
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    """Configurație pentru producție"""
    DEBUG = False
    TESTING = False


# Selectează config pe baza mediului
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# Detectează mediul
FLASK_ENV = os.getenv('FLASK_ENV', 'development')
