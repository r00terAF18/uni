from django.apps import AppConfig


class ProfessorAppConfig(AppConfig):
    verbose_name = "اساتید | دانشکده"
    name = "professor_app"

    def read():
        import professor_app.signals
