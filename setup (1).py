from setuptools import setup, find_packages

setup(
    name="pad",
    version="0.0.1",
    author="wilfredo henao",
    author_email="wilfredo.henao@est.iudigital.edu.co",
    description="actividad programacion oob",
    py_modules=["actividad_1","actividad_2"],
    install_requires=[
        "matplotlib",
        "seaborn",
        "pandas",
        "numpy",
        "openpyxl",
        "requests"
    ]
) 