from __future__ import absolute_import, unicode_literals

from celery import shared_task

from games.scrapers import volume_scraper


@shared_task
def scrape_volume():
    volume_scraper.scrape()
    return

