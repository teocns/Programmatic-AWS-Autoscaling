class CapacityScalingInstructions:

    autoscaling_group: str

    # Amount of instances
    capacity: int

    def __init__(self, autoscaling_group, capcity) -> None:
        self.autoscaling_group = autoscaling_group
        self.capacity = capcity




