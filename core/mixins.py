from django.conf import settings

from core.constants import DEFAULT_PAGINATED_BY, DEFAULT_GET_ELIDED_PAGE_RANGE_ON_EACH_SIDE, \
    DEFAULT_GET_ELIDED_PAGE_RANGE_ON_ENDS


def get_paginated_context(context, request, queryset, paginator_class, paginate_by=None, on_each_side=None,
                          on_ends=None):
    try:
        if not paginate_by:
            paginate_by = int(settings.PAGINATION_CONFIGURATIONS.get(
                'PAGINATE_BY', DEFAULT_PAGINATED_BY)
            )
        if not on_each_side:
            on_each_side = int(settings.PAGINATION_CONFIGURATIONS.get(
                'GET_ELIDED_PAGE_RANGE_ON_EACH_SIDE', DEFAULT_GET_ELIDED_PAGE_RANGE_ON_EACH_SIDE)
            )
        if not on_ends:
            on_ends = int(settings.PAGINATION_CONFIGURATIONS.get(
                'GET_ELIDED_PAGE_RANGE_ON_ENDS', DEFAULT_GET_ELIDED_PAGE_RANGE_ON_ENDS)
            )
    except AttributeError:  # pragma: no cover
        paginate_by = DEFAULT_PAGINATED_BY
        on_each_side = DEFAULT_GET_ELIDED_PAGE_RANGE_ON_EACH_SIDE
        on_ends = DEFAULT_GET_ELIDED_PAGE_RANGE_ON_ENDS

    page = request.GET.get('page', 1)
    paginator = paginator_class(queryset, paginate_by)

    objects = paginator.page(page)
    objects.adjusted_elided_pages = paginator.get_elided_page_range(
        page,
        on_each_side=on_each_side,
        on_ends=on_ends
    )
    context['page_obj'] = objects
    context['current_page_number'] = int(page)

    return context


class PaginationMixin:
    def get_paginate_by(self, queryset):
        paginate_by = self.paginate_by
        try:
            if not paginate_by:
                paginate_by = int(settings.PAGINATION_CONFIGURATIONS.get('PAGINATE_BY', DEFAULT_PAGINATED_BY))
        except AttributeError:
            paginate_by = DEFAULT_PAGINATED_BY

        return paginate_by

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = get_paginated_context(
            context=context,
            request=self.request,
            queryset=self.get_queryset(),
            paginator_class=self.paginator_class,
            paginate_by=self.paginate_by,
        )
        return context
