# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from exchange.themes.models import Theme


class Command(BaseCommand):
    help = 'List available themes by name and id'

    def handle(self, *args, **options):
        themes = all_entries = Theme.objects.all()
        self.stdout.write("Available Themes:")

        for theme in themes:
            self.stdout.write("- %s [%s]" % (theme.name, theme.id))
