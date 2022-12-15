#Starting the server
- `uvicorn api:app --reload`

#Testing

```
curl --location --request POST 'http://127.0.0.1:8000/env/' \
--header 'Content-Type: application/json' \
-d '{
    "latitude": 32.990254,
    "longitude": 106.974998
}'
```

#DOCS
- OpenAPI standard: `http://127.0.0.1:8000/redoc`
- Swagger UI: `http://127.0.0.1:8000/docs`


