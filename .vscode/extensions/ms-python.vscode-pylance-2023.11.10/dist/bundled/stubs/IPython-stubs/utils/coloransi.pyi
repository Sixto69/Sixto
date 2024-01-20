"""
This type stub file was generated by pyright.
"""

import os

"""Tools for coloring text in ANSI terminals.
"""
__all__ = ['TermColors', 'InputTermColors', 'ColorScheme', 'ColorSchemeTable']
color_templates = ...
def make_color_table(in_class): # -> None:
    """Build a set of color attributes in a class.

    Helper function for building the :class:`TermColors` and
    :class`InputTermColors`.
    """
    ...

class TermColors:
    """Color escape sequences.

    This class defines the escape sequences for all the standard (ANSI?)
    colors in terminals. Also defines a NoColor escape which is just the null
    string, suitable for defining 'dummy' color schemes in terminals which get
    confused by color escapes.

    This class should be used as a mixin for building color schemes."""
    NoColor = ...
    Normal = ...
    _base = ...


class InputTermColors:
    """Color escape sequences for input prompts.

    This class is similar to TermColors, but the escapes are wrapped in \\001
    and \\002 so that readline can properly know the length of each line and
    can wrap lines accordingly.  Use this class for any colored text which
    needs to be used in input prompts, such as in calls to raw_input().

    This class defines the escape sequences for all the standard (ANSI?)
    colors in terminals. Also defines a NoColor escape which is just the null
    string, suitable for defining 'dummy' color schemes in terminals which get
    confused by color escapes.

    This class should be used as a mixin for building color schemes."""
    NoColor = ...
    if os.name == 'nt' and os.environ.get('TERM', 'dumb') == 'emacs':
        Normal = ...
        _base = ...
    else:
        Normal = ...
        _base = ...


class NoColors:
    """This defines all the same names as the colour classes, but maps them to
    empty strings, so it can easily be substituted to turn off colours."""
    NoColor = ...
    Normal = ...


class ColorScheme:
    """Generic color scheme class. Just a name and a Struct."""
    def __init__(self, __scheme_name_, colordict=..., **colormap) -> None:
        ...
    
    def copy(self, name=...): # -> ColorScheme:
        """Return a full copy of the object, optionally renaming it."""
        ...
    


class ColorSchemeTable(dict):
    """General class to handle tables of color schemes.

    It's basically a dict of color schemes with a couple of shorthand
    attributes and some convenient methods.

    active_scheme_name -> obvious
    active_colors -> actual color table of the active scheme"""
    def __init__(self, scheme_list=..., default_scheme=...) -> None:
        """Create a table of color schemes.

        The table can be created empty and manually filled or it can be
        created with a list of valid color schemes AND the specification for
        the default active scheme.
        """
        ...
    
    def copy(self): # -> ColorSchemeTable:
        """Return full copy of object"""
        ...
    
    def add_scheme(self, new_scheme): # -> None:
        """Add a new color scheme to the table."""
        ...
    
    def set_active_scheme(self, scheme, case_sensitive=...): # -> None:
        """Set the currently active scheme.

        Names are by default compared in a case-insensitive way, but this can
        be changed by setting the parameter case_sensitive to true."""
        ...
    

