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

class ColonySite(colony.System):
    """
    The colony site class.
    """

    def load_components(self):
        """
        Loads the main components models, controllers, etc.
        This load should occur only after the dependencies are loaded.
        """

        # retrieves the mvc utils plugin and uses it to creates the
        # controllers and assigning them to the current instance
        mvc_utils_plugin = self.plugin.mvc_utils_plugin
        mvc_utils_plugin.assign_controllers(self, self.plugin)

    def unload_components(self):
        """
        Unloads the main components models, controllers, etc.
        This load should occur the earliest possible in the unloading process.
        """

        # retrieves the mvc utils plugin and uses it to destroy the
        # controllers, unregistering them from the internal structures
        mvc_utils_plugin = self.plugin.mvc_utils_plugin
        mvc_utils_plugin.unassign_controllers(self)

    def get_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as patterns,
        to the mvc service. The tuple should relate the route with the handler
        method/function.

        :rtype: Tuple
        :return: The tuple of regular expressions to be used as patterns,
        to the mvc service.
        """

        return (
            (r"colony_site/?", self.main_controller.landing, "get"),
            (r"colony_site/index", self.main_controller.index, "get"),
            (r"colony_site/landing", self.main_controller.landing, "get")
        )

    def get_resource_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as resource patterns,
        to the mvc service. The tuple should relate the route with the base
        file system path to be used.

        :rtype: Tuple
        :return: The tuple of regular expressions to be used as resource patterns,
        to the mvc service.
        """

        # retrieves the plugin manager and uses it to retrieve
        # the plugin path for resource path calculus
        plugin_manager = self.plugin.manager
        plugin_path = plugin_manager.get_plugin_path_by_id(self.plugin.id)

        return (
            (r"colony_site/resources/.+", (plugin_path + "/colony_site/resources/extras", "colony_site/resources")),
        )
