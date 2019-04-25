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
        Comment:                   "italic",
        Comment.Preproc:           "noitalic",

        Keyword:                   "bold",
        # Keyword.Pseudo:            "nobold",
        # Keyword.Type:              "nobold",

        Operator.Word:             "bold",

        Name.Class:                "bold",
        Name.Namespace:            "bold",
        Name.Exception:            "bold",
        Name.Entity:               "bold",
        Name.Tag:                  "bold",

        String:                    "#000", #italic
        String.Interpol:           "bold",
        String.Escape:             "bold",

        Generic.Heading:           "bold",
        Generic.Subheading:        "bold",
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold",

        Error:                     "border:#FF0000"
    }
