import info
from CraftCore import CraftCore


class subinfo(info.infoclass):
    def registerOptions(self):
        self.parent.package.categoryInfo.platforms = CraftCore.compiler.Platforms.NotAndroid

    def setTargets(self):
        self.versionInfo.setDefaultValues()

        self.description = "KDNSSD Framework"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = None


from Blueprints.CraftPackageObject import CraftPackageObject

class Package(CraftPackageObject.get("kde").pattern):
    def __init__(self):
        CraftPackageObject.get("kde").pattern.__init__(self)
