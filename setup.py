try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

readme = open('README.rst').read()

setup(name="blinker",
      version='1.6.2',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      author='Jason Kirtland',
      author_email='jek@discorporate.us',
      maintainer="Pallets Ecosystem",
      maintainer_email="contact@palletsprojects.com",
      description='Fast, simple object-to-object and broadcast signaling',
      keywords='signal emit events broadcast',
      long_description=readme,
      long_description_content_type="text/x-rst",
      license='MIT License',
      url='https://blinker.readthedocs.io',
      project_urls={
        'Source': 'https://github.com/pallets-eco/blinker',
      },
      python_requires='>=3.7',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries',
          ],
)
