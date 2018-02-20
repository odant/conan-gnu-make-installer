from conans import ConanFile


class TestPackageGNUMakeInstaller(ConanFile):
    settings = "os_build", "arch_build"

    def test(self):
        self.run("make --version")

