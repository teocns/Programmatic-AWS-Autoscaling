
from autoscaling.groups import AutoScalingGroup
from autoscaling.CapacityScalingInstructions import CapacityScalingInstructions
from autoscaling.functions import set_capacity


set_capacity(
    CapacityScalingInstructions(
        AutoScalingGroup.get_auto_scaling_group_name(
            AutoScalingGroup.RATE_LIMITER
        ),
        1
    )
)
