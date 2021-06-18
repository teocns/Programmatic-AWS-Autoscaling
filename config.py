DOMAIN_RATE_LIMIT = 5
CAPACITY_PER_DISTRIBUTION = 200


AUTO_SCALING_GROUPS = {
    'SCRAPER': {
        'codename': "",
        # 'instance_creation_paramters': {
        #     'InstanceType': 'c5.large',
        #     'SecurityGroupIds': ['sg-05dec40ce8b91a8c8'],
        #     'InstanceMarketOptions': {
        #         'MarketType': 'spot',
        #         'SpotOptions': {
        #             'MaxPrice': 'string',
        #             'SpotInstanceType': 'one-time' | 'persistent',
        #             'InstanceInterruptionBehavior': 'hibernate' | 'stop' | 'terminate'
        #         }
        #     },
        # }


    },
    'SPIDER': {
        'codename': ''
    },
    'RATE_LIMITER': {
        'codename': 'awseb-e-dnpwccp42g-stack-AWSEBAutoScalingGroup-YP7HYN21XF1D'
    }
}


ENABLE_DEBUG_OUTPUT = True
# If set to True, will not forward requests, instead it will hang for 3 seconds on the request. Intended to test the rate limiter
ENABLE_DEBUG_NOFORWARD = True


############################
# REDIS CONFIGURATION
# Replace with your own credentials
############################


redis_endpoint = "redis://redis-endpoint.com"

redis_pass = "USER"
redis_user = "PASS"


aws_access_key_id = 'AKIAQLRVICZQD6ZSXUW7'
aws_secret_access_key = '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'
