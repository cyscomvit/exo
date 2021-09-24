from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup_args = dict(
    name='exopassword',
    version='0.0.6',
    description='ExoPassword is a Password Strength Analyzing module which utilizes different Machine Learning models to predict the strength of your passwords.',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n',
    license='MIT',
    packages=find_packages(),
    author='Apratim Shukla, Mayank Tolani',
    author_email='apratimshukla6@gmail.com',
    keywords=['Exo', 'ExoPassword', 'PasswordAnalysis'],
    url='https://github.com/apratimshukla6/exo',
    download_url='https://pypi.org/project/exopassword/'
)

install_requires = ['requests', 'joblib', 'scikit-learn==0.24.1']

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires, include_package_data=True, package_data={'': ['*.joblib']})