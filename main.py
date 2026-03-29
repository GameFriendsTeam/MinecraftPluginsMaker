#!/usr/bin/env python3
"""
Minecraft Plugin Maker — MPM
Python-версия оригинального C# WPF проекта.
"""
import os
import sys

# Добавляем корень проекта в path
ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT)

from ui.main_window import MPMApp

if __name__ == "__main__":
    app = MPMApp()
    app.mainloop()
