## Running server
```bash
docker build -t sendify . && docker run --rm --name sendify-app -p 8080:8080 sendify
```
## Testing backend against request
(Must have cURL installed)
```bash
./test_request.sh
```