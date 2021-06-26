
from autoscaling.groups import AutoScalingGroup
from autoscaling.CapacityScalingInstructions import CapacityScalingInstructions
from autoscaling.functions import set_autoscaling_desired_distributions_capacity


# set_autoscaling_desired_distributions_capacity(
#     CapacityScalingInstructions(
#         AutoScalingGroup.get_auto_scaling_group_codename(
#             AutoScalingGroup.RATE_LIMITER
#         ),
#         2
#     )
# )
