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
    description='PyQt Comic Viewer',
    url='https://github.com/yjg30737/pyqt-comic-viewer.git',
    install_requires=[
        'PyQt5>=5.15',
        'pyqt-style-setter @ git+https://git@github.com/yjg30737/pyqt-style-setter.git@main',
        'pyqt-custom-titlebar-setter @ git+https://git@github.com/yjg30737/pyqt-custom-titlebar-setter.git@main',
        'pyqt-toast @ git+https://git@github.com/yjg30737/pyqt-toast.git@main',
        'pyqt-viewer-widget @ git+https://git@github.com/yjg30737/pyqt-viewer-widget.git@main',
        'python-open-filepath-and-select @ git+https://git@github.com/yjg30737/python-open-filepath-and-select.git@main',
        'pyqt-svg-icon-pushbutton @ git+https://git@github.com/yjg30737/pyqt-svg-icon-pushbutton.git@main',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main',
        'pyqt-get-selected-filter @ git+https://git@github.com/yjg30737/pyqt-get-selected-filter.git@main'
    ]
)