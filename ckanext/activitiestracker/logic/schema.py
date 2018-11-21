from ckan.logic.validators import resource_id_exists, user_id_exists, package_id_exists
from ckan.lib.navl.validators import not_empty, ignore_missing

def resource_tracker_create_schema():
    schema = {
        'el': [resource_id_exists],
        'ec':[ignore_missing],
        'ea':[ignore_missing],
        
    }
    return schema