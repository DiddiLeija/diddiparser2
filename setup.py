import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="diddiparser2",
    version="1.0.0",
    author="Diego Ramirez",
    author_email="dr01191115@gmail.com",
    description="The official DiddiScript parser.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://diddiparser2.readthedocs.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Operating System :: POSIX",
        "Operating System :: MacOS",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Unix",
        "Topic :: Software Development",
        "Topic :: Software Development :: Compilers",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Libraries",
    ],
    keywords="diddiscript python parser",
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "diddiparser2=diddiparser2.cli:main",
            "diddiscript-console=diddiparser2.parser:interactive_console",
            "diddiscript-editor=diddiparser2.editor.main:main",
        ],
    },
    project_urls={
        "Documentation": "http://diddiparser2.readthedocs.io",  # ReadTheDocs site
        "Tracker": "http://github.com/DiddiLeija/diddiparser2/issues",  # GitHub issues page
        "Source": "http://github.com/DiddiLeija/diddiparser2",  # source code on GitHub
    },
    install_requires=["colorama>=0.4.0"],
    zip_safe=False,
)
