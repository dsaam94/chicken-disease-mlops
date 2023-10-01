import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.1.0"

REPO_NAME = "chicken-disease-mlops"
AUTHOR_USER_NAME = "dsaam94"
SRC_REPO = "diseaseClassification"
AUTHOR_EMAIL = "dsaa94@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description = "A small python package for classiying disease app.",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"hhttps://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracking" : f"hhttps://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")

)
