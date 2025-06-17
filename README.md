[![Verified on MseeP](https://mseep.ai/badge.svg)](https://mseep.ai/app/090f67e7-6918-449f-963e-c9ef31dc2aa9)
[![smithery badge](https://smithery.ai/badge/@alperenkocyigit/call-for-papers-mcp)](https://smithery.ai/server/@alperenkocyigit/call-for-papers-mcp)

# Call For Papers MCP

A Smithery MCP for searching academic conferences and events from WikiCFP.

## Description

ConferenceSearcher allows you to search for upcoming academic conferences and events based on keywords. It scrapes conference information from WikiCFP and returns detailed information about each matching event, including name, description, dates, location, and submission deadlines.

## Tool: getEvents

Search for conferences matching specific keywords.

### Parameters

- `keywords` (string, required): Keywords to search for conferences (e.g., 'ai agent', 'machine learning')
- `limit` (number, optional): Maximum number of events to return (default: 10)

### Returns

A JSON object with the following properties:

- `status`: Status of the operation (success/error)
- `count`: Number of events found
- `events`: Array of conference events, each containing:
  - `name`: Name of the conference
  - `title`: Title of the conference
  - `when`: Date and time of the conference
  - `where`: Location of the conference
  - `submission_deadline`: Submission deadline
  - `notification_due`: Notification due date (if available)
  - `wikicfp_link`: Link to the conference page on WikiCFP
  - `external_link`: External conference website URL (if available)
  - `related_resources`: Array of related conferences/resources (if available), each containing:
    - `name`: Name of the related resource
    - `title`: Title of the related resource
    - `url`: WikiCFP URL to the related resource

### Response Example 
```python
python3 app.py "ai agent" 3
```

```json
{
  "status": "success",
  "count": 3,
  "events": [
    {
      "id": "188218",
      "name": "AIAS 2025",
      "title": "Symposium for AI Accelerated Science 2025",
      "when": "Oct 27, 2025 - Oct 28, 2025",
      "where": "San Francisco",
      "submission_deadline": "Aug 1, 2028",
      "notification_due": "Sep 1, 2028",
      "wikicfp_link": "http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=188218&copyownerid=193501",
      "external_link": "https://aias2025.org/",
      "related_resources": [
        {
          "name": "AIxDKE 2026",
          "title": "International Conference on AI x Data and Knowledge Engineering",
          "url": "http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=188224"
        }
      ]
    },
    {
      "id": "186126",
      "name": "PRIMA 2025",
      "title": "26th International Conference on Principles and Practice of Multi-Agent Systems",
      "when": "Dec 15, 2025 - Dec 19, 2025",
      "where": "Modena",
      "submission_deadline": "Jul 22, 2025 (Jul 15, 2025)",
      "notification_due": "Sep 29, 2025",
      "wikicfp_link": "http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=186126&copyownerid=186186",
      "external_link": "https://conferences-website.github.io/prima2025/",
      "related_resources": [
        {
          "name": "Ei/Scopus-CCNML 2025",
          "title": "2025 5th International Conference on Communications, Networking and Machine Learning (CCNML 2025)",
          "url": "http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=127474"
        }
      ]
    },
    {
      "id": "185890",
      "name": "EUMAS 2025",
      "title": "The 22nd European Conference on Multi-Agent Systems",
      "when": "Sep 3, 2025 - Sep 5, 2025",
      "where": "Bucharest, Romania",
      "submission_deadline": "May 16, 2025",
      "notification_due": "Jun 30, 2025",
      "wikicfp_link": "http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=185890&copyownerid=191777",
      "external_link": "https://euramas.github.io/eumas2025/",
      "related_resources": [
        {
          "name": "Ei/Scopus-CCNML 2025",
          "title": "2025 5th International Conference on Communications, Networking and Machine Learning (CCNML 2025)",
          "url": "http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=127474"
        },
        {
          "name": "PRIMA 2025",
          "title": "26th International Conference on Principles and Practice of Multi-Agent Systems",
          "url": "http://www.wikicfp.com/cfp/servlet/event.showcfp?eventid=186126"
        }
      ]
    }
  ]
}
```

## License
This project is licensed under the GNU(GENERAL PUBLIC LICENSE) v3 - see the [LICENSE](LICENSE) file for details.