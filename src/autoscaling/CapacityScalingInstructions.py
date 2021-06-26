class CapacityScalingInstructions:

    autoscaling_group_aws_codename: str

    # Amount of instances
    distributions: int

    def __init__(self, autoscaling_group_aws_codename, distributions) -> None:
        self.autoscaling_group_aws_codename = autoscaling_group_aws_codename
        self.distributions = distributions
