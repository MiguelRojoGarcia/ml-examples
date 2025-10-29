import pytest
from datetime import datetime, timezone, timedelta
from core.domain.common.value_objects.timestamp import TimeStamp

def test_now_returns_utc_datetime():
    metric_date = TimeStamp.now()
    assert isinstance(metric_date.value, datetime)
    assert metric_date.value.tzinfo == timezone.utc