# API Consumption Service

## Overview

The `api_consumption` service integrates the backend with the RAWG Video Games Database API. Its current responsibility is to retrieve the complete list of video game genres and expose that information through a local FastAPI endpoint.

The service separates external API communication, business access, data validation, and HTTP routing into independent components.

## Main Flow

```text
Client request
    ↓
FastAPI route
    ↓
CRUD service
    ↓
RAWG API client
    ↓
RAWG API
    ↓
Validated response
    ↓
Client
```

## Current Functionality

The service:

- retrieves genres from the RAWG API
- authenticates requests using the `RAWG_API_KEY` environment variable
- processes paginated RAWG responses
- combines all genre results into a single response
- validates the response using Pydantic schemas
- exposes the data through a FastAPI endpoint

## Endpoint

```http
GET /rawg/genres
```

The endpoint returns a collection of video game genres, including fields such as:

- `id`
- `name`
- `slug`
- `games_count`
- `image_background`

## External Dependency

The service consumes the following RAWG API resource:

```text
https://api.rawg.io/api/genres
```

The API key is read from:

```text
RAWG_API_KEY
```

## Response Structure

The response contains:

- `count`: total number of retrieved genres
- `next`: next page reference, returned as `null`
- `previous`: previous page reference, returned as `null`
- `results`: list of genre objects