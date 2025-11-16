"""
Compatibility shim for pyrogram types.

Maps common keyboard-related classes from pyrogram.types onto the top-level
pyrogram module so libs that do `from pyrogram import ReplyKeyboardMarkup`
(or InlineKeyboardMarkup) won't fail.

Place this file at: PyroUbot/core/helpers/pyrogram_compat.py
"""
from __future__ import annotations

import importlib
import warnings
from typing import Dict

def _apply_mappings() -> None:
    try:
        pyrogram = importlib.import_module("pyrogram")
    except Exception:
        return

    _types = None
    try:
        _types = importlib.import_module("pyrogram.types")
    except Exception:
        _types = None

    if _types is None:
        return

    mappings: Dict[str, str] = {
        # Inline keyboards
        "InlineKeyboardMarkup": "InlineKeyboardMarkup",
        "InlineKeyboardButton": "InlineKeyboardButton",
        "InlineKeyboard": "InlineKeyboardMarkup",  # alias some libs expect

        # Reply keyboards
        "ReplyKeyboardMarkup": "ReplyKeyboardMarkup",
        "ReplyKeyboardButton": "ReplyKeyboardButton",
        "KeyboardButton": "KeyboardButton",
        "KeyboardButtonRow": "KeyboardButtonRow",

        # Other common names
        "ForceReply": "ForceReply",
        "ReplyKeyboardRemove": "ReplyKeyboardRemove",
    }

    for top_name, type_name in mappings.items():
        try:
            if not hasattr(pyrogram, top_name):
                attr = getattr(_types, type_name, None)
                if attr is not None:
                    setattr(pyrogram, top_name, attr)
        except Exception as exc:
            warnings.warn(f"pyrogram_compat: failed to map {top_name}: {exc}")

# apply immediately
_apply_mappings()
