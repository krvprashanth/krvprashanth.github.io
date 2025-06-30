# -*- coding: utf-8 -*-

import time

# Data about this site
BLOG_AUTHOR = "krvprashanth"  # (translatable)
BLOG_TITLE = "krvprashanth"  # (translatable)
# This is the main URL for your site. It will be used
# in a prominent link. Don't forget the protocol (http/https)!
SITE_URL = "https://krvprashanth.in/"
# This is the URL where Nikola's output will be deployed.
# If not set, defaults to SITE_URL
# BASE_URL = "https://krvprashanth.in/"
BLOG_CONTACT_PAGE = "/contact"
BLOG_EMAIL = "krvprashanth@gmail.com"
BLOG_DESCRIPTION = "Bytes Beyond Bandwidth"  # (translatable)
DEFAULT_LANG = "en"

TRANSLATIONS = {
    DEFAULT_LANG: "",
    # Example for another language:
    # "es": "./es",
}

TRANSLATIONS_PATTERN = '{path}.{lang}.{ext}'


NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/", "blog"),
        ("/pages/about/", "about"),
#        ("/archive/", "archive"),
        ("/rss.xml", "feed"), # TODO: Put this in the bottom, somehwere? As a clickable icon?
    ),
}

NAVIGATION_ALT_LINKS = {
    DEFAULT_LANG: ()
}

# Name of the theme to use.
THEME = "willy-wonky"
USE_CDN = False
USE_BUNDLES = False

FAVICONS = (
    ("icon", "/favicon.ico", "32x32"),
)


POSTS = (
#    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.md", "posts", "post.tmpl"),
    ("posts/*.txt", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
)
PAGES = (
#    ("pages/*.rst", "pages", "page.tmpl"),
    ("pages/*.md", "pages", "page.tmpl"),
    ("pages/*.txt", "pages", "page.tmpl"),
    ("pages/*.html", "pages", "page.tmpl"),
)


TIMEZONE = "Asia/Kolkata"

DATE_FORMAT = 'dd-MMM-yyyy'

COMPILERS = {
    "rest": ['.rst', '.txt'],
    "markdown": ['.md', '.mdown', '.markdown'],
    "textile": ['.textile'],
    "txt2tags": ['.t2t'],
    "bbcode": ['.bb'],
    "wiki": ['.wiki'],
    "ipynb": ['.ipynb'],
    "html": ['.html', '.htm'],
    # PHP files are rendered the usual way (i.e. with the full templates).
    # The resulting files have .php extensions, making it possible to run
    # them without reconfiguring your server to recognize them.
    "php": ['.php'],
    # Pandoc detects the input from the source filename
    # but is disabled by default as it would conflict
    # with many of the others.
    # "pandoc": ['.rst', '.md', '.txt'],
}

CATEGORY_ALLOW_HIERARCHIES = False
CATEGORY_OUTPUT_FLAT_HIERARCHY = False


HIDDEN_AUTHORS = ['Guest']
FRONT_INDEX_HEADER = {
    DEFAULT_LANG: ''
}

#ARCHIVE_PATH = "archive/"
#ARCHIVE_FILENAME = "index.html"
#ARCHIVES_ARE_INDEXES = False

ATOM_FILENAME_BASE = "feed"

REDIRECTIONS = []

# Presets of commands to execute to deploy. Can be anything, for
# example, you may use rsync:
# "rsync -rav --delete --delete-after output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola plugin -i ping`).  Or run `nikola check -l`.
# You may also want to use github_deploy (see below).
# You can define multiple presets and specify them as arguments
# to `nikola deploy`.  If no arguments are specified, a preset
# named `default` will be executed.  You can use as many presets
# in a `nikola deploy` command as you like.
# DEPLOY_COMMANDS = {
#     'default': [
#         "rsync -rav --delete --delete-after output/ joe@my.site:/srv/www/site",
#     ]
# }

# github_deploy configuration
# For more details, read the manual:
# https://getnikola.com/handbook.html#deploying-to-github
# You will need to configure the deployment branch on GitHub.
GITHUB_SOURCE_BRANCH = 'src'
GITHUB_DEPLOY_BRANCH = 'master'

# The name of the remote where you wish to push to, using github_deploy.
GITHUB_REMOTE_NAME = 'origin'

# Whether or not github_deploy should commit to the source branch automatically
# before deploying.
GITHUB_COMMIT_SOURCE = True

# Where the output site should be located
OUTPUT_FOLDER = 'output'


# #############################################################################
# Image Gallery Options
# #############################################################################

GALLERIES_USE_THUMBNAIL = False
GALLERIES_DEFAULT_THUMBNAIL = None

IMAGE_FOLDERS = {'images': 'images'}

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Show teasers (instead of full posts) in indexes? 
INDEX_TEASERS = False

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the feeds, if FEED_TEASERS is True (translatable)
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

FEED_LINKS_APPEND_QUERY = False

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = """
<div class="license">
<a rel="license" href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
<img alt="Creative Commons License BY-NC-SA"
style="border-width:0; margin-bottom:12px;"
src="/images/cc-88x31.png"></a>
</div>
"""
# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = """
Contents by <a href="{contact}">{author}</a> - Powered by <a href="https://getnikola.com" rel="nofollow">Nikola</a><br>
This site uses willy-wonky theme by <a href="https://gitlab.com/ru2saig/willy-wonky" target="_blank" rel="noopener">ru2saig</a><br>
{license}
"""

# (translatable)
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "contact": BLOG_CONTACT_PAGE,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE
        }
    )
}

# A simple copyright tag for inclusion in RSS feeds that works just
# like CONTENT_FOOTER and CONTENT_FOOTER_FORMATS
RSS_COPYRIGHT = 'Contents by {author}</a> {license}'
RSS_COPYRIGHT_PLAIN = 'Contents by {author} {license}'
RSS_COPYRIGHT_FORMATS = CONTENT_FOOTER_FORMATS

# TODO: go with isso
# To use comments, you can choose between different third party comment
# systems.  The following comment systems are supported by Nikola:
#   disqus, facebook, intensedebate, isso, muut, commento, utterances
# You can leave this option blank to disable comments.
COMMENT_SYSTEM = ""
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = ""

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
STRIP_INDEXES = True

# Instead of putting files in <slug>.html, put them in <slug>/index.html.
# No web server configuration is required. Also enables STRIP_INDEXES.
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata.
PRETTY_URLS = True


# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# Defaults are markdown.extensions.(fenced_code|codehilite|extra)
# markdown.extensions.meta is required for Markdown metadata.
MARKDOWN_EXTENSIONS = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'markdown.extensions.extra']

# Modify the number of Post per Index Page
INDEX_DISPLAY_POST_COUNT = 20

# A search form to search this site, for the sidebar. You can use a Google
# custom search (https://www.google.com/cse/)
# Or a DuckDuckGo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# (translatable)
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
# SEARCH_FORM = """
# <!-- DuckDuckGo custom search -->
# <form method="get" id="search" action="https://duckduckgo.com/"
#  class="navbar-form pull-left">
# <input type="hidden" name="sites" value="%s">
# <input type="hidden" name="k8" value="#444444">
# <input type="hidden" name="k9" value="#D51920">
# <input type="hidden" name="kt" value="h">
# <input type="text" name="q" maxlength="255"
#  placeholder="Search&hellip;" class="span2" style="margin-top: 4px;">
# <input type="submit" value="DuckDuckGo Search" style="visibility: hidden;">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL
#
# If you prefer a Google search form, here's an example that should just work:
# SEARCH_FORM = """
# <!-- Google custom search -->
# <form method="get" action="https://www.google.com/search" class="navbar-form navbar-right" role="search">
# <div class="form-group">
# <input type="text" name="q" class="form-control" placeholder="Search">
# </div>
# <button type="submit" class="btn btn-primary">
# 	<span class="glyphicon glyphicon-search"></span>
# </button>
# <input type="hidden" name="sitesearch" value="%s">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL
# If set to True, the tags 'draft', 'mathjax' and 'private' have special
# meaning. If set to False, these tags are handled like regular tags.
USE_TAG_METADATA = False

# If set to True, a warning is issued if one of the 'draft', 'mathjax'
# and 'private' tags are found in a post. Useful for checking that
# migration was successful.
WARN_ABOUT_TAG_METADATA = False

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []

