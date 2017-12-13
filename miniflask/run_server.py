#!/usr/bin/env python

from miniflask.application import APPLICATION


APPLICATION.run(host='0.0.0.0', port=5000, debug=True)
