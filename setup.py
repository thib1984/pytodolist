from setuptools import setup

setup(name='pypodo',
      version='0.3.0',
      description='pypodo is a todolist program who works with a .todo file at the root of the home directory : use pypodo to run it',
      url='https://github.com/thib1984/pypodo',
      author='thib1984',
      author_email='thibault.garcon@gmail.com',
      license='mit',
      packages=['pypodo'],
      zip_safe=False,
      entry_points = {
          'console_scripts': ['pypodo=pypodo.__pypodo__:pypodo'],
      }
)
