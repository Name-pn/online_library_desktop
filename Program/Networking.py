import PyQt5
from PyQt5.QtCore import QEventLoop, QObject, QMetaObject, Q_ARG, QUrl
from PyQt5.QtGui import QImage, QImageReader
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply

class Networking:
    class NetworkingPrivate(QObject):
        def httpGetImage(self, src):
            request = QNetworkRequest()
            request.setUrl(src)
            reply = self.nam.get(request)
            self.loop.exec()
            img = QImage()
            
            reader = QImageReader(reply)
            if reply.error() == QNetworkReply.NoError:
                 reader.read(img)
            else:
                 print('[NetworkingPrivate] Reply error')
            reply.deleteLater()
            return img

        def httpGetImageAsync(self, src, receiver, slot):
            request = QNetworkRequest()
            request.setUrl(src)
            obj = (receiver, (src, slot))
            reply = self.nam.get(request)
            self.requests[reply] = obj

        def onFinished(self, reply):
            if reply in self.requests:
                obj = self.requests[reply]
                redirectedUrl = reply.attribute(QNetworkRequest.RedirectionTargetAttribute)
                redirectedTo = redirectedUrl.toUrl()
                if redirectedTo.isValid():
                    if redirectedTo != reply.url():
                        self.httpGetImageAsync(redirectedTo, obj[0], obj[1][1])
                    else:
                        print('[NetworkingPrivate] Infinite redirect loop at ' + str(redirectedTo))
                else:
                    img = QImage()
                    reader = QImageReader()
                    if reply.error() == QNetworkReply.NoError:
                        reader.read(img)
                    else:
                        print('[NetworkingPrivate] Reply error')
                    if obj[0] and obj[1][1]:
                        QMetaObject.invokeMethod(obj[0], obj[1][1], PyQt5.QtCore.Qt.DirectConnection, Q_ARG(QUrl, obj[1][0]), Q_ARG(QImage, img))

        def __init__(self):
            super().__init__()
            self.requests = dict()
            self.nam = QNetworkAccessManager()
            self.loop = QEventLoop()
            self.nam.finished.connect(self.onFinished)
            self.nam.finished.connect(self.loop.quit)

        #def __del__(self):
        #    self.loop.deleteLater()
        #    self.nam.deleteLater()


    def httpGetImage(self, url) -> QImage:
        return self.manager.httpGetImage(url)

    def httpGetImageAsync(self, url, receiver, slot):
        return self.manager.httpGetImageAsync(url, receiver, slot)

    def __init__(self):
        self.manager = self.NetworkingPrivate()


NETWORK_MANAGER = Networking()