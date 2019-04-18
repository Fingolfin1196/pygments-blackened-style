# -*- coding: utf-8 -*-
"""
    pygments.styles.blackened
    ~~~~~~~~~~~~~~~~~~~~~

    Based on bw but a bit more varied.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


class BlackenedStyle(Style):
    """
    Based on bw but a bit more varied. Good for use in LaTeX code.
    """

    background_color = "#ffffff"
    default_style = ""

    styles = {
        Whitespace:                 '#fff',  # bbbbbb

        Comment:                    'italic',
        Comment.Preproc:            'bold italic',
        # Comment.Special:            'italic #0000aa',

        Keyword:                    'bold',  # 0000aa
        # Keyword.Type:               '#00aaaa',

        Operator.Word:              '#0000aa',

        Name.Builtin:               'bold',
        # Name.Function:              '#00aa00',
        Name.Class:                 'underline #00aa00',
        # Name.Namespace:             'underline #00aaaa',
        # Name.Variable:              '#aa0000',
        Name.Constant:              '#aa0000',
        Name.Entity:                'bold #800',
        Name.Attribute:             '#1e90ff',
        Name.Tag:                   'bold #1e90ff',
        Name.Decorator:             '#888888',

        String:                     '#000',  # aa5500
        # String.Symbol:              '#0000aa',
        # String.Regex:               '#009999',

        Number:                     '#000',  # 009999

        Generic.Heading:            'bold',  # 000080
        Generic.Subheading:         'bold',  # 800080
        Generic.Deleted:            '#aa0000',
        Generic.Inserted:           '#00aa00',
        Generic.Error:              '#aa0000',
        Generic.Emph:               'italic',
        Generic.Strong:             'bold',
        Generic.Prompt:             '#555555',
        Generic.Output:             '#888888',
        Generic.Traceback:          '#aa0000',

        # Error:                      '#F00 bg:#FAA'
    }
