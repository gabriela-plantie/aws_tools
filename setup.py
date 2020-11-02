import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aws_tools",
    version="0.0.1",
    author="Gabriela Plantie",
    author_email="glplantie@gmail.com",
    description="AWS Tools for Athena from SageMaker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gabriela-plantie/aws_tools",
    packages=setuptools.find_packages(),
    install_requires=[
        'awswrangler>=1.8.1',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)