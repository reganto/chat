from tornado import web, websocket, ioloop


class TickerConnection(websocket.WebSocketHandler):
    def on_open(self):
        self.timeout = ioloop.PeriodicCallback(self._ticker, 1000)
        self.timeout.start()

    def on_close(self):
        self.timeout.stop()

    def _ticker(self):
        self.send('tick!')


class HomeHandler(web.RequestHandler):
    def get(self):
        self.render('index.html')



if __name__ == "__main__":
    app = web.Application(
        [('/', HomeHandler), ('/w', TickerConnection)],
        debug=True
    )
    app.listen(8001)
    ioloop.IOLoop.current().start()
