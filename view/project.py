import modal.project as modal_project


def find_by_account_id(account_id):
    return modal_project.find_by_account_id(account_id=account_id)


def find_by_id(id):
    return modal_project.find_by_id(id=id)