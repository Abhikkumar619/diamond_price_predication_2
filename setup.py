import setuptools



REPO_NAME="diamond_price_predication_2"
AUTHOR_USER_NAME="Abhikkumar619"
SRC_REP='Diamond_project'
AUTHOR_EMAIL="abisheky194@gmail.com"
__version__="0.0.0.1"


setuptools.setup(
    name=SRC_REP,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    
)