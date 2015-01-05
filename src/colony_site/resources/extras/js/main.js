// Hive Colony Website
// Copyright (c) 2008-2015 Hive Solutions Lda.
//
// This file is part of Hive Colony Website.
//
// Hive Colony Website is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// Hive Colony Website is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with Hive Colony Website. If not, see <http://www.gnu.org/licenses/>.

// __author__    = João Magalhães <joamag@hive.pt>
// __version__   = 1.0.0
// __revision__  = $LastChangedRevision$
// __date__      = $LastChangedDate$
// __copyright__ = Copyright (c) 2008-2015 Hive Solutions Lda.
// __license__   = GNU General Public License (GPL), Version 3

jQuery(document).ready(function() {
            // creates the video player elements
            jQuery("video").player("default", {
                        mini : true
                    });

            // retrieves the view presentation
            var viewPresenation = jQuery("#view-presentation");

            // retrieves the view video
            var viewVideo = jQuery("#view-video");

            // retrieves the view or
            var viewOr = jQuery("#view-or");

            // retrieves the colony video element
            var colonyVideoElement = jQuery("#colony-promotional-video video");

            // registers for the click event on the view presentation
            viewPresenation.click(function(event) {
                        // retrieves the colony presentation
                        var colonyPresentation = jQuery("#colony-presentation");

                        // removes the view presentation
                        viewPresenation.remove();

                        // removes the view or
                        viewOr.remove();

                        // shows the colony presentation
                        colonyPresentation.show();
                    });

            // registers for the click event on the view video
            viewVideo.click(function(event) {
                        // retrieves the colony video
                        var colonyVideo = jQuery("#colony-promotional-video");

                        // removes the view presentation
                        viewVideo.remove();

                        // removes the view or
                        viewOr.remove();

                        // shows the colony video
                        colonyVideo.show();
                    });

            // registers for the maximize event on the colony video element
            colonyVideoElement.bind("maximize", function(event) {
                        // retrieves the element
                        var element = jQuery(this);

                        // retrieves the colony video
                        var colonyVideo = jQuery("#colony-promotional-video");

                        // retrieves the colony video with
                        colonyVideoWidth = colonyVideo.width();

                        // animate the expanding of the video with
                        colonyVideo.animate({
                                    width : colonyVideoWidth * 1.5
                                }, 350);
                    });

            // registers for the minimize event on the colony video element
            colonyVideoElement.bind("minimize", function(event) {
                        // retrieves the element
                        var element = jQuery(this);

                        // retrieves the colony video
                        var colonyVideo = jQuery("#colony-promotional-video");

                        // retrieves the colony video with
                        colonyVideoWidth = colonyVideo.width();

                        // animate the expanding of the video with
                        colonyVideo.animate({
                                    width : colonyVideoWidth / 1.5
                                }, 350);
                    });
        });
