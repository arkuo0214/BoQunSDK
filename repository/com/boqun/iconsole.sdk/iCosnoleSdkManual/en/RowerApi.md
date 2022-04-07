# Rower Machine API



<div id="BoQunRower"/>

## BoQunRower



Instantiate the rowing machine

##### BoQunRower.init()



Query rowing machine configuration information resistance, fan status, etc., callback [onResponseConfigInfo](#onResponseConfigInfo), read failure callback [onError](ErrorCode.md)

##### BoQunRower.queryConfigInfo()



Query rowing machine information

##### BoQunRower.queryMachineInfo(int type)

type：

- BoQunRower.TYPE_SPORT_STATUS    Movement status, callback [onResponseSportStatus](#onResponseSportStatus)
- BoQunRower.TYPE_LOAD_LEVEL         Resistance level, callback [onResponseLoadLevel](#onResponseLoadLevel)



Start exercise, call back [onResponseSportStatus](#onResponseSportStatus)

##### BoQunRower.start()



Pause motion, call back [onResponseSportStatus](#onResponseSportStatus)

##### BoQunRower.pause()



Stop motion, call back [onResponseSportStatus](#onResponseSportStatus)

##### BoQunRower.stop()



Control the resistance level of the rowing locomotive, callback [onResponseLoadLevel](#onResponseLoadLevel)

##### BoQunRower.setLoadLevel(int level)

The larger the level value, the greater the resistance. The level has a range limit. The level range parameter is read [RowerConfigInfo](#RowerConfigInfo)



Control the fan wind level, call back [onResponseFanLevel](#onResponseFanLevel)

##### BoQunRower.setFanLevel(int level)

The wind power level supports 0-3 segments. If the machine does not have a fan, it does not support adjustment. Get the status of whether the machine has a fan [RowerConfigInfo](#RowerConfigInfo)



Set the working mode of the rowing machine slave computer

##### BoQunRower.setWorkMode(@RowerWorkMode int mode)

mode:

- RowerWorkMode .NORMAL   When the TFT screen is on, this state should be set to enter the working state
- RowerWorkMode .SLEEP         When the TFT screen is turned off, this state should be set to enter the sleep mode
- RowerWorkMode .SHUT_DOWN     This state should be set when the TFT is powered off to release resources



rowing machine monitor

##### BoQunRower.setOnRowerListener(OnRowerListener onRowerListener)



Enable and disable the serial port, the default is enabled

##### BoQunRower.setSerialPortEnabled(boolean enable)

This method is provided to facilitate handling of special cases. For example, multiple APPs reading the serial port at the same time will cause mutual interference. Using this method can avoid the problem of mutual interference.

<u>Tips: It will not really close the serial port, but it will never read the serial port data</u>



Destroy the instance, release resources

##### BoQunRower.destroy()






<div id="OnRowerListener"/>
## OnRowerListener




<div id="onResponseConfigInfo"/>

Reply to the lower control configuration information


##### void onResponseConfigInfo([RowerConfigInfo](#RowerConfigInfo) info)




<div id="onResponseSportStatus"/>

return to motion


##### void onResponseSportStatus(@RowerSportState int status)

status：

- RowerSportState .STOP   stop state
- RowerSportState .START start state
- RowerSportState .PAUSE pause state




<div id="onResponseSportData"/>

Reply to sports information

##### void onResponseSportData([RowerSportData](#RowerSportData) data)




<div id="onResponsePullAndPut"/>

Reply pull and release status and progress value


##### void onResponsePullAndPut(@IntRange(from = 0, to = 100) int progress, boolean isPull)

progress：Pull and release stroke percentage

isPull  = true   pull ，isPull  = false   put




<div id="onResponseLoadLevel"/>

Recovery resistance level


##### void onResponseLoadLevel(int load)




<div id="onResponseFanLevel"/>

Reply fan wind level


##### void onResponseFanLevel(int level)




<div id="onExternalKeyEvent"/>

Press the external key of the panel (the UP and DOWN buttons can be pressed for a long time) to trigger the callback and reply [RowerKeyCode](#RowerKeyCode)


##### void onExternalKeyEvent(@RowerKeyCode int keyCode)



An error occurred callback [ErrorCode](ErrorCode.md)

##### void onError(int errorCode)






<div id="BoQunRowerFactory"/>
## BoQunRowerFactory





Instantiate the rowing machine factory

##### BoQunRowerFactory.init()



Query rowing machine factory information, call back [onResponseFactoryInfo](#onResponseFactoryInfo)

##### BoQunRowerFactory.queryFactoryInfo()



Query the motor stroke and call back [onResponseLoadMotorStroke](#onResponseLoadMotorStroke)

##### BoQunRowerFactory.queryLoadMotorStroke(int load)



Set the motor stroke

##### BoQunRowerFactory.setLoadMotorStroke(int load, int adc)




<div id="setRepairDirection"/>
fix motor error

##### BoQunRowerFactory.setRepairDirection(@RowerRepairDirection int direction)

direction：

- RowerRepairDirection.UP     fix above
- RowerRepairDirection.DOWN  fix below



Modify rowing machine factory information

##### BoQunRowerFactory.setFactoryInfo(RowerFactoryInfo info)



Rowing Machine Factory Listener

##### BoQunRowerFactory.setOnRowerFactoryListener(OnRowerFactoryListener listener)



Destroy factory pattern instance

##### BoQunRowerFactory.destroy()






<div id="OnRowerFactoryListener"/>
## OnRowerFactoryListener 



Reply to factory information

##### void onResponseFactoryInfo([RowerFactoryInfo](#RowerFactoryInfo ) info)



return motor stroke

##### void onResponseLoadMotorStroke(int load, int adc)



return motor status

##### void onResponseMotorStatus(int status)

status：

- RowerMotorStatus.NORMAL    //normal
- RowerMotorStatus.ERROR_UP     //error above
- RowerMotorStatus.ERROR_DOWN  //error below

When an error occurs you should use BoQunRowerFactory.[setRepairDirection](#setRepairDirection)(@RowerRepairDirection int direction) to fix the error





## RowerSportData



excercise time


getTime()

| meta   | description |
| ------ | ----------- |
| return | long        |



Paddle frequency per minute

getSpm()

| meta   | description |
| ------ | ----------- |
| return | int         |



Number of paddles

getStroke()

| meta   | description |
| ------ | ----------- |
| return | int         |



power

getWatt()

| meta   | description |
| ------ | ----------- |
| return | int         |



Movement distance, unit: (M)

getDistance()   

| meta   | description |
| ------ | ----------- |
| return | int         |



Exercise burns calories

getCalories()

| meta   | description |
| ------ | ----------- |
| return | int         |



How much time per 500 meters

getTimePer500m()

| meta   | description |
| ------ | ----------- |
| return | long        |



heart rate

getHeartRate()

| meta   | description |
| ------ | ----------- |
| return | int         |



<div id="RowerConfigInfo"/>
## RowerConfigInfo



Local WATT mode

##### isLocalWattMode()

| meta   | description |
| ------ | ----------- |
| return | boolean     |



with fan

##### hasFan()

| meta   | description |
| ------ | ----------- |
| return | boolean     |



Manual control

##### isManualControl()

| meta   | description |
| ------ | ----------- |
| return | boolean     |



least resistance

##### getMinLoadLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



maximum resistance

##### getMaxLoadLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



Minimum WATT

##### getMinWatt()

| meta   | description |
| ------ | ----------- |
| return | int         |



Max WATT

##### getMaxWatt()

| meta   | description |
| ------ | ----------- |
| return | int         |







<div id="RowerFactoryInfo"/>

## RowerFactoryInfo



diameter

##### getDiameter()

| meta   | description |
| ------ | ----------- |
| return | int         |



magnet count

##### getMagnet()

| meta   | description |
| ------ | ----------- |
| return | int         |



distance ratio

##### getDistance()

| meta   | description |
| ------ | ----------- |
| return | int         |



Calorie ratio

##### getCalories()

| meta   | description |
| ------ | ----------- |
| return | int         |



How much time to match per 500 meters

##### getTimePer500m()

| meta   | description |
| ------ | ----------- |
| return | int         |



<div id="RowerKeyCode"/>
## RowerKeyCode



start or pause

##### RowerKeyCode.KEY_START_PAUSE = 0x01



stop

##### RowerKeyCode.KEY_STOP = 0x02



resistance plus

##### RowerKeyCode.KEY_LOAD_UP = 0x03



resistance reduction

##### RowerKeyCode.KEY_LOAD_DOWN = 0x04



fan

##### RowerKeyCode.KEY_FAN = 0x05



