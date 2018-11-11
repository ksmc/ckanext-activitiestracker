import datetime
import uuid

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import types

import ckan.model as model

from ckan.model.domain_object import DomainObject
from ckan.model.meta import metadata, mapper
from ckan.model.types import make_uuid

class ResourceTracker(DomainObject):

    @classmethod
    def get(cls, reference):
        return model.Session.query(cls).filter(cls.id == reference).first()

resource_tracker_table = Table(
    'resource_traker',
    metadata,
    Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
    Column('package_id', types.UnicodeText),
    Column('resource_id', types.UnicodeText),
    Column('user_id', types.UnicodeText),
    Column('created', types.DateTime, default=datetime.datetime.utcnow),
)

mapper(ResourceTracker, resource_tracker_table)

def setup():
    resource_tracker_table.create(checkfirst=True)