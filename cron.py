import os
import sys
sys.path.append('/home/weetao/webenv/cntest')
os.environ["DJANGO_SETTINGS_MODULE"] = 'cntest.settings'

from NCRE.models import QueryCount
from django.core.cache import cache

q_counts = QueryCount.objects.all()[0]
if cache.get('query_count'):
    q_counts.q_count = cache.get('query_count')
    q_counts.save()