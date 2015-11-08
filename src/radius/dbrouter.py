class DBRouter(object):
    """
    A router to control all database operations on models in the
    auth application.
    """

    radiusmodels = (
    	'freeradius'
    )

    def db_for_read(self, model, **hints):
        """
        Attempts to read radius models go to radius
        """
        if model._meta.app_label in self.radiusmodels:
            return 'radius'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write radius models go to radius
        """
        if model._meta.app_label in self.radiusmodels:
            return 'radius'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the radiusmodels is involved.
        """
        if obj1._meta.app_label in self.radiusmodels or \
           obj2._meta.app_label in self.radiusmodels:
           return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the radius models only appears in the 'radius'
        database.
        """
        if app_label in self.radiusmodels:
            return db == 'radius'
        return None