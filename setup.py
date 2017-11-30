from setuptools import setup, find_packages

install_requires = [
    'tensorflow==1.2',
    'scipy',
    'scikit-learn',
    'opencv-python',
    'h5py',
    'matplotlib',
    'Pillow',
    'requests',
    'psutil'
]

setup(
    name='Facenet',
    version='0.1',
    packages=find_packages('src'),
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=install_requires,
    package_dir = {'': 'src'} 
)

# See below for issue with setuptools for package_dir
# it will break on "editable" install
#
# https://github.com/pypa/pip/issues/126
