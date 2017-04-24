from rest_framework.pagination import CursorPagination
from rest_framework.settings import api_settings

__all__ = (
    'CustomPagination',
)


class CustomPagination(CursorPagination):
    cursor_query_param = 'cursor'
    page_size = api_settings.PAGE_SIZE
    template = 'rest_framework/pagination/previous_and_next.html'
    offset_cutoff = 1000


