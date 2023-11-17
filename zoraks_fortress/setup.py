import setuptools

setuptools.setup(
    name="zoraks_fortress",
    description="A text-based Zorak adventure game.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "Flask==2.3.2",
        "Flask-Session==0.5.0",
        "SQLAlchemy==1.4.46",
    ],
    python_requires=">=3.10",
)