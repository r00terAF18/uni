from django.apps import AppConfig


class ProfessorAppConfig(AppConfig):
    verbose_name = "اساتید"
    name = "professor_app"

    def ready(self):
        import professor_app.signals
