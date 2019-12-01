from setuptools import find_packages, setup

setup(
    name="sds011-pm-sensor-python",
    version="0.0.1",
    description="A parser for the sds011 pm sensor serial interface",
    author="Jesse Collis",
    author_email="jesse@jcmultimedia.com.au",
    url="https://github.com/jessedc/sds011-pm-sensor-python",
    packages=find_packages(exclude=["*.tests"]),
    test_suite="sds011.tests",
    install_requires=[
        "influxdb>=5.2",
        "pyserial>=3.4"
    ],
    setup_requires=[
    ],
    tests_require=[
    ],
    entry_points={
        "console_scripts": [
            "sds011 = sds011.__main__:main",
        ],
    },
)
