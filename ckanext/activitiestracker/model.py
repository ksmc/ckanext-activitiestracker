import datetime
import uuid

from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import types

import ckan.model as model

from ckan.model.domain_object import DomainObject
from ckan.model.meta import metadata, mapper
from ckan.model.types import make_uuid

class ResourceLog(DomainObject):

    @classmethod
    def get(cls, reference):
        return model.Session.query(cls).filter(cls.id == reference).first()

resource_log_table = Table('resource_log',metadata,
    Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
    Column('ea', types.UnicodeText),
    Column('ec', types.UnicodeText),
    Column('el', types.UnicodeText),
    Column('user_id', types.UnicodeText),
    Column('created', types.DateTime, default=datetime.datetime.utcnow),
)

mapper(ResourceLog, resource_log_table)

def setup():
    resource_log_table.create(checkfirst=True)