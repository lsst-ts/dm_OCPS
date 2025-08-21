import setuptools
import setuptools_scm

setuptools.setup(
    version=setuptools_scm.get_version(write_to="python/lsst/dm/OCPS/version.py")
)
