# SPDX-License-Identifier: BSD-2-Clause
# SPDX-FileCopyrightText: 2023 Jonah Brüchert <jbb@kaidan.im>

import info
from Package.PipPackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        self.svnTargets["master"] = ""
        self.defaultTarget = "master"


class Package(PipPackageBase):
    def __init__(self, **args):
        PipPackageBase.__init__(self)
