from distutils.core import setup
import setuptools


def readme() -> str:
    with open(r'README.md') as f:
        README = f.read()
    return README


setup(
    name='pywhatkit',
    packages=setuptools.find_packages(),
    version='4.7',
    license='MIT',
    description='PyWhatKit is a Python library for Sending whatsapp message at certain time, it has several other features too.',
    author='Ankit Raj Mahapatra',
    author_email='ankitrajjitendra816@gmail.com',
    url='https://github.com/Ankit404butfound/PyWhatKit',
    download_url='https://github.com/Ankit404butfound/awesomepy/archive/1.0.tar.gz',
    keywords=['sendwhatmsg', 'info', 'playonyt', 'search', 'watch_tutorial'],
    install_requires=[
        'pyautogui',
        'wikipedia',
        'requests',
        'Pillow'
    ],
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 4 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
