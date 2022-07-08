# -*- coding: utf-8 -*-
import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def registerOptions(self):
        self.options.dynamic.setDefault("buildType", "Release")

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/libxml2"] = None
        self.runtimeDependencies["libs/llvm-meta/clang"] = None

    def setTargets(self):
        self.svnTargets["master"] = "https://invent.kde.org/sdk/clazy.git"
        self.targetUpdatedRepoUrl["master"] = (["https://anongit.kde.org/clazy"], "https://invent.kde.org/sdk/clazy.git")

        for ver in ["1.10", "1.11"]:
            self.targets[ver] = f"https://download.kde.org/stable/clazy/{ver}/src/clazy-{ver}.tar.xz"
            self.targetDigestUrls[ver] = f"https://download.kde.org/stable/clazy/{ver}/src/clazy-{ver}.tar.xz.sha256"
            self.targetInstSrc[ver] = f"clazy-{ver}"
        self.patchToApply["1.11"] = [("0001-Allow-to-build-clazy-on-mac.patch", 1)]
        self.defaultTarget = '1.11'


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
        self.supportsClang = False
        if CraftCore.compiler.isMSVC():
            clangLib = os.path.join(CraftCore.standardDirs.craftRoot(), "lib", "craft_clang_plugins.lib")
            self.subinfo.options.configure.args = f"-DCLANG_LIBRARY_IMPORT='{clangLib}'"
