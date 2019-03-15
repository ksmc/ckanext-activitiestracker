#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from ckan import model

from ckan.lib.cli import CkanCommand

class ActivitiesTrackerCommand(CkanCommand):
    '''Activities tracker commands
    Usage:
      activitiestracker init-db
        - Create the resource_log table in the database
    '''

    summary = __doc__.split('\n')[0]
    usage = __doc__
    max_args = 5
    min_args = 0

    def __init__(self, name):
        super(ActivitiesTrackerCommand, self).__init__(name)

    def command(self):
        self._load_config()

        if len(self.args) == 0:
            self.parser.print_usage()
            sys.exit(0)

        print ''

        cmd = self.args[0]

        if cmd == 'initdb':
            self.setup_db()
        else:
            print 'command %s not recognized' % cmd

    def setup_db(self):
        from ckanext.activitiestracker.model import setup as db_setup
        db_setup()
        print 'resource_tracker table created'
        print ''

    