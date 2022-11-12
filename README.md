### INSTALL

`bash ./scripts/install.sh`


### RUN

`bash ./scripts/start.sh`

### TEST

`bash ./scripts/test.sh`


### API

**URL:** `/command/` <br>
**Method:** `POST`<br>
**Body:** <JSON>: ```{
  "command": string
}```

### EXAMPLE

**Request:**

```shell
curl -X 'POST' \
  'http://localhost:8000/command/' \
  -H 'accept: text/plain' \
  -H 'Content-Type: application/json' \
  -d '{
  "command": "date"
}'
```

**Response:**

`Sat Nov 12 12:57:16 EET 2022`
