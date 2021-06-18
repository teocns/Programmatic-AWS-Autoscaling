from enum import Enum
from config import AUTO_SCALING_GROUPS


class AutoScalingGroup:
    SCRAPER = 'SCRAPER'
    SPIDER = 'SPIDER'
    RATE_LIMITER = 'RATE_LIMITER'
    PROCESSING = 'PROCESSING'

    def get_auto_scaling_group_name(auto_scaling_group: 'AutoScalingGroup'):

        return AUTO_SCALING_GROUPS[auto_scaling_group]['codename']
        pass
