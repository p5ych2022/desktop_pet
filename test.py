#!/usr/bin/env python
# -*- coding:utf-8 -*-
# auther:psych
# time:2025/1/18

from PyQt5.QtWidgets import QApplication, QLabel
import sys
import os

QT_PLUGIN_PATH_VALUE = r".\venv\Lib\site-packages\PyQt5\Qt5\plugins"

# 设置环境变量
os.environ["QT_PLUGIN_PATH"] = QT_PLUGIN_PATH_VALUE

app = QApplication(sys.argv)
label = QLabel("Hello, PyQt!")
label.show()
sys.exit(app.exec_())
