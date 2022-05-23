# -*- coding: utf-8 -*-
# Dioptas - GUI program for fast processing of 2D X-ray diffraction data
# Principal author: Clemens Prescher (clemens.prescher@gmail.com)
# Copyright (C) 2014-2019 GSECARS, University of Chicago, USA
# Copyright (C) 2015-2018 Institute for Geology and Mineralogy, University of Cologne, Germany
# Copyright (C) 2019 DESY, Hamburg, Germany
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# x - horizontal motor
# y - vertical motor
# z - focus

# 13-IDD config
epics_config = {
    'sample_position_x': '13IDD:m81',
    'sample_position_y': '13IDD:m83',
    'sample_position_z': '13IDD:m82',
    'sample_position_omega': '13IDD:m84',
    'ds_mirror': '13IDD:m24.RBV',
    'us_mirror': '13IDD:m23.RBV',
    'microscope': '13IDD:m67.RBV',
    'station': '13IDD',
}

# 13-BMD config
# epics_config = {
#     'sample_position_x': '13BMD:m89',
#     'sample_position_y': '13BMD:m90',
#     'sample_position_z': '13BMD:m91',
#     'sample_position_omega': '13BMD:m92',
#     'ds_mirror': '13BMD:m68.RBV',
#     'us_mirror': '13BMD:m65.RBV',
#     'microscope': '13BMD:m23.RBV',
#     'station': '13BMD',
# }
