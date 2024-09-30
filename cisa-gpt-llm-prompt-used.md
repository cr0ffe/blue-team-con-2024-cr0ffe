
```
{
    "IOC_Categories": [
        {
            "category": "File Indicators",
            "indicators": [
                {
                    "name": "<file name>",
                    "hashes": {
                        "SHA-256": "<hash value>"
                    },
                    "valid_from": "<valid_from timestamp>"
                },
                // Add more file indicators here
            ]
        },
        {
            "category": "IPv4 Indicators",
            "indicators": [
                {
                    "ip": "<IPv4 address>",
                    "valid_from": "<valid_from timestamp>"
                },
                // Add more IPv4 indicators here
            ]
        },
        {
            "category": "FQDN Indicators",
            "indicators": [
                {
                    "fqdn": "<domain name>",
                    "valid_from": "<valid_from timestamp>"
                },
                // Add more FQDN indicators here
            ]
        },
        {
            "category": "URL Indicators",
            "indicators": [
                {
                    "url": "<URL>",
                    "valid_from": "<valid_from timestamp>"
                },
                // Add more URL indicators here
            ]
        }
    ]
}
```
