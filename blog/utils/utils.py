

class UtilsClass(object):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(UtilsClass, cls).__new__(cls)
        return cls.__instance

    def get_author_name(self, user):
        return f"{user.first_name} {user.last_name}" 