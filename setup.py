from setuptools import setup, find_packages

setup(
    name='pyqt-comic-viewer',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    package_data={'pyqt_comic_viewer.ico': ['close.png'],
                  'pyqt_comic_viewer.style': ['button.css', 'dark_gray_theme.css', 'text_button.css']},
    description='PyQt Comic Viewer',
    url='https://github.com/yjg30737/pyqt-comic-viewer.git',
    install_requires=[
        'PyQt5>=5.8',
        'pyqt-toast @ git+https://git@github.com/yjg30737/pyqt-toast.git@main',
        'pyqt-resource-helper @ git+https://git@github.com/yjg30737/pyqt-resource-helper.git@main',
        'pyqt-viewer-widget @ git+https://git@github.com/yjg30737/pyqt-viewer-widget.git@main',
        'python-open-filepath-and-select @ git+https://git@github.com/yjg30737/python-open-filepath-and-select.git@main',
    ]
)