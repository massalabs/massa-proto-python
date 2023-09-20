from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Massa proto python'
LONG_DESCRIPTION = 'Massa protobuf api generated using betterproto'

# Setting up
setup(
    name="massa_proto_python",
    version=VERSION,
    author="sd",
    author_email="<sd@massa.net>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "betterproto==2.0.0b6",
    ],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'
    keywords=['python'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
    ]
)
