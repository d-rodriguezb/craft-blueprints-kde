import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.description = "the poppler CJK encoding data"
        self.svnTargets["master"] = "git://git.freedesktop.org/git/poppler/poppler-data"

        # use poppler data matching the latest poppler release used in poppler.py
        v = "0.4.11"
        self.defaultTarget = v
        self.targets[v] = "https://poppler.freedesktop.org/poppler-data-" + v + ".tar.gz"
        self.targetInstSrc[v] = "poppler-data-" + v
        self.targetDigests[v] = (["2cec05cd1bb03af98a8b06a1e22f6e6e1a65b1e2f3816cb3069bb0874825f08c"], CraftHash.HashAlgorithm.SHA256)

    def setDependencies(self):
        self.runtimeDependencies["virtual/base"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
