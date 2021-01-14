from conans import ConanFile, tools
import os, re


class GNUMakeInstaller(ConanFile):
    name = "gnu_make_installer"
    version = "4.3.0"
    license = "GNU General Public License v3.0 https://www.gnu.org/licenses/gpl-3.0.html"
    description = "Binary GNU Make for Windows"
    url = "https://github.com/odant/conan-gnu_make_installer"
    settings = {
        "os_build": ["Windows"],
        "arch_build": ["x86_64", "x86"]
    }
    exports_sources = "src/*"
    build_policy = "missing"

    def source(self):
        content = tools.load("src/src/config.h.W32.template")
        re_pkg = re.compile("%PACKAGE%")
        content = re_pkg.sub("make", content)
        re_ver = re.compile("%VERSION%")
        content = re_ver.sub(self.version, content)
        tools.save("src/src/config.h.W32", content)
        os.remove("src/src/config.h.W32.template")

    def build(self):
        folder = os.path.join(self.source_folder, "src")
        arch = str(self.settings.arch_build)
        with tools.chdir(folder), tools.vcvars(self, arch=arch):
            args = ["--without-guile"]
            if arch == "x86":
                args.append("--x86")
            self.run("build_w32.bat %s" % " ".join(args))

    def package(self):
        self.copy("*gnumake.exe", dst=".", keep_path=False)
        src_exe = os.path.join(self.package_folder, "gnumake.exe")
        dst_exe = os.path.join(self.package_folder, "make.exe")
        os.rename(src_exe, dst_exe)

    def package_info(self):
        self.env_info.PATH.append(self.package_folder)

