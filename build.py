import os
from conan.packager import ConanMultiPackager


# Common settings
username = "odant" if "CONAN_USERNAME" not in os.environ else None


if __name__ == "__main__":
    builder = ConanMultiPackager(
        username=username,
        exclude_vcvars_precommand=True
    )
    builder.add(
        settings={
            "os_build": "Windows",
            "arch_build": "x86_64"
        },
        options={},
        env_vars={},
        build_requires={}
    )
    builder.run()
