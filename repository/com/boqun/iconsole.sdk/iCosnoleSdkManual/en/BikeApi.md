# Bike API



<div id="BoQunBike"/>

## BoQunBike





instantiated bicycle

##### BoQunBike.init()





Query bicycle configuration information resistance, ascension range, status, etc., callback [onResponseConfigInfo](#onResponseConfigInfo), read failure callback [onError](ErrorCode.md)

##### BoQunBike.queryConfigInfo()





Inquire about bicycle information

##### BoQunBike.queryMachineInfo( int <u>type</u>)

type：

- BoQunBike.TYPE_SPORT_STATUS    sport state, callback[onResponseSportStatus](#onResponseSportStatus)

- BoQunBike.TYPE_LOAD_LEVEL         load level, callback[onResponseLoadLevel](#onResponseLoadLevel)





Start the exercise, call back [onResponseSportStatus](#onResponseSportStatus) after the start is successful, and start transmitting data [onResponseSportData](#onResponseSportData)

##### BoQunBike.start()





Pause the movement, and call back [onResponseSportStatus](#onResponseSportStatus) after the pause is successful. No movement data will be transmitted during the pause state.

##### BoQunBike.pause()





Stop motion, call back [onResponseSportStatus](#onResponseSportStatus)

##### BoQunBike.stop()





Control the resistance level of the bicycle, call back [onResponseLoadLevel](#onResponseLoadLevel)

##### BoQunBike.setLoadLevel( int <u>load</u> )

The larger the load value, the greater the resistance. The load has a range limit. The load range parameter reads [BikeConfigInfo](#BikeConfigInfo)





Control the bicycle to upgrade the level, and call back [onResponseInclineLevel](#onResponseInclineLevel)

##### BoQunBike.setInclineLevel( int <u>incline</u> )

The larger the incline value, the higher the inclination. The incline has a range limit. The incline range parameter reads [BikeConfigInfo](#BikeConfigInfo)





Control the fan wind level, call back [onResponseFanLevel](#onResponseFanLevel)

##### BoQunBike.setFanLevel( int <u>level</u>)

The wind level supports 0-3 segments, and the machine does not support adjustment if there is no fan. Get the status of whether the machine has a fan [BikeConfigInfo](#BikeConfigInfo)





Set the working mode of the bicycle lower computer

##### BoQunBike.setWorkMode( int <u>mode</u>)

mode:

- BikeWorkMode.NORMAL          //This state should be set when the TFT screen is on, and enter the working state
- BikeWorkMode.SLEEP               //This state should be set when the TFT screen is turned off, and enter sleep mode
- BikeWorkMode.SHUT_DOWN  //This state should be set when the TFT is powered off to release resources





To enable or disable FMTS, it must be used with the lower control board with FMTS function

##### BoQunBike.setFTMSEnabled( boolean <u>enable</u>)





Enable and disable the serial port, the default is enabled

##### BoQunBike.setSerialPortEnabled( boolean <u>enable</u>)

This method is provided to facilitate handling of special cases. For example, multiple APPs reading the serial port at the same time will cause mutual interference. Using this method can avoid the problem of mutual interference.

<u>Tips: It will not really close the serial port, but it will never read the serial port data</u>



bike monitor

##### BoQunBike.setBikeListener([OnBikeListener](#OnBikeListener) listener)



Register status callback listener

##### BoQunBike.registerStateListener(BikeStatusCallback callback)



Unregister status callback listener

##### BoQunBike.unregisterStateListener(BikeStatusCallback callback)



Unregister all registered status callback listeners

##### BoQunBike.unregisterAllStateListener()



Destroy the instance, release resources

##### BoQunBike.destroy()





## BikeStatusCallback



Bicycle state change callback

##### void onBikeSportStateChange(int status)




<div id="BikeStatusCallbacks"/>
## BikeStatusCallbacks

​       This is the class that mainly implements the status callback. Currently, it supports monitoring the FTMS status. If there is a need to implement other functions later, or you can inherit the BikeStatusCallback interface to implement custom status callbacks



Currently implemented FMTS switch status callback

```java
BoQunBike.registerStateListener(new BikeStatusCallbacks.FTMSStateCallback() {
            @Override
            public void onFTMSStateChange(boolean enable) {
                 //enable On and off state
            }
        });
```

Remember to unregister

```java
BoQunBike.unregisterStateListener(xxxx);

//Or, look at individual application scenarios and needs
BoQunBike.unregisterAllStateListener();
```





<div id="OnBikeListener"/>

## OnBikeListener



<div id="onResponseConfigInfo"/>

Reply to the lower control configuration information

##### void onResponseConfigInfo([BikeConfigInfo](#BikeConfigInfo) info)



<div id="onResponseSportStatus"/>

return to motion

##### void onResponseSportStatus(@BikeSportState int status)

status：

- BikeSportState.STOP   //stop state
- BikeSportState.START //start state
- BikeSportState.PAUSE //pause state



<div id="onResponseSportData"/>

Reply to sports information

##### void onResponseSportData(int stepCount, int rpm, int heartRate)

stepCount：Number of steps (accumulated value)

rpm：RPM

heartRate：heartbeat



<div id="onResponseLoadLevel"/>

Reply to the lower control resistance level

##### void onResponseLoadLevel(int load)



<div id="onResponseInclineLevel"/>

Reply to Ascension Level under Control

##### void onResponseInclineLevel(int incline)



<div id="onResponseFanLevel"/>

Reply fan wind level

##### void onResponseFanLevel(int level)



<div id="onExternalKeyEvent"/>

Press the external key on the panel (the UP and DOWN buttons can be long-pressed) to trigger the callback and reply [BikeKeyCode](#BikeKeyCode)

##### void onExternalKeyEvent([@BikeKeyCode](#BikeKeyCode) int keyCode)



<div id="onError"/>

Error callback [ErrorCode](ErrorCode.md)

##### void onError(int errorCode)





<div id="BoQunBikeFactory"/>
## BoQunBikeFactory





Instantiate a bicycle factory

##### BoQunBikeFactory.init()



Query the resistance motor stroke of the specified resistance level, and call back [onResponseLoadMotorStoke](#onResponseLoadMotorStoke)

##### BoQunBikeFactory.queryLoadMotorStroke( int load)



Query the ascension motor stroke of the specified ascension level, and call back [onResponseInclineMotorStroke](#onResponseInclineMotorStroke)

##### BoQunBikeFactory.queryInclineMotorStroke( int incline)



Set the machine wheel diameter

##### BoQunBikeFactory.setWheelDiameter( int wheelDiameter)



Set the ADC value of the resistance motor stroke for the specified resistance level

##### BoQunBikeFactory.setLoadMotorStroke( int load, int adc)



Set the ADC value of the ascension motor stroke for the specified ascension level

##### BoQunBikeFactory.setInclineMotorStroke( int incline, int adc)



Start the automatic correction of the ascension motor, call back [onResponseInclineAutoCorrection](#onResponseInclineAutoCorrection)

##### BoQunBikeFactory.startInclineAutoCorrection()



Start the automatic correction of the ascension motor, call back [onResponseInclineAutoCorrection](#onResponseInclineAutoCorrection)

direction Correction direction

- AutoCorrectionDirection.AUTO Default is auto orientation
- AutoCorrectionDirection.UP
- AutoCorrectionDirection.DOWN

##### BoQunBikeFactory.startInclineAutoCorrection(@AutoCorrectionDirection int direction)



Stop the automatic correction of the ascension motor and call back [onResponseInclineAutoCorrection](#onResponseInclineAutoCorrection)

##### BoQunBikeFactory.stopInclineAutoCorrection()



Bike Factory Mode Monitor

##### BoQunBikeFactory.setOnBikeFactoryListener( [OnBikeFactoryListener](#OnBikeFactoryListener) listener)



Destroy the instance, release resources

##### BoQunBikeFactory.destroy()







<div id="OnBikeFactoryListener"/>
## OnBikeFactoryListener




<div id="onResponseLoadMotorStoke"/>
Reply the motor stroke ADC of the specified resistance level

##### void onResponseLoadMotorStoke(int load, int adc)




<div id="onResponseInclineMotorStroke"/>
Reply to the motor stroke ADC of the specified ascension level

##### void onResponseInclineMotorStroke(int incline, int adc)




<div id="onResponseInclineAutoCal"/>
Reply the status of auto calibration and ADC value

##### void onResponseInclineAutoCorrection(@AutoCorrectionStateint state, int inclineADC)

state:

- AutoCorrectionState.CORRECTION_START  //Ascension Motor Calibration Begins
- AutoCorrectionState.CORRECTION_ING      //Lifting motor calibration
- AutoCorrectionState.CORRECTION_STOP   //Lift motor calibration stop

inclineADC:The value range is 0-255. The ADC will keep changing during the ascension motor calibration. The normal situation is from small to large, and from large to small is a complete calibration.







<div id="BikeConfigInfo"/>

## BikeConfigInfo





##### getClientId()

Obtain customer ID to meet the customized needs of different customers

| meta   | description |
| ------ | ----------- |
| return | int         |



##### getWattGroup()

Get watt group

| meta   | description |
| ------ | ----------- |
| return | int         |




##### getWheelDiameter()

get wheel diameter

| meta   | description |
| ------ | ----------- |
| return | int         |



##### isManualControl()

Whether it is manual control

| meta   | description |
| ------ | ----------- |
| return | boolean     |



##### getMinLoadLevel()

Get the least resistance level

| meta   | description |
| ------ | ----------- |
| return | int         |



##### getMaxLoadLevel()

Get the maximum resistance level

| meta   | description |
| ------ | ----------- |
| return | int         |




##### getNegativeInclineLevel()

Get Negative Ascension Level

| meta   | description |
| ------ | ----------- |
| return | int         |




##### getMinInclineLevel()

Get the minimum ascension level

| meta   | description |
| ------ | ----------- |
| return | int         |




##### getMaxInclineLevel()

Get the maximum ascension level

| meta   | description |
| ------ | ----------- |
| return | int         |



##### hasIncline()

Whether the machine is equipped with ascension

| meta   | description |
| ------ | ----------- |
| return | boolean     |



##### hasFan()

Whether the machine is equipped with a fan

| meta   | description |
| ------ | ----------- |
| return | boolean     |





##### hasFTMS()

Whether the machine is configured with FMTS function

| meta   | description |
| ------ | ----------- |
| return | boolean     |





<div id="BikeKeyCode"/>

## BikeKeyCode



start or pause

##### BikeKeyCode.KEY_START_PAUSE = 0x01



stop

##### BikeKeyCode.KEY_STOP = 0x02



resistance plus

##### BikeKeyCode.KEY_LOAD_UP = 0x03



resistance reduction

##### BikeKeyCode.KEY_LOAD_DOWN = 0x04



Ascension Plus

##### BikeKeyCode.KEY_INCLINE_UP = 0x05



ascension decrease

##### BikeKeyCode.KEY_INCLINE_DOWN = 0x06



fan

##### BikeKeyCode.KEY_FAN = 0x07



