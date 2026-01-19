from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'  # ← Innuma correct a irukku!
    
    def ready(self):
        import users.signals  # ← Intha line mathiri add pannu
