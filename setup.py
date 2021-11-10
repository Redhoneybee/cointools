from setuptools import setup, find_packages

setup(
    name="cointools",
    version="1.0.2",
    license='MIT',
    author="redhoneybee",
    author_email="flack319@gmail.com",
    description="simple using threading to invest about bitcoin.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Redhoneybee/cointools",
    keywords=["bitcoin", "invest", "thread", "threading", "tools"],
    packages=find_packages(where="cointools", exclude = ["test.*, tests.*"])
)
    