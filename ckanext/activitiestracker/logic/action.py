import datetime

from ckan.logic import side_effect_free, check_access, get_or_bust
from ckan.logic import NotFound, ValidationError

from ckan.lib.navl.dictization_functions import validate

from ckanext.activitiestracker.logic.schema import resource_tracker_create_schema

from ckanext.activitiestracker.model import ResourceLog
from ckan.model import User

@side_effect_free
def resource_tracker_list(context, data_dict):
    '''Return the list of trackers for a particular resource
    :param resource_id: the id of the resource
    :param limit: the number of returning results
    :param offset: the offset to start returning results from
    '''
    check_access('resource_tracker_list', context, data_dict)
    
    resource_id = data_dict.get('resource_id')
    limit = data_dict.get('limit')
    offset = data_dict.get('offset')
    session = context['session']
    query = session.query(ResourceLog)

    if resource_id:
        query = query.filter(ResourceLog.resource_id == resource_id)
    if limit:
        query = query.limit(int(limit))
    if offset:
        query = query.offset(int(offset))

    trackers = query.all()

    return [tracker.as_dict() for tracker in trackers]

def resource_tracker_create(context, data_dict):
    '''Append a new resource tracker to the list of resource log
    :param resource_id: the id of the resource
    :param event: the action which the user take 
    :param obj_type: object type which the user action is applied to.
    :param user_id: the username of the user
    '''
    check_access('resource_tracker_create', context, data_dict)
    
    data, errors = validate(data_dict, resource_tracker_create_schema(), context)

    if errors:
        raise ValidationError(errors)
    
    logger = User.get(context.get('user'))
    if logger:
        tracker = ResourceLog(
        resource_id=data.get('resource_id'),
        event=data.get('event'),
        obj_type=data.get('obj_type'),
        user_id=logger.name,
        )
    else:
        tracker = ResourceLog(
        resource_id=data.get('resource_id'),
        event=data.get('event'),
        obj_type=data.get('obj_type'),
        user_id=None,
        )

    tracker.save()

    return tracker.as_dict()