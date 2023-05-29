import info
from CraftCore import CraftCore


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()
        self.description = "Spelling framework for Qt, plugin-based."

    def registerOptions(self):
        # hunspell just when needed, on Windows(visual studio) or Mac we try with the OS specific checkers
        self.options.dynamic.registerOption("useHunspell", CraftCore.compiler.isLinux)

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["libs/qt/qtbase"] = None

        if self.options.dynamic.useHunspell:
            self.runtimeDependencies["libs/hunspell"] = None


from Blueprints.CraftPackageObject import CraftPackageObject


class Package(CraftPackageObject.get("kde").pattern):
    def __init__(self):
        CraftPackageObject.get("kde").pattern.__init__(self)

        # always use just hunspell, if at all!
        self.subinfo.options.configure.args += ["-DCMAKE_DISABLE_FIND_PACKAGE_ASPELL=ON"]
        if not self.subinfo.options.dynamic.useHunspell:
            self.subinfo.options.configure.args += ["-DCMAKE_DISABLE_FIND_PACKAGE_HUNSPELL=ON"]
