from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

# with open("requirements.txt") as f:
#     requirements = f.read().splitlines()

setup(
    name="calculadora-jfmatta",
    version="0.0.1",
    author="JulianoMata",
    author_email="jfmatta@gmail.com",
    description="Cálculos simples",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JulianoMata/calculadora",
    packages=find_packages(),
    # install_requires=requirements,
    python_requires='>=3.8',
)