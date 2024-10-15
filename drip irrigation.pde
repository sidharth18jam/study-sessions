#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>
#include <BlynkTimer.h>
#include <TimeLib.h>
#include <WidgetRTC.h>

char auth[] = "Your_Blynk_Auth_Token";
char ssid[] = "Your_SSID";
char pass[] = "Your_WIFI_Password";

#define SOLENOID_PIN 2
#define MANUAL_OVERRIDE_PIN 3  // New pin for manual override
#define RAIN_SENSOR_PIN A0    // Analog pin for rain sensor
#define BATTERY_PIN A1        // Analog pin for battery voltage reading

BlynkTimer timer;
WidgetRTC rtc;
bool isRaining = false;
unsigned long rainStartTime = 0;
bool isOnBattery = false;
bool wateringDoneToday = false;

void setup()
{
  Serial.begin(115200);
  pinMode(SOLENOID_PIN, OUTPUT);
  pinMode(MANUAL_OVERRIDE_PIN, INPUT_PULLUP);
  digitalWrite(SOLENOID_PIN, HIGH);

  // Check power source
  float voltage = analogRead(BATTERY_PIN) * (3.3 / 1023.0) * 2; // Voltage divider
  isOnBattery = (voltage < 4.5); // Assuming 5V power supply, less than 4.5V means on battery

  if (isOnBattery) {
    // Configure for low power mode
    WiFi.mode(WIFI_SHUTDOWN);
    ESP.deepSleep(300e6); // Sleep for 5 minutes (300 seconds)
  } else {
    Blynk.begin(auth, ssid, pass);
    setSyncInterval(10 * 60); // Sync time every 10 minutes
  }

  timer.setInterval(60000L, checkScheduledWatering); // Check every minute
  timer.setInterval(1000L, checkRainSensor);
  timer.setInterval(1000L, checkManualOverride);
}

void loop()
{
  if (!isOnBattery) {
    Blynk.run();
    timer.run();
  }
}

void closeValve()
{
  digitalWrite(SOLENOID_PIN, HIGH);
  Serial.println("Solenoid valve closed.");
  Blynk.virtualWrite(V2, "Valve closed");
}

void checkRainSensor()
{
  int rainValue = analogRead(RAIN_SENSOR_PIN);
  if (rainValue > 500) { // Adjust this threshold based on your sensor
    if (!isRaining) {
      isRaining = true;
      rainStartTime = millis();
    } else if (millis() - rainStartTime > 600000) { // 10 minutes
      closeValve();
      Blynk.virtualWrite(V2, "Irrigation paused due to rain");
    }
  } else {
    isRaining = false;
    rainStartTime = 0;
  }
}

void checkManualOverride()
{
  if (digitalRead(MANUAL_OVERRIDE_PIN) == LOW) {
    digitalWrite(SOLENOID_PIN, !digitalRead(SOLENOID_PIN));
    String status = digitalRead(SOLENOID_PIN) == LOW ? "opened" : "closed";
    Serial.println("Manual override: Valve " + status);
    Blynk.virtualWrite(V2, "Manual override: Valve " + status);
    delay(1000); // Debounce
  }
}

BLYNK_CONNECTED()
{
  rtc.begin();
}

void checkScheduledWatering()
{
  if (hour() == 8 && minute() == 0 && !wateringDoneToday) {
    if (!isRaining) {
      waterPlants();
    } else {
      Blynk.virtualWrite(V1, "Watering skipped due to rain");
    }
    wateringDoneToday = true;
  } else if (hour() == 0 && minute() == 0) {
    // Reset the flag at midnight
    wateringDoneToday = false;
  }
}

void waterPlants()
{
  digitalWrite(SOLENOID_PIN, LOW);
  delay(300000); // Water for 5 minutes (adjust as needed)
  digitalWrite(SOLENOID_PIN, HIGH);
  
  String message = "Plants watered at " + String(hour()) + ":" + String(minute());
  Blynk.virtualWrite(V1, message);
  Serial.println(message);
}