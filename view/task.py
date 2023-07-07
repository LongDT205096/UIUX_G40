import modal.task as modal_task


def find_by_account_id(account_id):
    return modal_task.find_by_account_id(account_id=account_id)


def find_by_id(id):
    return modal_task.find_by_id(id=id)


def find_by_project_id(project_id):
    return modal_task.find_by_project_id(project_id=project_id)