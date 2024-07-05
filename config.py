class Config:
 DEBUG = False
 DEVELOPMENT = False
 CSRF_ENABLED = True
 ASSETS_DEBUG = False

class ProductionConfig(Config):
 pass

class DevelopmentConfig(Config): 
 DEBUG = True
 DEVELOPMENT = True
 TEMPLATES_AUTO_RELOAD = True
 ASSETS_DEBUG = True

 api_key = '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'