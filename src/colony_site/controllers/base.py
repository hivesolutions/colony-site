#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Website
# Copyright (c) 2008-2020 Hive Solutions Lda.
#
# This file is part of Hive Colony Website.
#
# Hive Colony Website is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Colony Website is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Colony Website. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2020 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import colony

AVAILABLE_LOCALES = (
    "en_us",
)
""" The available locales """

controllers = colony.__import__("controllers")

class BaseController(controllers.Controller):

    def __init__(self, plugin, system):
        controllers.Controller.__init__(self, plugin, system)

    def template_file(self, template = "general.html.tpl", *args, **kwargs):
        request = kwargs.get("request", None)

        locale = self.get_locale(
            request,
            available_locales = AVAILABLE_LOCALES
        )

        return self.retrieve_template_file(
            file_path = template,
            locale = locale,
            *args,
            **kwargs
        )
