# Authorization REST API

POST /register

{
    email, phone, name, role
}

Response:
- 201, {id}
- 400
- 500

{
    error_message: $message
}

POST /login

{
    login,
    password
}

Response:
- 200, {token, expiration}
- 400
- 500

{
    error_message: $message
}

# Customer REST API

GET /orders

Header:
- x-auth-token: $token

- 200
- 401 (access denied)
- 500
- 400

{
    orders: [
        {
            id: 1,
            restraunt: {
                name
            },
            timestamp,
            items: [
                {
                    price, quantity, description, image
                }
            ]
        }
    ],
    page_index: 0,
    page_count: 10
}

GET /order/${id}

- 200
- 400
- 401 (access denied)
- 404
- 500

ResponseBody

{
    id: 1,
    restraunt: {
        name
    },
    timestamp,
    items: [
        {
            price, quantity, description, image
        }
    ]
}

GraphQL


POST /order

{
    restraunt_id,
    menu_items: [
        {quantity, menu_item_id}
    ]
}

Response:

OK
{
  id,
  secret_payment_url,
  estimated_time_of_arrival
}

---

# Restaurant REST API

GET /orders?status=active/complete/denied

Response:
{
    orders: [
        {
            id,
            menu_items: [
                {quantity, menu_item_id}
            ]            
        }
    ],
    page_index: 0,
    page_count: 10
}

POST (patch?) /order/${id}/

Request body:
{
    order_action: deny/accept/complete
}

Response:
- 200
- 400
- 401 (access denied)
- 403 (forbidden)
- 404
- 500

---

# Courier REST API

GET /deliveries?status=active/complete

Response:
{
    delivery: [
        {
            order_id,
            restraunt: {
                address,
                distance
            }         
            customer: {
                address,
                distance
            },
            payment
        }
    ],
    page_index: 0,
    page_count: 10
}

Response:
- 200
- 400
- 401 (access denied)
- 500

---

POST (patch?) /develiry/${id}/

Request body:
{
    order_action: accept/complete
}

Response:
- 200
- 400
- 401 (access denied)
- 403 (forbidden)
- 404
- 500

---

RabbitMQ queue schema (logitics)

- Queue (producer, consumer)
- Fanout (?)
- 1 queue - 1 data type (model)
- EMAIL_SENDING_QUEUE, EMAIL_SENDING_QUEUE_V2
- RabbitMQ cookbook, RabbitMQ best practices