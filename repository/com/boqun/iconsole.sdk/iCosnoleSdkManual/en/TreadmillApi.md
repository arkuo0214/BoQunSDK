# Treadmill API




<div id="BoQunTreadmill"/>
## BoQunTreadmill







Initialize the treadmill

##### BoQunTreadmill.init()



Query treadmill configuration information, maximum and minimum speed and ascension range, etc., callback [onResponseConfigInfo](#onResponseConfigInfo), read failure callback [onError](ErrorCode.md)

##### BoQunTreadmill.queryConfigInfo()



Query treadmill information, call back [onResponseConfigInfo](#onResponseConfigInfo)

##### BoQunTreadmill.queryMachineInfo( int <u>type</u>)

type:

* BoQunTreadmill.TYPE_SPORT_STATUS     //Movement status, callback [onResponseSportStatus](#onResponseSportStatus)
* BoQunTreadmill.TYPE_SPEED_AND_INCLINE  //Speed and Ascension, callback [onResponseSpeedLevel](#onResponseSpeedLevel) and [onResponseInclineLevel](#onResponseInclineLevel)



Start exercise, call back [onResponseSportStatus](#onResponseSportStatus)

##### BoQunTreadmill.start()



Pause motion, call back [onResponseSportStatus](#onResponseSportStatus)

##### BoQunTreadmill.pause()



Stop motion, call back [onResponseSportStatus](#onResponseSportStatus)

##### BoQunTreadmill.stop()



CoolDown mode, callback [onResponseSportStatus](#onResponseSportStatus) and [onCoolDownStateChange](

##### BoQunTreadmill.coolDown()



Set the treadmill speed and call back [onResponseSpeedLevel](#onResponseSpeedLevel)

##### BoQunTreadmill.setSpeedLevel( int <u>speed</u>)

speed 1= 0.1 kilometers



Set treadmill ascension, callback [onResponseInclineLevel](#onResponseInclineLevel)

##### BoQunTreadmill.setInclineLevel( int incline)



Set the fan wind level, call back [onResponseFanLevel](#onResponseFanLevel)

##### BoQunTreadmill.setFanLevel(int level)

The wind level supports 0-3 segments, and the machine does not support adjustment if there is no fan. Get the status of whether the machine has a fan [TreadmillConfigInfo](#TreadmillConfigInfo)





Set the working mode of the lower computer

##### BoQunTreadmill.setWorkMode(@TreadmillWorkMode int mode)

mode:

- TreadmillWorkMode.NORMAL         //This state should be set when the TFT screen is on and enter the working state
- TreadmillWorkMode.SLEEP               //This state should be set when the TFT screen is off and enter sleep mode
- TreadmillWorkMode.SHUT_DOWN  // his state should be set when the TFT is shut down to release resources



Setting up the treadmill listener

##### BoQunTreadmill.setOnTreadmillListener(OnTreadmillListener l)



Enable and disable the serial port, the default is enabled

##### BoQunTreadmill.setSerialPortEnabled(boolean enable)

This method is provided to facilitate handling of special cases. For example, multiple APPs reading the serial port at the same time will cause mutual interference. Using this method can avoid the problem of mutual interference.

<u>Tips: It will not really close the serial port, but it will never read the serial port data</u>



Register status callback listener

##### BoQunTreadmill.registerStateListener(TreadmillStatusCallback callback)



Unregister status callback listener

##### BoQunTreadmill.unregisterStateListener(TreadmillStatusCallback callback)



Unregister all registered status callback listeners

##### BoQunTreadmill.unregisterAllStateListener()



Destroy the instance, release resources

##### BoQunTreadmill.destroy()





## TreadmillStatusCallback



This is an interface class, the treadmill state change and exercise state change callback

```
void onTreadmillSportStateChange(int state);

void onTreadmillStateChange(int state,int speed);
```




<div id="TreadmillStatusCallbacks"/>
## TreadmillStatusCallbacks

​       This is a class that mainly implements some abstract classes to monitor status callbacks. Currently, it supports security Key status monitoring, CoolDown mode monitoring, and unmanned motion monitoring. Other functions will be implemented later if necessary, or you can inherit the TreadmillStatusCallback interface to implement custom status callbacks.



Example:

```java
//Security KEY status monitoring
BoQunTreadmill.registerStateListener(new TreadmillStatusCallbacks.SafetyKeyStatusCallback() {
       @Override
       public void onSafetyKeyStatus(boolean normal) {
            //normal==true secure key insertion
            //normal==false security Key unplug
       }
});
//CoolDown mode listener
BoQunTreadmill.registerStateListener(new TreadmillStatusCallbacks.CoolDownStatusCallback() {
       /**
        * status:
        
        * CoolDownState.START    COOL DOWN mode starts to decelerate
        * CoolDownState.ING      During deceleration, the speed value will become smaller and smaller
        * CoolDownState.END      COOL DOWN mode ends
        *
        * speed: real time speed
        */
       @Override
       public void onCoolDownStatus(int status, int speed) {
          
       }
});

// no movement monitor
long detectionTime=45//Detect unmanned movement time, unit: second

BoQunTreadmill.registerStateListener(
    new TreadmillStatusCallbacks.UnmannedStateDetectionCallback(detectionTime) {
       @Override
       public void onUnmannedStateDetection(boolean isUnmanned, long time) {
           //isUnmanned Whether it is currently unmanned movement, when the unmanned movement time exceeds the detection time, it will become true
           //time Start positive no-run time
       }
});
```

Remember to unregister

```
BoQunTreadmill.unregisterStateListener(xxxx);

//Or, look at individual application scenarios and needs
BoQunTreadmill.unregisterAllStateListener();
```




<div id="OnTreadmillListener"/>
## OnTreadmillListener



<div id="onResponseConfigInfo"/>

Reply to the lower control configuration information

##### void onResponseConfigInfo([TreadmillConfigInfo](#TreadmillConfigInfo) info)



<div id="onResponseSportStatus"/>

return to motion

##### void onResponseSportStatus(@TreadmillSportState int state)

status：

- TreadmillSportState.STOP   stop state
- TreadmillSportState.START start state
- TreadmillSportState.PAUSE pause state
- TreadmillSportState.COOL_DOWN  in COOL DOWN mode
- TreadmillSportState.ERROR   An error occurred


<div id="onResponseSportData"/>
Reply to sports information

##### void onResponseSportData(int heartRate, int speed)

heartRate ：heart rate

speed：real time speed


<div id="onResponseSpeedLevel"/>
Reply to the lower control speed level

##### void onResponseSpeedLevel(int speed)


<div id="onResponseInclineLevel"/>
Reply to Ascension Level under Control

##### void onResponseInclineLevel(int incline)


<div id="onResponseFanLevel"/>
Reply fan wind level

##### void onResponseFanLevel(int level)


<div id="onExternalKeyEvent"/>
Press the external key of the panel (the UP and DOWN buttons can be pressed for a long time) to trigger the callback and reply [TreadmillKeyCode](#TreadmillKeyCode)

##### void onExternalKeyEvent(@TreadmillKeyCode int keyCode, int value)


<div id="onError"/>
Error callback [ErrorCode](ErrorCode.md)

##### void onError(int errorCode)








<div id="BoQunTreadmillFactory"/>
## BoQunTreadmillFactory



Instantiate the treadmill factory

##### BoQunTreadmillFactory.init()



Query treadmill factory information, call back [onResponseFactoryInfo](#onResponseFactoryInfo)

##### BoQunTreadmillFactory.queryFactoryInfo()



Set Treadmill Factory Information

##### BoQunTreadmillFactory.setFactoryInfo(int code, int value)



Start automatic correction, callback [onResponseMotorAutoCorrection](#onResponseMotorAutoCorrection)

##### BoQunTreadmillFactory.startAutoCorrection()



Stop automatic correction, callback [onResponseMotorAutoCorrection](#onResponseMotorAutoCorrection)

##### BoQunTreadmillFactory.stopAutoCorrection()



Treadmill Factory Listener

##### BoQunTreadmillFactory.setOnTreadmillFactoryListener(OnTreadmillFactoryListener listener)



Destroy the treadmill factory instance

##### BoQunTreadmillFactory.destroy()




<div id="OnTreadmillFactoryListener"/>
## OnTreadmillFactoryListener


<div id="onResponseFactoryInfo"/>
Query factory information callback

##### void onResponseFactoryInfo(TreadmillFactoryInfo info)

<div id="onResponseMotorAutoCal"/>
Autocorrect callback

##### void onResponseMotorAutoCorrection(@AutoCorrectionState int status, int speed, int adc, int inclineVR)




<div id="TreadmillConfigInfo"/>
## TreadmillConfigInfo



Get WATT group

##### getWattGroup()

| meta   | description |
| ------ | ----------- |
| return | int         |



Get minimal ascension

##### getMinInclineLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



Get maximum ascension

##### getMaxInclineLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



get min speed

##### getMinSpeedLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



get max speed

##### getMaxSpeedLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



Get the speed increment, when accelerating or decelerating, you should use the current plus or minus getChipSpeedLevel()

##### getChipSpeedLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



Is there ascension

##### hanIncline()

| meta   | description |
| ------ | ----------- |
| return | boolean     |



Is there a fan

##### hasFan()

| meta   | description |
| ------ | ----------- |
| return | boolean     |





<div id="TreadmillKeyCode"/>
## TreadmillKeyCode



start or pause

##### TreadmillKeyCode.KEY_START_PAUSE = 0x01



stop

##### TreadmillKeyCode.KEY_STOP = 0x02



fan

##### TreadmillKeyCode.KEY_FAN = 0x03



Speed plus

##### TreadmillKeyCode.KEY_SPEED_UP = 0x04



speed reduction

##### TreadmillKeyCode.KEY_SPEED_DOWN = 0x05



Ascension Plus

##### TreadmillKeyCode.KEY_INCLINE_UP = 0x06



ascension decrease

##### TreadmillKeyCode.KEY_INCLINE_DOWN = 0x07



COOL_DOWN

##### TreadmillKeyCode.KEY_COOL_DOWN = 0x08



volume up

##### TreadmillKeyCode.KEY_VOLUME_UP = 0x09



volume down

##### TreadmillKeyCode.KEY_VOLUME_DOWN = 0x10



Speed adjustment shortcut keys

##### TreadmillKeyCode.KEY_FAST_SPEED = 0x1A



Ascension Adjustment Hotkeys

##### TreadmillKeyCode.KEY_FAST_INCLINE = 0x1B



Turn the knob forward

##### TreadmillKeyCode.KEY_TURN_KNOB_FORWARD = 0x1C



Knob reversed

##### TreadmillKeyCode.KEY_TURN_KNOB_REVERSE = 0x1D



Return key (can customize the function)

##### TreadmillKeyCode.KEY_BACK = 0x1E

