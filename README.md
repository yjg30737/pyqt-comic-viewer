# pyqt-comic-viewer
PyQt Comic Viewer

## Requirements
* PyQt5 >= 5.15

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-comic-viewer.git --upgrade```

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-custom-titlebar-window.git">pyqt-custom-titlebar-window</a> - For frameless window
* <a href="https://github.com/yjg30737/pyqt-dark-gray-theme.git">pyqt-dark-gray-theme</a> - For theme
* <a href="https://github.com/yjg30737/pyqt-toast.git">pyqt-toast</a> - For notify window
* <a href="https://github.com/yjg30737/pyqt-resource-helper.git">pyqt-resource-helper</a> - For setting icon
* <a href="https://github.com/yjg30737/pyqt-viewer-widget.git">pyqt-viewer-widget</a> - Package which includes parent class of ```ComicBookViewerWidget```(```ViewerWidget```) 
* <a href="https://github.com/yjg30737/python-open-filepath-and-select.git">python-open-filepath-and-select</a> - For showing the indicated image file in explorer and selecting it

## Feature
* Theme of this application is dark-gray.
* ```ComicBookViewerWidget``` has most features of ```ViewerWidget```.
* Open the directory which current file belongs to
* Invert the color to prevent the eye strain
* Add certain image to bookmark list, but it won't save so if you restart the software the image you saved as a bookmark will be not there. I will add bookmark save feature using ```QSettings```.

## Note
I still test open compressed file feature so it won't work. Open normal file, directory is working and so far i don't find any problems at those two. There's a couple of other things that won't work properly like recent feature and setting background color. This is very first version of application and i will improve it. Sorry for premature upload.

## Example
Code Sample
```python
from pyqt_comic_viewer.comicBookViewerApp import ComicBookViewerApp

if __name__ == "__main__":
    import sys

    app = ComicBookViewerApp(sys.argv)
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/152635333-a47fd3ad-b424-43b7-96d8-7fd1799437f3.mp4

The comic pages being used for example are from Dragonball Multiverse.

