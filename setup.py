import setuptools

setuptools.setup(
    name="ppcc2019",
    version='0.0.2',
    description='Jupyter notebook for deep learning tutorial at ppcc 2019',
    author='Masahiko Saito',
    author_email='saito@icepp.s.u-tokyo.ac.jp',
    packages=setuptools.find_packages(),
    install_requires=[
        'matplotlib',
        'pandas',
        'sklearn',
        'jupyter',
        'graphviz',
        'pydotplus',
        'tensorflow',
        'keras',
    ],
)
