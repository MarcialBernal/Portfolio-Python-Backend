# API Consumption Service - Technical Documentation

## 1. Module Structure

```text
api_consumption/
├── crud.py
├── rawg_api_client.py
├── schemas.py
└── routers/
    ├── routes.py
    └── __init__.py
```

## 2. External API Client

### File

```text
rawg_api_client.py
```

### Configuration

```python
RAWG_BASE_URL = "https://api.rawg.io/api"
API_KEY = os.getenv("RAWG_API_KEY")
```

The base URL identifies the RAWG API. The API key is loaded from the `RAWG_API_KEY` environment variable and is sent as a query parameter.

### `get_genres()`

The `get_genres()` function requests the RAWG genres endpoint:

```text
GET https://api.rawg.io/api/genres
```

The request includes:

```python
params = {"key": API_KEY}
```

The HTTP request uses a timeout of 10 seconds:

```python
requests.get(url, params=params, timeout=10)
```

The function calls `raise_for_status()`, which raises an exception when the external API returns an HTTP error.

## 3. Pagination

RAWG returns pagination information through the `next` field.

The client uses a loop:

```python
while url:
```

For every page:

1. sends a request
2. parses the JSON response
3. appends the values from `results`
4. obtains the next page URL from `data.get("next")`
5. continues until there is no next page

All retrieved genres are accumulated in the `results` list.

The function returns a normalized response:

```python
{
    "count": len(results),
    "next": None,
    "previous": None,
    "results": results
}
```

The final response contains all pages in one collection.

## 4. CRUD Layer

### File

```text
crud.py
```

### `fetch_genres()`

The `fetch_genres()` function delegates the external request to `get_genres()`:

```python
def fetch_genres() -> dict:
    data = get_genres()
    return data
```

This layer separates route handling from the external API client and provides a service-level entry point for genre retrieval.

## 5. Pydantic Schemas

### File

```text
schemas.py
```

### `Genre`

Represents an individual RAWG genre:

```python
class Genre(BaseModel):
    id: int
    name: str
    slug: Optional[str] = None
    games_count: Optional[int] = None
    image_background: Optional[str] = None
```

Required fields:

- `id`
- `name`

Optional fields:

- `slug`
- `games_count`
- `image_background`

### `GenresResponse`

Represents the complete response:

```python
class GenresResponse(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[Genre]
```

It validates:

- the total count
- pagination fields
- the list of returned genres
- the structure of every genre object

## 6. FastAPI Router

### File

```text
routers/routes.py
```

The router defines the following endpoint:

```python
@router.get("/rawg/genres", response_model=GenresResponse)
def get_genres_route():
    return fetch_genres()
```

### Endpoint Contract

```http
GET /rawg/genres
```

The `response_model=GenresResponse` configuration instructs FastAPI to validate and serialize the returned data according to the Pydantic schema.

## 7. Request Flow

```text
GET /rawg/genres
    ↓
get_genres_route()
    ↓
fetch_genres()
    ↓
get_genres()
    ↓
RAWG /api/genres
    ↓
Pagination processing
    ↓
GenresResponse validation
    ↓
HTTP response
```

## 8. Error Handling

The external client currently handles HTTP errors through:

```python
response.raise_for_status()
```

A timeout of 10 seconds is configured for each request. Network errors, timeout errors, and HTTP errors propagate to the caller unless they are handled by a higher-level exception handler.

## 9. Environment Configuration

The service requires the following environment variable:

```text
RAWG_API_KEY
```

The value is loaded when `rawg_api_client.py` is imported.

## 10. Current Scope

The current implementation exposes only the RAWG genres resource. The structure can be extended with additional client functions, CRUD methods, schemas, and routes for other RAWG resources.