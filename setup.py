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
    packages=['facenet',],
    license='MIT',
    long_description=open('README.md').read(),
    install_requires=install_requires,
    package_dir = {'facenet': 'src'}
)
