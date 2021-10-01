import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

Project_Name = "oneNeuron_perceptron_pypi"
user_name = "guptabhishek8"


setuptools.setup(
    name=f"{Project_Name}-{user_name}",
    version="0.0.2",
    author=user_name,
    author_email="guptabhishek8@gmail.com",
    description=" its a implementation of Perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{user_name}/{Project_Name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{user_name}/{Project_Name}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "tqdm",
        "pandas",
        "joblib",
        "matplotlib.pyplot",
        "matplotlib.colors",
    ]
)
