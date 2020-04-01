from sentry_sdk import capture_message, configure_scope

from .constants import SentryLevel


def capture_sentry_message(tag, tag_value, message, level=None, extra=None):
    with configure_scope() as scope:
        scope.set_tag(tag, tag_value)
        scope.level = level or SentryLevel.ERROR

        if not extra:
            extra = {}

        for key, value in extra.items():
            scope.set_extra(key, value)

        capture_message(message=message)
