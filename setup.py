import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = [
    "setuptools>=40.0.0",
    "Cython",
    "scipy",
    "oct2py",
    "pesq",
    "sox",
]

setuptools.setup(
    name="semetrics",
    version="0.0",
    author="Huy Le Nguyen",
    author_email="nlhuy.cs.16@gmail.com",
    description="Speech Enhancement Metrics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/usimarit/semetrics",
    packages=setuptools.find_packages(include=["semetrics*"]),
    package_data={
        "semetrics": ["*.m"]
    },
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "License :: OSI Approved :: Apache-2.0 License",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    python_requires='>=3.6',
)
