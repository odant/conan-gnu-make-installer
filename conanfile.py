from conans import ConanFile, tools
import os


class GNUMakeInstaller(ConanFile):
    name = "gnu_make_installer"
    version = "4.2.1"
    license = "GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.html"
    description = "Binary GNU Make for Windows"
    url = "https://github.com/odant/conan-gnu_make_installer"
    settings = {
        "os_build": ["Windows"],
        "arch_build": ["x86_64"]
    }
    exports_sources = "src/*"
    build_policy = "missing"

    def build(self):
        folder = os.path.join(self.source_folder, "src")
        with tools.chdir(folder):
            self.run("build_w32.bat)

    def package(self):
        self.copy("*gnumake.exe", dst=".", keep_path=False)
        src_exe = os.path.join(self.package_folder, "gnumake.exe")
        dst_exe = os.path.join(self.package_folder, "make.exe")
        os.rename(src_exe, dst_exe)

    def package_info(self):
        self.env_info.PATH.append(self.package_folder)

