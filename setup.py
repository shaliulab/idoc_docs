import setuptools
import git

PACKAGE_NAME = "idoc"
packages = setuptools.find_packages()
print(packages)

with open("README.md", "r") as fh:
    long_description = fh.read()

repo = git.Repo()
git_hash = repo.head.object.hexsha
# attention. you need to update the numbers ALSO in the imgstore/__init__.py file
version = "1.0.1"

with open(f"{PACKAGE_NAME}/_version.py", "w") as fh:
    fh.write(f"__version__ = '{version}'\n")

setuptools.setup(
    name=PACKAGE_NAME,
    version=version,
    author="Antonio Ortega",
    author_email="antonio.ortega@kuleuven.be",
    description="Performing learning and memory experiments in Drosophila",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github/shaliulab/idoc",
    packages=packages,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Unix",
    ],
    install_requires = [
        'imutils', 'pyfirmata', 'opencv-python','numpy',
        'pandas', 'sklearn', 'netifaces', 'bottle',
        'gitpython', 'cheroot', 'requests'
    ],
    dependency_links= [
        'python_requires>=3.7.0',
    ],
    entry_points={
        'console_scripts': [
        ]
    }
)
