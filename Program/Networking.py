import PyQt6
from PyQt6.QtCore import QEventLoop, QObject, QMetaObject, Q_ARG, QUrl, QFile
from PyQt6.QtGui import QImage, QImageReader
from PyQt6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PyQt6.QtPdf import QPdfDocument


class Networking:
    class NetworkingPrivate(QObject):
        def httpGetImage(self, src):
            request = QNetworkRequest()
            request.setUrl(src)
            reply = self.nam.get(request)
            self.loop.exec()
            img = QImage()
            
            reader = QImageReader(reply)
            if reply.error() == QNetworkReply.NetworkError.NoError:
                 reader.read(img)
            else:
                 print('[NetworkingPrivate] Reply error')
            reply.deleteLater()
            return img

        def httpGetPdf(self, src, parent):
            request = QNetworkRequest()
            request.setUrl(src)
            reply = self.nam.get(request)
            while not reply.isFinished():
                self.loop.exec()

            doc = QPdfDocument(parent)
            file = QFile('./pdfCache.pdf')
            file.open(QFile.OpenModeFlag.WriteOnly)
            if file.isOpen():
                file.write(reply.readAll())
                file.close()
            else:
                print('File error')
            if reply.error() == QNetworkReply.NetworkError.NoError:
                doc.load('./pdfCache.pdf')

            else:
                print('[NetworkingPrivate] Reply error')
            reply.deleteLater()
            return doc



        def __init__(self):
            super().__init__()
            self.requests = dict()
            self.nam = QNetworkAccessManager()
            self.loop = QEventLoop()
            self.nam.finished.connect(self.loop.quit)

        #def __del__(self):
        #    self.loop.deleteLater()
        #    self.nam.deleteLater()


    def httpGetImage(self, url) -> QImage:
        return self.manager.httpGetImage(url)

    def httpGetImageAsync(self, url, receiver, slot):
        return self.manager.httpGetImageAsync(url, receiver, slot)

    def httpGetPdf(self, url, parent):
        return self.manager.httpGetPdf(url, parent)

    def __init__(self):
        self.manager = self.NetworkingPrivate()



NETWORK_MANAGER = Networking()