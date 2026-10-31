"""Sphinx documentation configuration.

This file defines the project metadata, documentation sources,
enabled extensions, Markdown processing, HTML output, theme
customization, navigation, and build behavior.
"""

from datetime import datetime


# Project metadata shown in page titles, generated notices, and theme
# navigation. Keep ``release`` synchronized with the package version.
project = "getwinbg"
author = "Virati Akiranandhan Reddy"
release = "0.1.0"
version = ".".join(release.split(".")[:2])
copyright = f"{datetime.now().year} {author}"


# Documentation source configuration. ``root_doc`` identifies the document
# that Sphinx uses as the entry point for the documentation tree. The suffix
# mapping allows the project to use both reStructuredText and Markdown files.
root_doc = "index"
language = "en"
today_fmt = "%B %d, %Y"
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# MyST adds Markdown support, while the remaining extensions provide copy
# buttons, reusable design components, and social-sharing metadata.
extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxext.opengraph",
]

# Use Python terminology and syntax highlighting by default for API and
# example content. ``needs_sphinx`` prevents builds with an older Sphinx
# version that may not support the configuration used by this project.
primary_domain = "py"
highlight_language = "python3"
needs_sphinx = "9.2"


# MyST Markdown features enabled for all Markdown documentation pages.
# Heading anchors make individual sections addressable through stable links.
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "substitution",
    "tasklist",
]
myst_heading_anchors = 3


# Files that are build artifacts, operating-system metadata, or otherwise
# not documentation sources. An empty templates path explicitly indicates
# that this project does not override the theme's template files.
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
]
templates_path = []


# HTML output and site metadata. ``html_baseurl`` is used when Sphinx creates
# canonical links and other URL-aware metadata. The meta description helps
# search engines and link previews describe the documentation site.
html_theme = "furo"
html_title = "getwinbg"
html_short_title = "getwinbg"
html_last_updated_fmt = "%b %d, %Y"
# The favicon and static directory are supplied by the documentation project.
html_favicon = "_static/favicon.ico"
html_static_path = ["_static"]
html_show_sphinx = False
html_show_copyright = True
# Avoid exposing source files through the generated site's "view source" links.
html_copy_source = False
# Retain Sphinx's domain and general indexes for navigable API references.
html_domain_indices = True
html_use_index = True
html_baseurl = "https://getwinbg.readthedocs.io/"
html_meta = {
    "description": (
        "Documentation for getwinbg, a Python package for retrieving "
        "Windows background image paths."
    ),
}


# Furo theme customization. Separate light and dark variables preserve
# readable contrast while keeping the project's cyan brand color consistent.
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#0891B2",
        "color-brand-content": "#0891B2",
    },
    "dark_css_variables": {
        "color-brand-primary": "#22D3EE",
        "color-brand-content": "#22D3EE",
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
}

# Sidebar templates are applied to every page. The navigation template
# renders the document tree, while the surrounding templates provide
# branding, search, scroll controls, and the theme variant selector.
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
        "sidebar/variant-selector.html",
    ],
}


# Code-block behavior. The prompt pattern covers Python, continuation,
# shell, and IPython prompts so copied examples contain executable content
# rather than interactive prompts.
copybutton_prompt_text = r">>> |\.\.\. |\$ |In \[\d*\]: "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = False
# Use distinct Pygments styles for light and dark theme variants.
pygments_style = "friendly"
pygments_dark_style = "monokai"


# Open Graph metadata controls how documentation links appear when shared on
# services that support social preview cards.
ogp_site_url = "https://getwinbg.readthedocs.io/"
ogp_site_name = "getwinbg"
ogp_description = (
    "Documentation for getwinbg, a Python package for retrieving "
    "Windows background image paths."
)
ogp_type = "website"


# Build quality and reproducibility controls. Strict reference checking makes
# unresolved links fail the build; warning settings preserve warning context
# for CI logs. TODO directives remain excluded from published documentation.
nitpicky = True
keep_warnings = True
show_warning_types = True
todo_include_todos = False
# Normalize doctest flags so examples behave consistently across builders.
trim_doctest_flags = True
