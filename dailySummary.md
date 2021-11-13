# Daily Summary

Generate a new daily summary for all carts by consuming `Orders` topic with registered sales, produce a new summary into `dailySummary` topic and generate a email notification for all vendors registered in topic.

**URL** : `/dailySummary`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**

Returns a daily summary with ID of vendor as key, and report as values.

```json
{
    "1": {
        "email": "dne@gmail.com",
        "totalVentas": 4
    },
    "13": {
        "email": "myge.one@gmail.com",
        "totalVentas": 25
    },
    "16": {
        "email": "myge.oasdne@gmail.com",
        "totalVentas": 3
    },
    "69": {
        "email": "m.contreraspezoa@gmail.com",
        "totalVentas": 4
    },
    "100": {
        "email": "miguel.contreras1@mail.udp.cl",
        "totalVentas": 1
    }
}
```

