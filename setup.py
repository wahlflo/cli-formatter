import setuptools

with open('README.md', mode='r', encoding='utf-8') as readme_file:
    long_description = readme_file.read()


setuptools.setup(
    name="cli-formatter",
    version="1.1.0",
    author="Florian Wahl",
    author_email="florian.wahl.developer@gmail.com",
    description="An utility for cli script to prettify their output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wahlflo/cli-formatter",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
