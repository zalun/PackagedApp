import SimpleHTTPServer
import SocketServer
from marionette import Marionette

m = Marionette('localhost', 2828)
m.start_session()
script = """
var request = navigator.mozApps.install('http://localhost:3000/package.manifest');
request.onsuccess = function () {
  marionetteScriptFinished('YAY');
};
request.onerror = function(e) {
marionetteScriptFinished('Boooo :( ' + this.error.name);
};"""
print m.execute_async_script(script)
# Out[69]: u'Boooo :( INVALID_MANIFEST'
