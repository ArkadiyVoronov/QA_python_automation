from models.drivers import drivers
from flask import request, jsonify


@app.route("/drivers/<driver_id>", methods=["GET"])
def find_driver(driver_id: str) -> Any:
    """Поиск водителя по id."""
    driver = Driver()
    try:
        response = driver.get_driver_info(driver_id)
        if response is None:
            return Response("Объект в базе не найден.", status=404)
        return str(response)
    except Exception:
        return Response("Неправильный запрос.", status=400)


@app.route("/drivers", methods=["POST"])
def create_driver() -> Response:
    """Создание записи о водителе."""
    driver_info = request.get_json()
    try:
        driver = Driver(id=driver_info["id"], name=driver_info["name"], car=driver_info["car"])
        driver.create_driver()
        return Response("Запись создана.", status=201)
    except Exception:
        return Response("Неправильный запрос.", status=400)


@app.route("/drivers/<driver_id>", methods=["DELETE"])
def delete_driver(driver_id: str) -> Response:
    """Удаление водителя из системы."""
    driver = Driver()
    try:
        response = driver.get_driver_info(driver_id)
        if response is None:
            return Response("Объект в базе не найден.", status=404)
        driver.delete_driver(driver_id)
        return Response("Удалено.", status=201)
    except Exception:
        return Response("Неправильный запрос.", status=400)








