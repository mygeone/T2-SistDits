# Generate new order

Insert a new order into Kafka data stream as producer

**URL** : `/newOrder`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

## Success Response

**Code** : `200 OK`

**Content examples**

For a vendor with cart `ID = 100`, `email = miguel.contreras1@mail.udp.cl` and one product with `ID,price and quantity`:

```json
{
    "vendor": {
        "email": "miguel.contreras1@mail.udp.cl",
        "cart_id": 100
    },
    "report": [
        {
            "id": 2,
            "price": 1500,
            "quantity": 2
        }
    ]
}
```

For a vendor with cart `ID = 100`, `email = miguel.contreras1@mail.udp.cl` and a list of product with `ID,price and quantity`:

```json
{
    "vendor": {
        "email": "miguel.contreras1@mail.udp.cl",
        "cart_id": 100
    },
    "report": [
        {
            "id": 2,
            "price": 1500,
            "quantity": 2
        },
        {
            "id": 7,
            "price": 15100,
            "quantity": 3
        },
        {
            "id": 2,
            "price": 500,
            "quantity": 10
        }
    ]
}
```
