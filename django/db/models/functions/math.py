from django.db.models import Transform


class Abs(Transform):
    function = 'ABS'
    lookup_name = 'abs'


class Round(Transform):
    function = 'ROUND'
    lookup_name = 'round'

