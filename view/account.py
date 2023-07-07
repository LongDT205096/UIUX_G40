import modal.account as modal_account


def string_adjust(string: str, desired_length):
    if len(string) < desired_length:
        padded_string = string.ljust(desired_length)
    else:
        padded_string = string

    return padded_string


def login(username, password):
    user = modal_account.find_by_username(username=string_adjust(username, 20))
    if user is not None:
        if password == user.password.strip():
            return [True, user.username, user.name, user.id]

    return [False]


def find_by_id(id):
    return modal_account.find_by_id(id)