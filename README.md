# PYPINotifier

PyPi Notifier is a cross-platform desktop application that helps developers keep track of new releases of Python modules and libraries available on PyPI (Python Package Index). It is written in Python using the Tkinter GUI toolkit and runs on Windows, macOS, and Linux.

*Installation:*

To install PyPi Notifier, follow these steps:

- Install Python 3.x: https://www.python.org/downloads/
- Clone or download the PyPi Notifier repository: https://github.com/Sheriff-Sap/pypi-notifier
- Open a terminal/command prompt and navigate to the pypi-notifier directory.
- Install the required packages by running the command: pip install -r requirements.txt
- Run the application by running the command: python main.py

*Usage*

Once the application is running, it will automatically check PyPI for new releases of the modules and libraries listed in the 'config.ini' file. To add or remove modules from the watchlist, simply edit the 'config.ini' file.

The application displays a table with the module name, the latest version available on PyPI, and the date it was released. If a new release is found, a desktop notification is displayed.

The application also provides an option to automatically launch a web browser with the PyPI page for the module when a new release is detected.

*Topics*

The following topics were covered in the development of PyPi Notifier:

- Cross-platform development: PyPi Notifier was developed using Python and the Tkinter GUI toolkit, which allows it to run on Windows, macOS, and Linux.

- Package management: PyPi Notifier interacts with PyPI to retrieve the latest release information for a list of modules and libraries.

- Configuration management: PyPi Notifier uses a configuration file ('config.ini') to manage the list of modules and libraries to monitor.

- Desktop notifications: PyPi Notifier uses the system's native notification mechanism to display a desktop notification when a new release is detected.

- OOP principles: PyPi Notifier was developed using object-oriented programming principles, which allowed for better code organization, reusability, and maintainability.

Python modules and libraries: PyPi Notifier uses several third-party Python modules and libraries, including 'requests' for interacting with PyPI, 'configparser' for parsing the configuration file, and 'plyer' for displaying desktop notifications.

*Conclusion*

PyPi Notifier is a useful tool for Python developers who want to stay up-to-date with the latest releases of the modules and libraries they use. It is a simple, easy-to-use, and cross-platform application that can be easily customized to fit the user's needs.
