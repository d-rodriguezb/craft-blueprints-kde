import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        self.description = "An open, royalty-free video coding format designed for video transmissions over the Internet"
        for ver in ["3.1.3", "3.6.1", "3.8.0"]:
            self.targets[ver] = f"https://storage.googleapis.com/aom-releases/libaom-{ver}.tar.gz"
            self.targetInstSrc[ver] = f"libaom-{ver}"
        self.targetDigests["3.8.0"] = (['a768d3e54c7f00cd38b01208d1ae52d671be410cfc387ff7881ea71c855f3600'], CraftHash.HashAlgorithm.SHA256)
        self.defaultTarget = "3.8.0"
    def setDependencies(self):
        self.buildDependencies["dev-utils/cmake"] = None
        self.buildDependencies["dev-utils/perl"] = None
        self.buildDependencies["dev-utils/yasm"] = None
        self.runtimeDependencies["virtual/base"] = None


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        self.subinfo.options.dynamic.buildStatic = False
        self.subinfo.options.configure.args += ["-DENABLE_DOCS=OFF"]
