import info
from Blueprints.CraftPackageObject import CraftPackageObject
from CraftCore import CraftCore


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()
        # Windows build is fixed in 24.08.1
        # TODO: remove when defaultTarget is 24.08.1
        if CraftCore.compiler.isWindows:
            self.defaultTarget = "24.08.1"
        self.description = "Analitza Library"

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["libs/qt/qtbase"] = None
        self.runtimeDependencies["libs/qt/qtdeclarative"] = None

        self.buildDependencies["libs/eigen3"] = None

        if not CraftCore.compiler.isAndroid:
            self.runtimeDependencies["libs/glew"] = None


class Package(CraftPackageObject.get("kde").pattern):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
