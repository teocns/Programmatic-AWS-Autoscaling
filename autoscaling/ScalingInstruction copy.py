class ScalingInstruction:
    autoscaling_group: str
    instances_count: int



    def __init__(self, autoscaling_group, instances_count) -> None:
        self.autoscaling_group = autoscaling_group
        self.instances_count = instances_count