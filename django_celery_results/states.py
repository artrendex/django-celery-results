# -*- coding: utf-8 -*-

from celery.states import *
from celery.states import REJECTED

PUBLISHED = 'PUBLISHED'

UNREADY_STATES = frozenset({PENDING, PUBLISHED, RECEIVED, STARTED, REJECTED, RETRY})

ALL_STATES = frozenset({
    PENDING, PUBLISHED, RECEIVED, STARTED, SUCCESS, FAILURE, RETRY, REVOKED,
})

