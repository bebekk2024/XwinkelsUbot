# Ensure pyrogram exposes top-level InlineKeyboard types for packages that expect them
# (e.g. pykeyboard which does `from pyrogram import InlineKeyboardMarkup`).
# Import this module before any package that imports pykeyboard/pyrogram internals.

try:
    import pyrogram
    from pyrogram import types as _types

    # Map types into top-level pyrogram module if missing
    if not hasattr(pyrogram, "InlineKeyboardMarkup") and hasattr(_types, "InlineKeyboardMarkup"):
        pyrogram.InlineKeyboardMarkup = _types.InlineKeyboardMarkup

    if not hasattr(pyrogram, "InlineKeyboardButton") and hasattr(_types, "InlineKeyboardButton"):
        pyrogram.InlineKeyboardButton = _types.InlineKeyboardButton

    # Add other mappings here if you encounter additional missing names
except Exception:
    # Don't raise here to avoid masking the actual startup error later;
    # keep silent so startup can continue (and fail elsewhere if necessary).
    pass
