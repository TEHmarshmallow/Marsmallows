from distutils.core import setup
setup(name='MRSspendfrom',
      version='1.0',
      description='Command-line utility for Marsmello "coin control"',
      author='Gavin Andresen',
      author_email='gavin@Marsmellofoundation.org',
      requires=['jsonrpc'],
      scripts=['spendfrom.py'],
      )
