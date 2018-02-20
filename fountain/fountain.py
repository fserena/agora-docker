import logging

from agora import Agora, setup_logging
from agora.server.fountain import build
import os

setup_logging(logging.DEBUG)

API_PORT = int(os.environ.get('API_PORT', 5000))

try:
	agora = Agora(persist_mode=True, base='knowledge', path='fountain', redis_file='fountain.db')

	server = build(agora.fountain)
	server.run(host='0.0.0.0', port=API_PORT, use_reloader=False, debug=False, threaded=True)
except (KeyboardInterrupt, Exception) as e:
	pass
finally:
	Agora.close()
