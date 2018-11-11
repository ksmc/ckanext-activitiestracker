from ckan.plugins.toolkit import auth_allow_anonymous_access
import ckan.plugins as p
import ckan.authz as authz
import ckan.model as model
import ckan.lib.dictization.model_dictize as model_dictize
from ckan.logic.auth import (get_package_object, get_group_object,
                             get_resource_object)
from ckanext.resourceauthorizer.logic import auth
from ckan.logic.auth.get import package_show as ckan_package_show
from ckan.logic.auth.get import resource_show as ckan_resource_show
from ckan.logic.auth.update import resource_update as ckan_resource_update

@p.toolkit.auth_allow_anonymous_access
def resource_tracker_create(context, data_dict):
    '''Authorization check for creating a log for a resource
    '''
    resource_id = data_dict.get('resource_id')
    resourceObj = get_resource_object(context, {'id': resource_id})
    return auth.resource_show(context, {'id': resourceObj.id})

def resource_tracker_list(context, data_dict):
    '''Authorization check for getting a list of log for a resource
    '''
    resource_id = data_dict.get('resource_id')
    return ckan_resource_update(context, {'id': resource_id})