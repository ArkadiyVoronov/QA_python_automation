from models.orders import orders
from flask import request, jsonify


@app.route("/orders/<order_id>", methods=["GET"])
def find_order(order_id: str) -> Any:
    """Поиск заказа по id."""
    order = Order
    try:
        response = order.get_order_info(order_id)
        if response is None:
            return Response("Объект в базе не найден.", status=404)
        return str(response)
    except Exception:
        return Response("Неправильный запрос.", status=400)


@app.route("/orders", methods=["POST"])
def create_order() -> Response:
    """Создание заказа."""
    order_info = request.get_json()
    try:
        order = Order(
            id=order_info["id"],
            address_from=order_info["address_from"],
            address_to=order_info["address_to"],
            client_id=order_info["client_id"],
            driver_id=order_info["driver_id"],
            date_created=order_info["date_created"],
            status=order_info["status"],
        )
        order.create_order()
        return Response("Запись создана.", status=201)
    except Exception:
        return Response("Неправильный запрос.", status=400)


@app.route("/orders/<order_id>", methods=["PUT"])
def update_order(order_id: str) -> Response:
    """Изменение заказа."""
    order = Order()
    try:
        new_order_data = request.get_json()
        if order.get_order_info(order_id) is None:
            return Response("Объект в базе не найден.", status=404)
        order_status = order.get_order_status(order_id)
        if (
            new_order_data["status"] in ["in_progress", "cancelled"]
            and "not_accepted" in order_status
        ):
            try:
                order.update_order(
                    order_id,
                    new_order_data["client_id"],
                    new_order_data["driver_id"],
                    new_order_data["status"],
                )
                return Response("Запись изменена.", status=201)
            except Exception:
                return Response("Неправильный запрос.", status=400)
        elif (
            new_order_data["status"] in ["done", "cancelled"]
            and "in_progress" in order_status
        ):
            try:
                order.update_order_status(order_id, new_order_data["status"])
                return Response("Запись изменена.", status=201)
            except Exception:
                return Response("Неправильный запрос.", status=400)
        return Response("Неверная последовательность статусов", status=400)
    except Exception:
        return Response("Плохой json.", status=400)
