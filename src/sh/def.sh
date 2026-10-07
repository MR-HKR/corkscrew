#!/bin/bash

xdg-mime default "$1" application/x-msdownload
update-desktop-database ~/.local/share/applications