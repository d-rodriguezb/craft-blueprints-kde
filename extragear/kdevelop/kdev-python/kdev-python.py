import sys

import info

class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()
        self.description = "python support for kdevelop"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = "default"
        self.runtimeDependencies["extragear/kdevelop/kdevelop"] = "default"
        self.runtimeDependencies["extragear/kdevelop/kdev-php"] = "default"

from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        if ("Paths", "Python") in CraftCore.settings:
            python = os.apth.join(CraftCore.settings.get(), "python")
        else:
            python = sys.executable
        self.subinfo.options.configure.args = f" -DPYTHON_EXECUTABLE=\"{python}\""
