#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Website
# Copyright (c) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Colony Website.
#
# Hive Colony Website is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Colony Website is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Colony Website. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import colony.base.system
import colony.base.decorators

class ColonySitePlugin(colony.base.system.Plugin):
    """
    The main class for the Colony Site plugin.
    """

    id = "pt.hive.cronus.plugins.colony_site"
    name = "Colony Site"
    description = "The plugin that offers the colony web site"
    version = "1.0.0"
    author = "Hive Solutions Lda. <development@hive.pt>"
    loading_type = colony.base.system.EAGER_LOADING_TYPE
    platforms = [
        colony.base.system.CPYTHON_ENVIRONMENT
    ]
    capabilities = [
        "mvc_service"
    ]
    dependencies = [
        colony.base.system.PluginDependency("pt.hive.colony.plugins.mvc.utils", "1.x.x")
    ]
    main_modules = [
        "colony_site.system"
    ]

    colony_site = None
    """ The colony site """

    mvc_utils_plugin = None
    """ The mvc utils plugin """

    def load_plugin(self):
        colony.base.system.Plugin.load_plugin(self)
        import colony_site.system
        self.colony_site = colony_site.system.ColonySite(self)

    def end_load_plugin(self):
        colony.base.system.Plugin.end_load_plugin(self)
        self.colony_site.load_components()

    def unload_plugin(self):
        colony.base.system.Plugin.unload_plugin(self)
        self.colony_site.unload_components()

    @colony.base.decorators.inject_dependencies
    def dependency_injected(self, plugin):
        colony.base.system.Plugin.dependency_injected(self, plugin)

    def get_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as patterns,
        to the mvc service. The tuple should relate the route with the handler
        method/function.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as patterns,
        to the mvc service.
        """

        return self.colony_site.get_patterns()

    def get_communication_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as communication patterns,
        to the mvc service. The tuple should relate the route with a tuple
        containing the data handler, the connection changed handler and the name
        of the connection.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as communication patterns,
        to the mvc service.
        """

        return self.colony_site.get_communication_patterns()

    def get_resource_patterns(self):
        """
        Retrieves the tuple of regular expressions to be used as resource patterns,
        to the mvc service. The tuple should relate the route with the base
        file system path to be used.

        @rtype: Tuple
        @return: The tuple of regular expressions to be used as resource patterns,
        to the mvc service.
        """

        return self.colony_site.get_resource_patterns()

    @colony.base.decorators.plugin_inject("pt.hive.colony.plugins.mvc.utils")
    def set_mvc_utils_plugin(self, mvc_utils_plugin):
        self.mvc_utils_plugin = mvc_utils_plugin
