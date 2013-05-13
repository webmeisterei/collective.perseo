from zope.interface import Interface
from zope import schema
from collective.perseo import perseoMessageFactory as _


class ISEOContextMetaSchema(Interface):

    title = schema.TextLine(
        title=_("label_title",
                default=u"Title Tag"),
        description=_("help_title",
                      default=(u"Text to be present in TITLE tag. It is "
                          "displayed in browser title bar. Search engines "
                          "display it as a title of the document.")),
        required=False)

    title_override = schema.Bool(
        title=_("label_title_override",
                default=u"Override the default"),
        required=False)

    description = schema.Text(
        title=_("label_description",
                default=u"Meta Description Tag"),
        description=_("help_description",
                      default=(u"Description of the document to be indexed by "
                          "Search Engines. This text will be present in meta "
                          "description tag in page HTML source.")),
        required=False)

    description_override = schema.Bool(
        title=_("label_title_override",
                default=u"Override the default"),
        required=False)

    keywords = schema.List(
        title=_("label_keywords",
                default=u"Meta Keywords Tag"),
        description=_("help_keywords",
                      default=(u"Keywords, the page will be indexed with. "
                          "Enter each keyword in separate line, please. "
                          "Though the relevance of listing meta keywords is "
                          "of questionable value now, it is useful to set "
                          "meta keywords for pages - for future reference.")),
        value_type=schema.TextLine(),
        required=False)

    keywords_override = schema.Bool(
        title=_("label_title_override",
                default=u"Override the default"),
        required=False)


class ISEOContextAdvancedSchema(Interface):

    meta_robots_follow = schema.Choice(
        title=_("label_meta_robots_follow",
                default=u"Meta Robots Follow Tag"),
        values=['follow', 'nofollow'],
        required=False)

    meta_robots_follow_override = schema.Bool(
        title=_("label_title_override",
                default=u"Override the default"),
        required=False)

    meta_robots_index = schema.Choice(
        title=_("label_meta_robots_index",
                default=u"Meta Robots Index Tag"),
        values=['index', 'noindex'],
        required=False)

    meta_robots_index_override = schema.Bool(
        title=_("label_title_override",
                default=u"Override the default"),
        required=False)

    meta_robots_advanced = schema.Choice(
        title=_("label_meta_robots_advanced",
                default=u"Meta Robots Advanced Tag"),
        values=['noodp', 'noydir', 'noarchive', 'nosnippet'],
        required=False)

    meta_robots_advanced_override = schema.Bool(
        title=_("label_title_override",
                default=u"Override the default"),
        required=False)

    canonical = schema.TextLine(
        title=_("label_canonical",
                default=u"Canonical URL"),
        description=_("help_canonical",
                      default=(u"Specify your canonical URL. If your site has "
                          "identical or vastly similar content that's "
                          "accessible through multiple URLs, this format "
                          "provides you with more control over the URL "
                          "returned in search results.")),
        required=False)

    canonical_override = schema.Bool(
        title=_("label_title_override",
                default=u"Override the default"),
        required=False)

    include_in_sitemap = schema.Choice(
        title=_("label_include_in_sitemap",
                default=u"Include in sitemap.xml.gz"),
        values=['yes', 'no'],
        required=False)

    include_in_sitemap_override = schema.Bool(
        title=_("label_title_override",
                default=u"Override the default"),
        required=False)

    sitemap_priority = schema.TextLine(
        title=_("label_sitemap_priority",
                default=u"Sitemap.xml.gz priority"),
        description=_("help_sitemap_priority",
                      default=u"Values from 0.1 to 1.0"),
        required=False)
