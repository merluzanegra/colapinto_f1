from flask import Flask, jsonify
import livef1

app = Flask(__name__)

@app.route("/colapinto")
def colapinto_data():
    try:
        # Objeto Live Timing
        session = livef1.LiveTiming()

        # Asegurarse de que la sesión esté cargada
        if not session.is_ready:
            session.update()

        # Buscar al piloto
        drivers = session.driver_numbers
        colapinto_number = None

        # Detección del número de Colapinto
        for num, drv in drivers.items():
            if "COLAPINTO" in drv["name"].upper():
                colapinto_number = num
                break

        if colapinto_number is None:
            return jsonify({"error": "No se encontró Colapinto"}), 404

        d = session.drivers[colapinto_number]

        # Preparar JSON
        data = {
            "driver": d["name"],
            "position": d.get("position"),
            "gap": d.get("gap"),
            "speed": d.get("speed_trap", {}).get("speed"),
            "sectors": [
                d["sectors"].get("1"),
                d["sectors"].get("2"),
                d["sectors"].get("3")
            ],
            "best_lap": d.get("best_lap_time"),
            "pit_status": d.get("pit_status"),
            "lap": d.get("laps")
        }

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/")
def root():
    return jsonify({
        "status": "OK",
        "info": "Endpoint disponible en /colapinto"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
