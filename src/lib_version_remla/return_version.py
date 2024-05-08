from importlib.metadata import version, PackageNotFoundError

class VersionUtil:
    def get_version():
        try:
            return version('lib_version_remla')
        except PackageNotFoundError:
            return version