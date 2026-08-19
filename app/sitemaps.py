from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "weekly"

    def items(self):
        return [
            'home',
            'about',
            'contact',
            'internship_minor',
            'internship_major',
            'why_us',
            'apply_internship'
        ]

    def location(self, item):
        return reverse(item)