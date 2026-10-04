"""本地开发服务器：带 no-cache 头，改完代码刷新即生效。用法：python serve.py [端口]"""
import http.server
import socketserver

PORT = 8765


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass  # 别刷屏


if __name__ == "__main__":
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"serving http://127.0.0.1:{PORT}/")
        httpd.serve_forever()
