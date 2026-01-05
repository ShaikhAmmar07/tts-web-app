#!/bin/bash
wget -O piper.tar.gz https://github.com/rhasspy/piper/releases/download/v1.2.0/piper_amd64.tar.gz
tar -xzf piper.tar.gz
chmod +x piper/piper
mv piper/piper /usr/local/bin/ || mv piper/piper ./piper_bin
rm -rf piper piper.tar.gz
