def get_user_status(status):
    status_dict = {'pending': 1, 'active': 2, 'deactivate': 3, 'deleted': 4}
    if type(status).__name__ == 'int':
        for key, value in status_dict.items():
            if value == status:
                return key

    if status_dict.get(status):
        return status_dict[status]
    return 0


def get_user_type(user_type):
    user_type_dict = {'Admin': 1, 'User': 2, 'Service Provider': 3}
    if type(user_type).__name__ == 'int':
        for key, value in user_type_dict.items():
            if value == user_type:
                return key
    if user_type_dict.get(user_type):
        return user_type_dict[user_type]
    return 0


def get_status(status):
    status_dict = {'pending': 1, 'active': 2, 'deactivate': 3, 'deleted': 4}
    if type(status).__name__ == 'int':
        for key, value in status_dict.items():
            if value == status:
                return key

    if status_dict.get(status):
        return status_dict[status]
    return 0
