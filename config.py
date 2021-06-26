
CAPACITY_PER_DISTRIBUTION = 200


AUTO_SCALING_GROUPS = {
    'SCRAPER': {
        'codename': "awseb-e-mtrrs34pb4-stack-AWSEBAutoScalingGroup-CRXTMF7SZFPD",
    },
    "SPIDER": {
        'codename': "awseb-e-iytce6es6v-stack-AWSEBAutoScalingGroup-BAURTOTXER0A"
    },
    
    'PROCESSOR': {
        'codename': 'awseb-e-bgv57pjazv-stack-AWSEBAutoScalingGroup-1J1B4S5WF92O8'
    }
}


ENABLE_DEBUG_OUTPUT = True
# If set to True, will not forward requests, instead it will hang for 3 seconds on the request. Intended to test the rate limiter
ENABLE_DEBUG_NOFORWARD = True


############################
# REDIS CONFIGURATION
# Replace with your own credentials
############################


redis_endpoint = "redis://crawler-threads-processing.gslcnb.0001.euw3.cache.amazonaws.com"

redis_pass = "USER"
redis_user = "PASS"


aws_access_key_id = 'AKIAQLRVICZQD6ZSXUW7'
aws_secret_access_key = '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'
