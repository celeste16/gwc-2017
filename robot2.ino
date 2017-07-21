
#include<AF_Motor.h>

AF_DCMotor motor1(3,motor);
AF_DCMotor motor2(4,motor);


void setup();
{
  Serial.begin(9600);
  Serial.println("Motor test");
  motor1.setSpeed(200);
  motor2.setSpeed(200);
  motor1.run(RELEASE);
  motor2.run(RELEASE);
}
void loop()
{
  Serial.print("Forward");
  motor1.run(FORWARD);
  motor2.run(FORWARD);
}  
  


