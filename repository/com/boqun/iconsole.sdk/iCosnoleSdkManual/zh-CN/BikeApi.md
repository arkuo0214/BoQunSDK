# 脚踏车API



<div id="BoQunBike"/>

## BoQunBike





实例化脚踏车

##### BoQunBike.init()





查询脚踏车配置信息阻力，扬升范围，状态，等等,回调[onResponseConfigInfo](#onResponseConfigInfo)，读取失败回调[onError](ErrorCode.md)

##### BoQunBike.queryConfigInfo()





查询脚踏车信息

##### BoQunBike.queryMachineInfo( int <u>type</u>)

type：

- BoQunBike.TYPE_SPORT_STATUS    运动状态，回调[onResponseSportStatus](#onResponseSportStatus)

- BoQunBike.TYPE_LOAD_LEVEL         阻力等级，回调[onResponseLoadLevel](#onResponseLoadLevel)





开始运动,开始成功之后回调[onResponseSportStatus](#onResponseSportStatus),开始传输数据[onResponseSportData](#onResponseSportData)

##### BoQunBike.start()





暂停运动,暂停成功之后回调[onResponseSportStatus](#onResponseSportStatus)，暂停状态期间不会传输运动数据

##### BoQunBike.pause()





停止运动,回调[onResponseSportStatus](#onResponseSportStatus)

##### BoQunBike.stop()





控制脚踏车阻力级别,回调[onResponseLoadLevel](#onResponseLoadLevel)

##### BoQunBike.setLoadLevel( int <u>load</u> )

load 数值越大阻力越大，load 有范围限制，load 范围参数读取 [BikeConfigInfo](#BikeConfigInfo)





控制脚踏车扬升级别,回调[onResponseInclineLevel](#onResponseInclineLevel)

##### BoQunBike.setInclineLevel( int <u>incline</u> )

incline 数值越大倾斜度越高，incline 有范围限制，incline 范围参数读取 [BikeConfigInfo](#BikeConfigInfo)





控制风扇风力级别,回调[onResponseFanLevel](#onResponseFanLevel)

##### BoQunBike.setFanLevel( int <u>level</u>)

风力级别支持0-3段，机台没有风扇则不支持调整，获取机台是否有风扇状态[BikeConfigInfo](#BikeConfigInfo)





设置脚踏车下位机工作模式

##### BoQunBike.setWorkMode( int <u>mode</u>)

mode:

- BikeWorkMode.NORMAL   TFT屏幕亮屏时应设置该状态,进入工作状态
- BikeWorkMode.SLEEP         TFT屏幕熄屏时应设置该状态,进入休眠模式
- BikeWorkMode.SHUT_DOWN     TFT关机时应设置该状态,释放资源





启用或关闭FMTS，须搭配带含有FMTS功能的下控板使用

##### BoQunBike.setFTMSEnabled( boolean <u>enable</u>)





启用和禁用串口，默认是启用状态

##### BoQunBike.setSerialPortEnabled( boolean <u>enable</u>)

提供此方法是方便处理特殊情况，比如多个APP同时读取串口会造成互相干扰问题，使用此方法可避免

tips：并不会真正关闭串口，但绝对不会读取串口资料



脚踏车监听器

##### BoQunBike.setBikeListener([OnBikeListener](#OnBikeListener) listener)



注册状态回调监听器

##### BoQunBike.registerStateListener(BikeStatusCallback callback)



解除注册状态回调监听器

##### BoQunBike.unregisterStateListener(BikeStatusCallback callback)



解除所有注册状态回调监听器

##### BoQunBike.unregisterAllStateListener()



销毁实例，释放资源

##### BoQunBike.destroy()





## BikeStatusCallback



脚踏车状态变化回调

##### void onBikeSportStateChange(int status)




<div id="BikeStatusCallbacks"/>
## BikeStatusCallbacks

​       这个是类主要实现一下状态回调，目前支持监听FTMS状态,后续有需求再实现其它功能或者你可以继承BikeStatusCallback接口实现自定义状态回调



目前实现有FMTS开关状态回调

```java
BoQunBike.registerStateListener(new BikeStatusCallbacks.FTMSStateCallback() {
            @Override
            public void onFTMSStateChange(boolean enable) {
                 //enable 启用和关闭状态
            }
        });
```

记要解除注册

```java
BoQunBike.unregisterStateListener(xxxx);

//或者,看个人应用场景和需求
BoQunBike.unregisterAllStateListener();
```





<div id="OnBikeListener"/>

## OnBikeListener



<div id="onResponseConfigInfo"/>

回复下控配置信息

##### void onResponseConfigInfo([BikeConfigInfo](#BikeConfigInfo) info)



<div id="onResponseSportStatus"/>

回复运动状态

##### void onResponseSportStatus(@BikeSportState int status)

status：

- BikeSportState.STOP   停止状态
- BikeSportState.START 开始状态
- BikeSportState.PAUSE 暂停状态



<div id="onResponseSportData"/>

回复运动资料

##### void onResponseSportData(int stepCount, int rpm, int heartRate)

stepCount：步数（累加值）

rpm：每分钟转速

heartRate：手握心跳



<div id="onResponseLoadLevel"/>

回复下控阻力等级

##### void onResponseLoadLevel(int load)



<div id="onResponseInclineLevel"/>

回复下控扬升等级

##### void onResponseInclineLevel(int incline)



<div id="onResponseFanLevel"/>

回复风扇风力级别

##### void onResponseFanLevel(int level)



<div id="onExternalKeyEvent"/>

面板外部键按下（UP,DOWN部分按钮可长按）触发回调，回复[BikeKeyCode](#BikeKeyCode) 

##### void onExternalKeyEvent([@BikeKeyCode](#BikeKeyCode) int keyCode)



<div id="onError"/>

发生错误回调[ErrorCode](ErrorCode.md)

##### void onError(int errorCode)





<div id="BoQunBikeFactory"/>
## BoQunBikeFactory





实例化脚踏车工厂

##### BoQunBikeFactory.init()



查询指定阻力等级的阻力马达行程,回调[onResponseLoadMotorStoke](#onResponseLoadMotorStoke)

##### BoQunBikeFactory.queryLoadMotorStroke( int load)



查询指定扬升等级的扬升马达行程,回调[onResponseInclineMotorStroke](#onResponseInclineMotorStroke)

##### BoQunBikeFactory.queryInclineMotorStroke( int incline)



设置机台轮径

##### BoQunBikeFactory.setWheelDiameter( int wheelDiameter)



设置指定阻力等级的阻力马达行程ADC值

##### BoQunBikeFactory.setLoadMotorStroke( int load, int adc)



设置指定扬升等级的扬升马达行程ADC值

##### BoQunBikeFactory.setInclineMotorStroke( int incline, int adc)



开始扬升马达自动校正，回调[onResponseInclineAutoCorrection](#onResponseInclineAutoCorrection)

##### BoQunBikeFactory.startInclineAutoCorrection()



开始扬升马达自动校正，回调[onResponseInclineAutoCorrection](#onResponseInclineAutoCorrection)

direction 校正方向

- AutoCorrectionDirection.AUTO 默认是自动方向
- AutoCorrectionDirection.UP
- AutoCorrectionDirection.DOWN

##### BoQunBikeFactory.startInclineAutoCorrection(@AutoCorrectionDirection int direction)



停止扬升马达自动校正，回调[onResponseInclineAutoCorrection](#onResponseInclineAutoCorrection)

##### BoQunBikeFactory.stopInclineAutoCorrection()



脚踏车工厂模式监听器

##### BoQunBikeFactory.setOnBikeFactoryListener( [OnBikeFactoryListener](#OnBikeFactoryListener) listener)



销毁实例，释放资源

##### BoQunBikeFactory.destroy()







<div id="OnBikeFactoryListener"/>
## OnBikeFactoryListener




<div id="onResponseLoadMotorStoke"/>
回复指定阻力等级的马达行程ADC

##### void onResponseLoadMotorStoke(int load, int adc)




<div id="onResponseInclineMotorStroke"/>
回复指定扬升等级的马达行程ADC

##### void onResponseInclineMotorStroke(int incline, int adc)




<div id="onResponseInclineAutoCal"/>
回复自动校正的状态和ADC值

##### void onResponseInclineAutoCorrection(@AutoCorrectionStateint state, int inclineADC)

state:

- AutoCorrectionState.CORRECTION_START  扬升马达校正开始
- AutoCorrectionState.CORRECTION_ING      扬升马达校正中
- AutoCorrectionState.CORRECTION_STOP   扬升马达校正停止

inclineADC:值范围0-255，扬升马达校正中ADC会不停的变化，正常情况是从小到大，从大到小为一次完整校正







<div id="BikeConfigInfo"/>

## BikeConfigInfo





##### getClientId()

获取客户ID，满足不同客户的定制化需求

| meta   | description |
| ------ | ----------- |
| return | int         |



##### getWattGroup()

获取瓦特组别

| meta   | description |
| ------ | ----------- |
| return | int         |




##### getWheelDiameter()

获取轮径

| meta   | description |
| ------ | ----------- |
| return | int         |



##### isManualControl()

是否为手动控制

| meta   | description |
| ------ | ----------- |
| return | boolean     |



##### getMinLoadLevel()

获取最小阻力等级

| meta   | description |
| ------ | ----------- |
| return | int         |



##### getMaxLoadLevel()

获取最大阻力等级

| meta   | description |
| ------ | ----------- |
| return | int         |




##### getNegativeInclineLevel()

获取负扬升等级

| meta   | description |
| ------ | ----------- |
| return | int         |




##### getMinInclineLevel()

获取最小扬升等级

| meta   | description |
| ------ | ----------- |
| return | int         |




##### getMaxInclineLevel()

获取最大扬升等级

| meta   | description |
| ------ | ----------- |
| return | int         |



##### hasIncline()

机台是否配置有扬升

| meta   | description |
| ------ | ----------- |
| return | boolean     |



##### hasFan()

机台是否配置风扇

| meta   | description |
| ------ | ----------- |
| return | boolean     |





##### hasFTMS()

机台是否配置FMTS功能

| meta   | description |
| ------ | ----------- |
| return | boolean     |





<div id="BikeKeyCode"/>

## BikeKeyCode



开始或暂停

##### BikeKeyCode.KEY_START_PAUSE = 0x01



停止

##### BikeKeyCode.KEY_STOP = 0x02



阻力加

##### BikeKeyCode.KEY_LOAD_UP = 0x03



阻力减

##### BikeKeyCode.KEY_LOAD_DOWN = 0x04



扬升加

##### BikeKeyCode.KEY_INCLINE_UP = 0x05



扬升减

##### BikeKeyCode.KEY_INCLINE_DOWN = 0x06



风扇

##### BikeKeyCode.KEY_FAN = 0x07



