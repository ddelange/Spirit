import os

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError

from ... import utils
from ...conf import settings


class Command(BaseCommand):
    help = (
        "Creates or updates .po files. Run "
        "`python manage.py spiritmakemessages > out` to read "
        "the output later (look for warnings)"
    )

    requires_system_checks = []

    def add_arguments(self, parser):
        parser.add_argument(
            "--locale",
            "-l",
            default=[],
            action="append",
            help="Creates or updates the message files for the given locale(s) (e.g. pt_BR). "
            "Can be used multiple times.",
        )

    def handle(self, *args, **options):
        if not settings.ST_BASE_DIR.endswith("spirit"):
            raise CommandError(
                "settings.ST_BASE_DIR is not the spirit root folder, are you overriding it?"
            )

        for root, dirs, files in os.walk(settings.ST_BASE_DIR):
            if "locale" not in dirs:
                continue

            with utils.pushd(root):
                call_command(
                    "makemessages", stdout=self.stdout, stderr=self.stderr, **options
                )

        self.stdout.write("ok")
