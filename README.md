### INSTALL

`bash ./scripts/install.sh`


### RUN

`bash ./scripts/start.sh`

`start.sh` accepts an optional port number as a param, for example: `bash ./scripts/start.sh 9000`

If the port isn't provided, the default will be 8000

### TEST

`bash ./scripts/test.sh`


### API

**URL:** `/command/` <br>
**Method:** `POST`<br>
**Body \<JSON\>:** ```{
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
