from distutils.core import setup
import setuptools

def readme():
    with open(r'README.md') as f:
        README = f.read()
    return README

setup(
    name = 'pywhatBapi',
    packages = setuptools.find_packages(),
    version = '1.0',
    license='MIT',
    description = 'PyWhatBapi is a Python library for Sending whatsapp messages to many unsaved mobile numbers, using a csv file as a Database, the mobile numbers and specif messages can stored in the csv file.',
    author = 'Sai Jeevan Puchakayala',
    author_email = 'saijeevan2002@gmail.com',
    url = 'https://github.com/SaiJeevanPuchakayala',
    download_url = 'https://github.com/SaiJeevanPuchakayala/pywhatBapi.git',
    keywords = ['sendwhatmsgs'],
    install_requires=[
          'pyautogui',
          'time',
          'pandas',
          'webbrowser',
        ],
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
    'Development Status :: 1 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    ],
)