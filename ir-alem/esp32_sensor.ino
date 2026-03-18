#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

#define DHTPIN 4
#define DHTTYPE DHT11
#define LDR_PIN 34

const char* ssid = "SUA_REDE_WIFI";
const char* password = "SUA_SENHA_WIFI";
const char* mqtt_server = "broker.hivemq.com";
const char* mqtt_topic = "farmtech/sensores";

DHT dht(DHTPIN, DHTTYPE);
WiFiClient espClient;
PubSubClient client(espClient);

unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE (200)
char msg[MSG_BUFFER_SIZE];

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Conectando a ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi conectado");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Mensagem recebida no topic: ");
  Serial.println(topic);
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
}

void reconnect() {
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);
    if (client.connect(clientId.c_str())) {
      Serial.println("conectado ao MQTT!");
      client.subscribe(mqtt_topic);
    } else {
      Serial.print("falha, rc=");
      Serial.print(client.state());
      Serial.println(" tentando novamente em 5 segundos");
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  dht.begin();
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  pinMode(LDR_PIN, INPUT);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  unsigned long now = millis();
  if (now - lastMsg > 5000) {
    lastMsg = now;
    
    float temperatura = dht.readTemperature();
    float umidade = dht.readHumidity();
    int luminosidade = analogRead(LDR_PIN);

    // Fazendo cálculo manual pois o sensor está "invertido" 
    // mais luz, está diminuindo o valor, e menos está aumentando o valor 
    // (4095 -> 12 bits)
    int luminosidadeInvertida = 4095 - luminosidade;
    
    if (isnan(temperatura) || isnan(umidade)) {
      Serial.println("Falha ao ler do sensor DHT!");
      return;
    }

    String payload = "{";
    payload += "\"temperatura\":" + String(temperatura) + ",";
    payload += "\"umidade\":" + String(umidade) + ",";
    payload += "\"luminosidade\":" + String(luminosidadeInvertida);
    payload += "}";

    payload.toCharArray(msg, MSG_BUFFER_SIZE);
    client.publish(mqtt_topic, msg);
    
    Serial.println("Dados enviados:");
    Serial.print("Temperatura: ");
    Serial.print(temperatura);
    Serial.println(" *C");
    Serial.print("Umidade: ");
    Serial.print(umidade);
    Serial.println(" %");
    Serial.print("Luminosidade: ");
    Serial.println(luminosidadeInvertida);
  }
}
