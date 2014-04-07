from distutils.core import setup

# https://github.com/pypa/pip/issues/289

class build_with_submodules(build):
    def run(self):
        if path.exists('.git'):
            check_call(['git', 'submodule', 'init'])
            check_call(['git', 'submodule', 'update'])
        build.run(self)

setup(
    cmdclass={"build": build_with_submodules},
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
