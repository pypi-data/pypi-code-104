# Copyright 2018-2020 Nick Anthony, Backman Biophotonics Lab, Northwestern University
#
# This file is part of PWSpy.
#
# PWSpy is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PWSpy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PWSpy.  If not, see <https://www.gnu.org/licenses/>.

import os
from pwspy_gui import appPath
dataDirectory = os.path.join(appPath, 'PWSAnalysisData')
analysisSettingsDirectory = os.path.join(dataDirectory, 'PWSAnalysisSettings')
extraReflectionDirectory = os.path.join(dataDirectory, 'ExtraReflection')
googleDriveAuthPath = os.path.join(dataDirectory, 'GoogleDrive')
