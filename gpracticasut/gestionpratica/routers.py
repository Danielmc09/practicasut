class GestionPracticaRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read mi_app_2 models go to mi_db_2.
        """
        if model._meta.app_label == 'gestionpratica':
            return 'gpracticasut'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'gestionpratica':
            return 'gpracticasut'
        return None