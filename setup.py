from setuptools import setup, find_packages

setup(
    name='pyqt-comic-viewer',
    version='0.4.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_comic_viewer.ico': ['book.svg', 'close.svg'],
                  'pyqt_comic_viewer.style': ['recent_file_widget.css']},
    description='PyQt comic viewer',
    url='https://github.com/yjg30737/pyqt-comic-viewer.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-style-setter>=0.0.1',
        'pyqt-custom-titlebar-setter>=0.0.1',
        'pyqt-viewer-widget>=0.0.1',
        'python-open-filepath-and-select @ git+https://git@github.com/yjg30737/python-open-filepath-and-select.git@main',
        'pyqt-svg-button>=0.0.1',
        'pyqt-resource-helper>=0.0.1',
        'pyqt-get-selected-filter @ git+https://git@github.com/yjg30737/pyqt-get-selected-filter.git@main'
    ]
)