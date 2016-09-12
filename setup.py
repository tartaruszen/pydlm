from setuptools import setup, find_packages

setup(
    name = 'pydlm',
    version = '0.1.0',
    author = 'Xiangyu Wang',
    author_email = 'wwrechard@gmail.com',
    description = ('An implementation of the Bayesian dynamic linear ' +
      'model in Python'),
    license = 'BSD',
    keywords = 'dlm bayes bayesian kalman filter smoothing dynamic model',
    url = 'http://wwrechard.github.com/PyDLM',
    packages = find_packages(),
    #package_data={'pykalman': ['datasets/descr/robot.rst', 'datasets/data/robot.mat']},
    classifiers = [
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Science/Research',
      'License :: OSI Approved :: BSD License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Time series analysis :: Scientific/Engineering :: Artificial Intelligence'
    ],
    include_package_data = False,
    install_requires = [
      'numpy',
      'matplotlib',
    ],
    tests_require = [
      'unittest',
    ],
    extras_require = {
        'docs': [
          'Sphinx',
        ],
        'tests': [
          'unittest',
        ],
    },
)
