import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fictional-tribble",
    version="1.0.0",
    author="Faithfulness Alamu",
    description="Mass delete your GitHub repositories",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Information to filter the project on PyPi website
    python_requires=">=3.6",  # Minimum version requirement of the package
    py_modules=["fictional-tribble"],  # Name of the python package
    package_dir={"": "."},  # Directory of the source code of the package
    install_requires=[
        "click>=8.0.1",
        "requests>=2.26.0",
    ],  # Install other dependencies if any
)
