from setuptools import setup, find_packages

setup(
    name="lyzr",
    version="0.1.26",
    author="lyzr",
    description="",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="",
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8.1, <3.12",
    install_requires=[
        "asyncio",
        "nest_asyncio",
        "openai==1.3.4",
        "litellm==1.2.0",
        "llama-index==0.9.4",
        "langchain==0.0.339",
        "python-dotenv>=1.0.0",
        "beautifulsoup4==4.12.2",
        "pandas==2.0.2",
        "weaviate-client==3.25.3",
        "llmsherpa",
    ],
    extras_require={
        "data-analyzr": [
            "scikit-learn==1.4.0",
            "statsmodels==0.14.1",
            "chromadb==0.4.22",
            "tabulate==0.9.0",
            "pmdarima==2.0.4",
            "openpyxl==3.1.2",
            "matplotlib==3.8.2",
            "redshift_connector==2.0.918",
            "mysql-connector-python==8.2.0",
            "psycopg2-binary==2.9.9",
            "snowflake-connector-python==3.6.0",
        ],
    },
)
