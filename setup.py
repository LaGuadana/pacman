from setuptools import setup, find_packages

setup(
    name="pacman-multiplayer",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "pygame>=2.0.0",
    ],
    entry_points={
        "console_scripts": [
            "pacman-server=server.main:main",
            "pacman-client=client.main:main",
        ],
    },
    python_requires=">=3.7",
)
