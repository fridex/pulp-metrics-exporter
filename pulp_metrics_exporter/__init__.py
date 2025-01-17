#!/usr/bin/env python3
# pulp-metrics-exporter
# Copyright(C) 2022 Fridolin Pokorny
# Based on Thoth's metrics-exporter code.
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""This is a Prometheus Metrics exporter for Pulp."""


from thoth.common import __version__ as __common__version__
from thoth.common import init_logging

__version__ = "0.0.0"
__service_version__ = f"{__version__}+common.{__common__version__}"


# Init logging here when gunicorn import this application.
init_logging()
