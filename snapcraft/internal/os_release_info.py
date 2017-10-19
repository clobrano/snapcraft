# -*- Mode:Python; indent-tabs-mode:nil; tab-width:4 -*-
#
# Copyright (C) 2015-2017 Canonical Ltd
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 3 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Linux Standard Base OS release information

import logging

logger = logging.getLogger(__name__)


class OSReleaseInfo(object):

    os_release_dict = {}

    def from_file(self, os_release_file='/etc/os-release'):
        with open(os_release_file) as os_release_file:
            for line in os_release_file:
                entry = line.rstrip().split('=')
                if len(entry) == 2:
                    self.os_release_dict[entry[0]] = entry[1].strip('"')

    def get_name(self, default=None):
        try:
            return self.os_release_dict['NAME']
        except KeyError:
            return default

    def get_id(self, default=None):
        try:
            return self.os_release_dict['ID']
        except KeyError:
            return default

    def get_version_info(self, default=None):
        try:
            return self.os_release_dict['VERSION_INFO']
        except KeyError:
            return default

    def get_version_codename(self, default=None):
        try:
            return self.os_release_dict['VERSION_CODENAME']
        except KeyError:
            return default
