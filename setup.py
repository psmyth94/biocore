from setuptools import find_packages, setup

REQUIRED_PACKAGES = [
    "numpy>=1.17",
    "pandas",
    "pyarrow>=15.0.0",
]

QUALITY_REQUIRE = ["ruff>=0.1.5"]

DOCS_REQUIRE = [
    # Might need to add doc-builder and some specific deps in the future
    "s3fs",
]

TESTS_REQUIRE = [
    "pytest",
    "pytest-timeout",
    "pytest-xdist",
    "polars>=0.20.5",
    "timezones>=0.10.2",
    "biosets",
    "datasets",
]

EXTRAS_REQUIRE = {
    "polars": ["polars>=0.20.5", "timezones>=0.10.2"],
    "datasets": ["datasets"],
    "biosets": ["biosets"],
    "test": QUALITY_REQUIRE + TESTS_REQUIRE + DOCS_REQUIRE,
    "quality": QUALITY_REQUIRE,
    "docs": DOCS_REQUIRE,
}

setup(
    name="biocore",
    version="1.0.2",  # expected format is one of x.y.z.dev0, or x.y.z.rc1 or x.y.z (no to dashes, yes to dots)
    description="Bioinformatics datasets and tools for bio-family projects",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Patrick Smyth",
    author_email="psmyth1994@gmail.com",
    url="https://github.com/psmyth94/biocore",
    download_url="https://github.com/psmyth94/biocore/tags",
    license="Apache 2.0",
    package_dir={"": "src"},
    packages=find_packages("src"),
    include_package_data=True,
    python_requires=">=3.8.0,<3.12.0",
    install_requires=REQUIRED_PACKAGES,
    extras_require=EXTRAS_REQUIRE,
    zip_safe=False,  # Required for mypy to find the py.typed file
)
