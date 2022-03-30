from models.clients import clients
from flask import request, jsonify
#from model import db


@app.route("/clients/<id>", methods=["GET"])
def find_client(client_id: str) -> Any:
    """Поиск клиента по id."""
    client = Client()
    try:
        response = client.get_client_info(client_id)
        if response is None:
            return Response("Объект в базе не найден.", status=404)
        return str(response)
    except Exception:
        return Response("Неправильный запрос.", status=400)


@app.route("/clients/", methods=["POST"])
def create_client() -> Response:
    """Создание записи о клиенте."""
    client_info = request.get_json()
    try:
        client = Client(id=client_info["id"], name=client_info["name"])
        client.create_client()
        return Response("Запись создана.", status=201)
    except Exception:
        return Response("Неправильный запрос.", status=400)


@app.route("/clients/<client_id>", methods=["DELETE"])
def delete_client(client_id: str) -> Response:
    """Удаление клиента из системы."""
    client = Client()
    try:
        response = client.get_client_info(client_id)
        if response is None:
            return Response("Объект в базе не найден.", status=404)
        client.delete_client(client_id)
        return Response("Удалено.", status=201)
    except Exception:
        return Response("Неправильный запрос.", status=400)

