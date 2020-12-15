from conans import ConanFile, tools, CMake


class LibsrtpConan(ConanFile):
    name = "libsrtp"
    version = "2.3.0-dev"
    settings = "os", "compiler", "build_type", "arch"
    description = "<Description of Libsrtp here>"
    url = "None"
    license = "None"
    author = "None"
    topics = None
    exports_sources = "**"
    generators = "cmake"

    def configure(self):
        del self.settings.compiler.libcxx

    def build_env(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        self.build_env().build()

    def package(self):
        self.build_env().install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
