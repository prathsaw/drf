from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


# PageNumberPagination
class MyPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'records'   # user can set how many numbers of records he wants to fetch per page
    max_page_size = 3                   # user cannot set number of records per page more than max_page_size value

# ======================================================================================================================


# LimitOffsetPagination
class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset'
    max_limit = 3
