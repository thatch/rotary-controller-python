#!/bin/sh
export KCFG_KIVY_KEYBOARD_MODE="systemanddock"
export KCFG_KIVY_LOG_DIR="$PWD/log"

python ./rotary_controller_python/main.py
