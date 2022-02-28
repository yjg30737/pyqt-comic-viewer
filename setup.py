from setuptools import setup, find_packages

setup(
    name='pyqt-comic-viewer',
    version='0.1.0',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_comic_viewer.ico': ['close.png']},
    description='PyQt Comic Viewer',
    url='https://github.com/yjg30737/pyqt-comic-viewer.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-custom-titlebar-window @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-window.git@main',
        'pyqt-dark-gray-theme @ git+https://git@github.com/yjg30737/pyqt-dark-gray-theme.git@main'
        'pyqt-toast @ git+https://git@github.com/yjg30737/pyqt-toast.git@main',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main',
        'pyqt-viewer-widget @ git+https://git@github.com/yjg30737/pyqt-viewer-widget.git@main',
        'python-open-filepath-and-select @ git+https://git@github.com/yjg30737/python-open-filepath-and-select.git@main',
    ]
)