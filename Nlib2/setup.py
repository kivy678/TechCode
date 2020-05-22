from distutils.core import setup, Extension
import os, shutil

if os.path.exists("build"):
    shutil.rmtree("build")


LibPath = os.path.dirname(os.path.realpath(__file__))
include_dir = os.path.join(LibPath, 'Nib/common')

module = Extension(
    'spam',
    define_macros=[("MAJOR_VERSION", "1"), ("MINOR_VERSION", "0")],
    include_dirs = [include_dir],
    # library_dirs = [],
    # libraries = [],
    sources=['basis.c',],
    #language="c++",
    #extra_compile_args=["-std=c++11", "-w", "-Wall", "-O2"],
)

setup(
    name="TechCode",
    version="0.5",
    description="TechCode",
    author="Kivy",
    author_email="kivy678@gmail.com",
    url="",
    ext_modules=[module]
)
