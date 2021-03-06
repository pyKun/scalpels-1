#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author: Kun Huang <academicgareth@gmail.com>

from scalpels.cli.api import api as agent_api
from prettytable import PrettyTable


def run(config):
    tracers = agent_api.get_tracer_list()
    t = PrettyTable(["tracer", "tracer script"])
    for tracer, script in tracers.items():
        t.add_row([tracer, script])
    print t
