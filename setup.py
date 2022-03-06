import os
from setuptools import setup

rootdir = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(rootdir,"README.md"), 'r') as f:
    long_description = f.read()

setup(
    name="fair_sim",
    version="0.1.0",
    author="Daniele Inturri",
    author_email="daniele.inturri@sud.tu-darmstadt.de",
    description="Framework for simulating fmus and controller written in python.",
    long_description=long_description,
    url="https://git.rwth-aachen.de/fst-tuda/projects/digitalization/fair_sim/fair_sim_release",
    packages= ["fair_sim", "fair_sim.fmu_export", "fair_sim.simulation", "fair_sim.project"],
    install_requires = ["FMPy",
                        "alive_progress",
                        "h5py",
                        "matplotlib",
                        "numpy",
                        "pandas",
                        "OMpython @ git+https://git@github.com/OpenModelica/OMPython.git"],

    python_requires=">=3.9",
)
