from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404


class CustomPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except (EmptyPage, PageNotAnInteger) as e:
            raise Http404 from e
