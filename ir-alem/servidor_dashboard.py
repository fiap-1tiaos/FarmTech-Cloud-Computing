import paho.mqtt.client as mqtt
import json
from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

dados_sensor = {
    "temperatura": 0,
    "umidade": 0,
    "luminosidade": 0,
    "timestamp": ""
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FarmTech Solutions - Dashboard IoT</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1a472a 0%, #2d5a3f 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        header {
            text-align: center;
            color: white;
            margin-bottom: 30px;
        }
        header h1 {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
        header p {
            font-size: 1.1rem;
            opacity: 0.9;
        }
        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .card {
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        }
        .card:hover {
            transform: translateY(-5px);
        }
        .card h3 {
            color: #1a472a;
            font-size: 1rem;
            margin-bottom: 15px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .card .value {
            font-size: 2.5rem;
            font-weight: bold;
            color: #2d5a3f;
        }
        .card .unit {
            font-size: 1rem;
            color: #666;
            margin-left: 5px;
        }
        .card.temperatura .value { color: #e74c3c; }
        .card.umidade .value { color: #3498db; }
        .card.luminosidade .value { color: #f39c12; }
        
        .card .icon {
            font-size: 2rem;
            margin-bottom: 10px;
        }
        .timestamp {
            text-align: center;
            color: white;
            opacity: 0.8;
        }
        .status {
            background: #27ae60;
            color: white;
            padding: 8px 16px;
            border-radius: 20px;
            display: inline-block;
            margin-top: 10px;
        }
    </style>
    <meta http-equiv="refresh" content="5">
</head>
<body>
    <div class="container">
        <header>
            <h1>🌾 FarmTech Solutions</h1>
            <p>Monitoramento em Tempo Real - Sistema IoT</p>
            <div class="status">● Conectado ao MQTT</div>
        </header>
        
        <div class="dashboard">
            <div class="card temperatura">
                <div class="icon">🌡️</div>
                <h3>Temperatura</h3>
                <div class="value">{{ dados.temperatura }}<span class="unit">°C</span></div>
            </div>
            
            <div class="card umidade">
                <div class="icon">💧</div>
                <h3>Umidade</h3>
                <div class="value">{{ dados.umidade }}<span class="unit">%</span></div>
            </div>
            
            <div class="card luminosidade">
                <div class="icon">☀️</div>
                <h3>Luminosidade</h3>
                <div class="value">{{ dados.luminosidade }}<span class="unit">lux</span></div>
            </div>
        </div>
        
        <div class="timestamp">
            <p>Última atualização: {{ dados.timestamp }}</p>
        </div>
    </div>
</body>
</html>
"""

def on_connect(client, userdata, flags, rc):
    print(f"Conectado ao MQTT com código de resultado {rc}")
    client.subscribe("farmtech/sensores")

def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        dados_sensor["temperatura"] = payload.get("temperatura", 0)
        dados_sensor["umidade"] = payload.get("umidade", 0)
        dados_sensor["luminosidade"] = payload.get("luminosidade", 0)
        dados_sensor["timestamp"] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Dados recebidos: {payload}")
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")

@app.route('/')
def dashboard():
    return render_template_string(HTML_TEMPLATE, dados=dados_sensor)

def main():
    client_mqtt = mqtt.Client()
    client_mqtt.on_connect = on_connect
    client_mqtt.on_message = on_message
    
    print("Conectando ao broker MQTT...")
    client_mqtt.connect("broker.hivemq.com", 1883, 60)
    client_mqtt.loop_start()
    
    print("Iniciando servidor web na porta 5000...")
    print("Acesse: http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=False)

if __name__ == "__main__":
    main()
