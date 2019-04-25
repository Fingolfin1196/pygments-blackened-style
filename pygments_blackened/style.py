# -*- coding: utf-8 -*-
"""
    pygments.styles.blackened
    ~~~~~~~~~~~~~~~~~~~~~

    Black-and-white style based on various built-in style, with most similarities to bw.
"""

from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Number, Operator, Generic, Whitespace, Punctuation, Other, Literal


class BlackenedStyle(Style):
    """
    Based on various built-in styles. Good for use in LaTeX code.
    """

    background_color = "#ffffff"
    default_style = ""

    styles = {
        Comment:                   "italic",
        Comment.Multiline:         "",
        Comment.Preproc:           "noitalic",
        Comment.Single:            "",
        Comment.Special:           "",

        Keyword:                   "bold",
        Keyword.Constant:          "",
        Keyword.Declaration:       "",
        Keyword.Namespace:         "",
        Keyword.Pseudo:            "", #nobold
        Keyword.Reserved:          "",
        Keyword.Type:              "", #nobold

        Operator:                  "bold",
        Operator.Word:             "",

        Name:                      "",
        Name.Attribute:            "",
        Name.Builtin:              "bold italic",
        Name.Builtin.Pseudo:       "",
        Name.Class:                "bold",
        Name.Constant:             "",
        Name.Decorator:            "",
        Name.Entity:               "bold",
        Name.Exception:            "bold",
        Name.Function:             "italic",
        Name.Property:             "",
        Name.Label:                "",
        Name.Namespace:            "bold italic",
        Name.Other:                "",
        Name.Tag:                  "bold",
        Name.Variable:             "",
        Name.Variable.Class:       "",
        Name.Variable.Global:      "",
        Name.Variable.Instance:    "",

        Number:                    "",
        Number.Float:              "",
        Number.Hex:                "",
        Number.Integer:            "",
        Number.Integer.Long:       "",
        Number.Oct:                "",

        String:                    "#000", #italic
        String.Backtick:           "",
        String.Char:               "",
        String.Doc:                "",
        String.Double:             "",
        String.Escape:             "bold",
        String.Heredoc:            "",
        String.Interpol:           "bold",
        String.Other:              "",
        String.Regex:              "",
        String.Single:             "",
        String.Symbol:             "",

        Generic:                   "",
        Generic.Deleted:           "",
        Generic.Emph:              "italic",
        Generic.Error:             "",
        Generic.Heading:           "bold",
        Generic.Inserted:          "",
        Generic.Output:            "",
        Generic.Prompt:            "bold",
        Generic.Strong:            "bold",
        Generic.Subheading:        "bold",
        Generic.Traceback:         "",

        Error:                     "border:#FF0000"
    }
