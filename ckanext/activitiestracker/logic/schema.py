from ckan.logic.validators import resource_id_exists, user_id_exists, package_id_exists
from ckan.lib.navl.validators import not_empty, ignore_missing

def resource_tracker_create_schema():
    schema = {
        'resource_id': [resource_id_exists],
        'package_id': [package_id_exists],
    }
    return schema