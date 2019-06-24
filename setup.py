from setuptools import setup

setup(name='blackqueen',
      version='0.1',
      description='Black Queen is a self learning Loosing-Chess engine using supervised and reinforcement learning.',
      url='https://github.com/mmagorsc/blackqueen',
      author='Max Magorsch',
      author_email='max@magorsch.de',
      license='MIT',
      packages=['blackqueen'],
      install_requires=[
          'tensorflow-gpu',
          'keras',
          'profilehooks',
          'numpy',
          'pyperclip',
          'python-chess',
          'ujson',
          'h5py'
      ],
      zip_safe=False)
