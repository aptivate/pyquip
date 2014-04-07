from distutils.core import setup

setup(
    name='pyquip',
    version='0.140407',
    author='Chris Wilson',
    author_email='support+pyquip@aptivate.org',
    packages=['pyquip'],
    url='http://github.com/aptivate/pyquip',
    license='LICENSE.txt',
    description='Simple installation and django-assets for jQuip',
    install_requires=[
        "django >= 1.5",
    ],
)
