#!/bin/sh
TMP=/tmp/jsay.wav
echo "$1" | open_jtalk \
-m /usr/local/Cellar/open-jtalk/1.10_1/voice/mei/mei_normal.htsvoice \
-x /usr/local/Cellar/open-jtalk/1.10_1/dic \
-ow $TMP && \
afplay $TMP
rm -f $TMP