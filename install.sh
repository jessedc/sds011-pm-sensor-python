#!/bin/bash

if [ ! -f .env.installed ]; then
    cp .env.example .env.installed
fi

cp ./lib/systemd/system/sds011-python.service /lib/systemd/system/
chmod 644 /lib/systemd/system/sds011-python.service

systemctl disable sds011-python.service

systemctl daemon-reload
systemctl enable sds011-python.service
systemctl start sds011-python.service
