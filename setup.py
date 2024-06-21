from setuptools import setup

setup(
    name="punkweb_forms",
    version="0.0.1",
    author="Punkweb",
    author_email="punkwebnet@gmail.com",
    packages=["punkweb_forms"],
    url="https://github.com/Punkweb/punkweb-forms",
    license="BSD-3-Clause",
    description="An app to generate dynamic forms in Django.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
    include_package_data=True,
    package_data={"": ["README.md"]},
    install_requires=[
        "django>=4.0",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
)
