import setuptools

setuptools.setup(
    name="kagebunshin", # Replace with your own username
    version="0.0.1",
    author="Andrieli Campagnaro",
    author_email="andricampagnaro@gmail.com",
    description="Teste de multiplos pacotes",
    long_description="Esse pacote permite fazer chamadas de pacotes internos",
    long_description_content_type="text/markdown",
    url="https://gitlab.com/conversaosgi/conversaosgi",
    packages=setuptools.find_packages("lib"),
    package_dir={"": "lib"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)