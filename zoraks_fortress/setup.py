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
        "SQLAlchemy==2.0.23",
        "flask-sqlalchemy==3.1.1"
        "blinker==1.7.0"
        "cachelib==0.10.2"
        "click==8.1.7"
        "itsdangerous==2.1.2"
        "jinja2==3.1.2"
        "markupsafe==2.1.3"
        "typing-extensions==4.8.0"
        "werkzeug==3.0.1"
    ],
    python_requires=">=3.10",
)