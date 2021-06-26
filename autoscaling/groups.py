from enum import Enum
from config import AUTO_SCALING_GROUPS


class AutoScalingGroup:
    SCRAPER = 'SCRAPER'
    SPIDER = 'SPIDER'
    PROCESSOR = 'PROCESSOR'

    def get_auto_scaling_group_codename(auto_scaling_group: 'AutoScalingGroup'):
        return AUTO_SCALING_GROUPS[auto_scaling_group]['codename']

    def get_by_auto_scaling_group_codename(codename):
        for name in AUTO_SCALING_GROUPS:
            if AUTO_SCALING_GROUPS[name]['codename'] == codename:
                return name
