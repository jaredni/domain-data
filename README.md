To run the project locally, use the command:

```bash
docker compose up --build
```

This will start the frontend server on [http://localhost:3000](http://localhost:3000) and the backend server on [http://localhost:8000](http://localhost:8000).


### Environment Variables
The project requires the following environment variables to be set inside /backend/.env:
```
WHOIS_API_KEY=your_whois_api_key
```

