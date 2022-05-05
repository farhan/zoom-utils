DATE_TIME_FORMAT = '%Y-%m-%dT%H:%M:%SZ'
DATE_TIME_DIFFERENCE_HOURS = 7
MIN_MINUTES_FOR_ATTENDANCE = 1

class ZoomAPIEndpoint(object):
    """Zoom API Endpoints"""

    GET_ACTIVE_USER_LIST = '/users'
    GET_USER_SETTINGS = '/users/{user_id}/settings'
    GET_MEETING = '/meetings/{meeting_id}'
    MEETING_PARTICIPANT_REPORT = '/report/meetings/{meeting_id}/participants'
    WEBINAR_PARTICIPANT_REPORT = '/report/webinars/{webinar_id}/participants'
    GET_MEETINGS_INSTANCES = '/past_meetings/{meeting_id}/instances'
    GET_WEBINAR_INSTANCES = '/past_webinars/{webinar_id}/instances'