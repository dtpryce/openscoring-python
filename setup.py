from distutils.core import setup

setup(
	name = "openscoring-dev",
	version = "0.1.1",
	description = "Python client library for the Openscoring REST web service (https://github.com/jpmml/openscoring)",
	author = "David Pryce",
	author_email = "dtpryce1988@gmail.com",
	url = "https://github.com/jpmml/openscoring-python",
	license = "GNU Affero General Public License (AGPL) version 3.0",
	packages = ["openscoring-dev"],
	install_requires = [
		"requests"
	]
)