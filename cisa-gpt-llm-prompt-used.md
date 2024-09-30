## Prompt Used

You are given a JSON file from a cybersecurity advisory with multiple indicators of compromise (IOCs) such as files, IP addresses, domains, and URLs. Break down the IOCs into the following categories in a JSON format, but only include file indicators where the filename ends with the characters "stix_.json". Extract the corresponding data and structure it accordingly:


1. File Indicators: Extract file names that end with "stix_.json" and their corresponding hashes (e.g., SHA-256). If the hash is missing, include an empty object for the "hashes" field.
1. IPv4 Indicators: Extract all IPv4 addresses.
1. FQDN Indicators: Extract fully qualified domain names (FQDN).
1.URL Indicators: Extract all URLs.


Here’s the required JSON structure:

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

## Additional instructions:
- Only include file indicators where the file name ends with "stix_.json".
- If any indicators are missing hashes, include the indicator with an empty "hashes" field.
- Ensure that each indicator includes the correct valid_from timestamp.
- Organize the IOCs into the appropriate categories based on their type (File, IP, FQDN, or URL).
