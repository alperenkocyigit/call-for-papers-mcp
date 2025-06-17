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

## License

MIT