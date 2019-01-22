# from distutils.core import setup
from setuptools import setup

setup(
    name='pypexels',
    version='1.0.0b3',
    packages=['pypexels', 'pypexels.src'],
    url='https://github.com/salvoventura/pypexels',
    license='MIT',
    author='salvatore ventura',
    author_email='salvoventura@gmail.com',
    description='A Python wrapper for the Pexels.com REST API',
    classifiers=[
                      # How mature is this project? Common values are
                      #   3 - Alpha
                      #   4 - Beta
                      #   5 - Production/Stable
                      'Development Status :: 4 - Beta',

                      # Indicate who your project is intended for
                      'Intended Audience :: Developers',

                      # Pick your license as you wish (should match "license" above)
                      'License :: OSI Approved :: MIT License',

                      # Specify the Python versions you support here. In particular, ensure
                      # that you indicate whether you support Python 2, Python 3 or both.
                      'Programming Language :: Python :: 2.7',
                      'Programming Language :: Python :: 3.5',
                      'Programming Language :: Python :: 3.6'
                  ],
    keywords=['pexels', 'rest', 'api', 'python', 'wrapper', 'development', 'pexels.com', 'photography'],
    install_requires=['requests'],
    python_requires='>=2.7'
)
