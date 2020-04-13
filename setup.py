import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="knotify",  # Replace with your own username
    version="0.0.1",
    author="George Miao",
    author_email="ge@georgemiao.com",
    description="A simple notification pusher",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GeorgeMiao219/Knotify",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)