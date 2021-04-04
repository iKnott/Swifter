import setuptools
with open("README.md","r") as fh:
	long_description = fh.read()

setuptools.setup(
	name = "Swifter",
	version = "0.0.1",
	author = "Sagnik Sarkar",
	email = "sagniksarkar.agt@gmail.com",
	long_description = long_description,
	long_description_content_type = "text/markdown",
	url = "https://github.com/iKnott/Swifter",
	packages = setuptools.find_packages(),
	classifiers = [
	"Programing Langauge :: Python :: 3",
	"Licence :: OSI Aproved :: MIT Licence",
	"Operating System :: OS Independent",
	],
	python_requires = '>3.5',
	)