#include <LiquidCrystal.h>
//For Crystal Display
int rs = 6;
int en = 7;
int d4 = 8;
int d5 = 9;
int d6 = 10;
int d7 = 11;

LiquidCrystal lcd(rs,en,d4,d5,d6,d7);

//Output to the Relay to Activate Pump
int IN1 = 2;
int IN2 = 3;
int IN3 = 4;
int IN4 = 5;

//Pins from Soil Moisture Sensor
int Pin1 = A0;
int Pin2 = A1;
int Pin3 = A2;
int Pin4 = A3;

//Value recieved from Soil Moisture Sensor Analog Pins
float sensor1Value = 0;
float sensor2Value = 0;
float sensor3Value = 0;
float sensor4Value = 0;

//Soil Moisture Sensor Value as a %
int Plant1Val;
int Plant2Val;
int Plant3Val;
int Plant4Val;

int HV1 = 690;
int HV2 = 700;
int HV3 = 670;
int HV4 = 670;

// Soil Moisture Sensor Lowest Value
int LV1 = 235;
int LV2 = 235;
int LV3 = 235;
int LV4 = 235;

// The different from the Lowest(Driest) to Highest(Wettiest) Value e.g High:520  - Low:185 = Total Difference:385
int tV1 = HV1-LV1;
int tV2 = HV2-LV2;
int tV3 = HV3-LV3;
int tV4 = HV4-LV4;

//Time Delay
int dt1 = 500;
int dt2 = 5000;
int count = 0;

void setup() {
  // put your setup code here, to run once:

lcd.begin(16,2);

Serial.begin(9600);

pinMode(IN1, OUTPUT);
pinMode(IN2, OUTPUT);
pinMode(IN3, OUTPUT);
pinMode(IN4, OUTPUT);

pinMode(Pin1, INPUT);
pinMode(Pin2, INPUT);
pinMode(Pin3, INPUT);
pinMode(Pin4, INPUT);

digitalWrite(IN1, HIGH);
digitalWrite(IN2, HIGH);
digitalWrite(IN3, HIGH);
digitalWrite(IN4, HIGH);

delay(dt1);
}

float sensors(float sensorValue, float Pin, String message,int IN, int LV, int tV)
{
 Serial.print(message);
  sensorValue = analogRead(Pin);
 Serial.println(sensorValue);
  

  if ((-((((sensorValue-LV)/tV)*100.)-100)) < 30)
  {
    digitalWrite(IN, LOW);
  }else{
    digitalWrite(IN, HIGH);
  }

  return sensorValue;
}

void sensorsLcd(int plantVal, float sensorValue, int xPositionLcd,int yPositionLcd,String message,int LV, int tV)
{
    plantVal = (-((((sensorValue-LV)/tV)*100.)-100));
    
    Serial.println(message + plantVal);
    
    lcd.setCursor(xPositionLcd,yPositionLcd);
    lcd.print(message);
    lcd.print(plantVal);
    lcd.print("%");
    //delay(100);
    
    if (plantVal < 30){
     // lcd.clear ();
      lcd.setCursor(xPositionLcd,yPositionLcd);
      lcd.print(message);
      lcd.print("ON   ");
    }
    
   //delay(200);
   //lcd.clear();
   //delay(200);
}

void loop()
{
  sensor1Value = sensors(sensor1Value, Pin1,"Plant 1 - Moisture Level: ",IN1,LV1,tV1);
  sensor2Value = sensors(sensor2Value, Pin2,"Plant 2 - Moisture Level: ",IN2,LV2,tV2);
  sensor3Value = sensors(sensor3Value, Pin3,"Plant 3 - Moisture Level: ",IN3,LV3,tV3);
  sensor4Value = sensors(sensor4Value, Pin4,"Plant 4 - Moisture Level: ",IN4,LV4,tV4);

  sensorsLcd(Plant1Val,sensor1Value,0,0,"P1:",LV1,tV1);
  sensorsLcd(Plant2Val,sensor2Value,8,0,"P2:",LV2,tV2); 
  sensorsLcd(Plant3Val,sensor3Value,0,1,"P3:",LV3,tV3);
  sensorsLcd(Plant4Val,sensor4Value,8,1,"P4:",LV4,tV4); 
    
  delay(2000);

  count++;
  if(count >=10)
  {
    lcd.clear();
    count =0;
  }
  //lcd.clear();
}
