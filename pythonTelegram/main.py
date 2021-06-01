from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

class VideoPlayer(QWidget):
    def __init__(self, parent=None):
        super(VideoPlayer, self).__init__(parent)
        videoItem = QGraphicsVideoItem()
        videoItem.setSize(QSizeF(640, 480))
        scene = QGraphicsScene(self)
        scene.addItem(videoItem)
        graphicsView = QGraphicsView(scene)
        layout = QVBoxLayout()
        layout.addWidget(graphicsView)
        self.setLayout(layout)
        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.mediaPlayer.setVideoOutput(videoItem)

    def keyPressEvent(self, e):
        print('state: ' + str(self.mediaPlayer.state()))
        print('mediaStatus: ' + str(self.mediaPlayer.mediaStatus()))
        print('error: ' + str(self.mediaPlayer.error()))
        if e.key() == Qt.Key_L:
            print('loading')
            self.load()
        if e.key() == Qt.Key_P:
            print('playing')
            self.mediaPlayer.play()

    def load(self):
        local = QUrl.fromLocalFile('C:\\Users\\tank.sui\\Videos\\Wildlife.wmv')
        media = QMediaContent(local)
        self.mediaPlayer.setMedia(media)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())

After Review your code， just list the root cause below.QUrl.fromLocalFile

local = QUrl.fromLocalFile('')
