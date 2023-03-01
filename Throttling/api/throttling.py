from rest_framework.throttling import UserRateThrottle


class CustomThrottleRate(UserRateThrottle):
    scope = 'Custom_Throttle_rate'
