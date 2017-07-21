#include <Servo.h>
int rightWhiskerPin = 7;
int leftWhiskerPin = 5;
int rightWhiskerState = 0;
int leftWhiskerState = 0;
Servo servoLeft;
Servo servoRight;
void setup() {
// put your setup code here, to run once:

delay(1000); 
pinMode(rightWhiskerPin, INPUT);
pinMode(leftWhiskerPin, INPUT);
Serial.begin(9600);
//Attach Left Servo
//Attach Right Servo
servoLeft.writeMicroseconds(1500);
servoRight.writeMicroseconds(1300);

}
void loop() {
// put your main code here, to run repeatedly:
rightWhiskerState = digitalRead(rightWhiskerPin);
leftWhiskerState = digitalRead(leftWhiskerPin);
// whisker state is 1 if unpressed and 0 if pressed.
if(rightWhiskerState == 0 && leftWhiskerState == 0){
//Make it move away from the Obstacle
}
else if(leftWhiskerState == 0){
//Make it move away from the Obstacle
}
else if(rightWhiskerState == 0){
//Make it move away from the Obstacle
}
else{
//Just move
}
}
void stopnow(){
servoLeft.writeMicroseconds(1500);
servoRight.writeMicroseconds(1500);
}
void forward(int time) // Forward function
{
// Left wheel counterclockwise
// Right wheel clockwise
// Maneuver for time ms
}
void turnLeft(int time) // Left turn function
{
}
void turnRight(int time) // Right turn function
{

}
void backward(int time) // Backward function
{
}
