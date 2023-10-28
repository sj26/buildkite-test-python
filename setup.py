import setuptools

setuptools.setup(
    name="buildkite-test-python",
    version="0.0.1",
    author="Buildkite Developer",
    author_email="dev@buildkite.com",
    description="A small example package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
