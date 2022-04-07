# 跑步机API




<div id="BoQunTreadmill"/>
## BoQunTreadmill







初始化跑步机

##### BoQunTreadmill.init()



查询跑步机配置信息，最大最小速度和扬升范围等等，回调[onResponseConfigInfo](#onResponseConfigInfo)，读取失败回调[onError](ErrorCode.md)

##### BoQunTreadmill.queryConfigInfo()



查询跑步机信息，回调[onResponseConfigInfo](#onResponseConfigInfo)

##### BoQunTreadmill.queryMachineInfo( int <u>type</u>)

type:

* BoQunTreadmill.TYPE_SPORT_STATUS   运动状态，回调[onResponseSportStatus](#onResponseSportStatus)
* BoQunTreadmill.TYPE_SPEED_AND_INCLINE 速度和扬升，回调[onResponseSpeedLevel](#onResponseSpeedLevel)和[onResponseInclineLevel](#onResponseInclineLevel)



开始运动，回调[onResponseSportStatus](#onResponseSportStatus)

##### BoQunTreadmill.start()



暂停运动，回调[onResponseSportStatus](#onResponseSportStatus)

##### BoQunTreadmill.pause()



停止运动，回调[onResponseSportStatus](#onResponseSportStatus)

##### BoQunTreadmill.stop()



CoolDown模式，回调[onResponseSportStatus](#onResponseSportStatus)和[onCoolDownStateChange](#onCoolDownStateChange)

##### BoQunTreadmill.coolDown()



设置跑步机速度，回调[onResponseSpeedLevel](#onResponseSpeedLevel)

##### BoQunTreadmill.setSpeedLevel( int <u>speed</u>)

speed 1= 0.1公里或英里



设置跑步机扬升，回调[onResponseInclineLevel](#onResponseInclineLevel)

##### BoQunTreadmill.setInclineLevel( int incline)



设置风扇风力级别，回调[onResponseFanLevel](#onResponseFanLevel)

##### BoQunTreadmill.setFanLevel(int level)

风力级别支持0-3段，机台没有风扇则不支持调整，获取机台是否有风扇状态[TreadmillConfigInfo](#TreadmillConfigInfo)





设置下位机工作模式

##### BoQunTreadmill.setWorkMode(@TreadmillWorkMode int mode)

mode:

- TreadmillWorkMode.NORMAL   TFT屏幕亮屏时应设置该状态,进入工作状态
- TreadmillWorkMode.SLEEP         TFT屏幕熄屏时应设置该状态,进入休眠模式
- TreadmillWorkMode.SHUT_DOWN     TFT关机时应设置该状态,释放资源



设置跑步机监听器

##### BoQunTreadmill.setOnTreadmillListener(OnTreadmillListener l)



启用和禁用串口，默认是启用状态

##### BoQunTreadmill.setSerialPortEnabled(boolean enable)

提供此方法是方便处理特殊情况，比如多个APP同时读取串口会造成互相干扰问题，使用此方法可避免

tips：并不会真正关闭串口，但绝对不会读取串口资料



注册状态回调监听器

##### BoQunTreadmill.registerStateListener(TreadmillStatusCallback callback)



解除注册状态回调监听器

##### BoQunTreadmill.unregisterStateListener(TreadmillStatusCallback callback)



解除所有注册状态回调监听器

##### BoQunTreadmill.unregisterAllStateListener()



销毁实例，释放资源

##### BoQunTreadmill.destroy()





## TreadmillStatusCallback



这是一个接口类，跑步机状态变化和运动状态变化回调

```
void onTreadmillSportStateChange(int state);

void onTreadmillStateChange(int state,int speed);
```




<div id="TreadmillStatusCallbacks"/>
## TreadmillStatusCallbacks

​       这个是类主要实现一些抽象类监听状态回调，目前支持安全Key状态监听,CoolDown模式监听，无人运动监听，后续有需求再实现其它功能或者你可以继承TreadmillStatusCallback接口实现自定义状态回调



目前实现有FMTS开关状态回调

```java
//安全KEY状态监听
BoQunTreadmill.registerStateListener(new TreadmillStatusCallbacks.SafetyKeyStatusCallback() {
       @Override
       public void onSafetyKeyStatus(boolean normal) {
            //normal==true //安全Key插入
            //normal==false //安全Key拔出
       }
});
//CoolDown模式监听
BoQunTreadmill.registerStateListener(new TreadmillStatusCallbacks.CoolDownStatusCallback() {
       /**
        * status:
        
        * CoolDownState.START    COOL DOWN模式开始减速
        * CoolDownState.ING      减速中 speed值会越来越小
        * CoolDownState.END      COOL DOWN模式结束
        *
        * speed:实时速度
        */
       @Override
       public void onCoolDownStatus(int status, int speed) {
          
       }
});

//无人运动监听
long detectionTime=45;//侦测无人运动时间，单位：秒

BoQunTreadmill.registerStateListener(
    new TreadmillStatusCallbacks.UnmannedStateDetectionCallback(detectionTime) {
       @Override
       public void onUnmannedStateDetection(boolean isUnmanned, long time) {
           //isUnmanned 当前是否是无人运动,当无人运动时间超过侦测时间就会变成true
           //time 开始正数无人运动时间
       }
});
```

记要解除注册

```
BoQunTreadmill.unregisterStateListener(xxxx);

//或者,看个人应用场景和需求
BoQunTreadmill.unregisterAllStateListener();
```




<div id="OnTreadmillListener"/>
## OnTreadmillListener



<div id="onResponseConfigInfo"/>

回复下控配置信息

##### void onResponseConfigInfo([TreadmillConfigInfo](#TreadmillConfigInfo) info)



<div id="onResponseSportStatus"/>

回复运动状态

##### void onResponseSportStatus(@TreadmillSportState int state)

status：

- TreadmillSportState.STOP   停止状态
- TreadmillSportState.START 开始状态
- TreadmillSportState.PAUSE 暂停状态
- TreadmillSportState.COOL_DOWN  在COOL DONW模式
- TreadmillSportState.ERROR   发生错误


<div id="onResponseSportData"/>
回复运动资料

##### void onResponseSportData(int heartRate, int speed)

heartRate ：心率

speed：实时速度


<div id="onResponseSpeedLevel"/>
回复下控速度等级

##### void onResponseSpeedLevel(int speed)


<div id="onResponseInclineLevel"/>
回复下控扬升等级

##### void onResponseInclineLevel(int incline)


<div id="onResponseFanLevel"/>
回复风扇风力级别

##### void onResponseFanLevel(int level)


<div id="onExternalKeyEvent"/>
面板外部键按下（UP,DOWN部分按钮可长按）触发回调，回复[TreadmillKeyCode](#TreadmillKeyCode) 

##### void onExternalKeyEvent(@TreadmillKeyCode int keyCode, int value)


<div id="onError"/>
发生错误回调[ErrorCode](ErrorCode.md)

##### void onError(int errorCode)








<div id="BoQunTreadmillFactory"/>
## BoQunTreadmillFactory



实例化跑步机工厂

##### BoQunTreadmillFactory.init()



查询跑步机工厂信息,回调[onResponseFactoryInfo](#onResponseFactoryInfo)

##### BoQunTreadmillFactory.queryFactoryInfo()



设置跑步机工厂信息

##### BoQunTreadmillFactory.setFactoryInfo(int code, int value)



开始自动校正,回调[onResponseMotorAutoCorrection](#onResponseMotorAutoCorrection)

##### BoQunTreadmillFactory.startAutoCorrection()



停止自动校正,回调[onResponseMotorAutoCorrection](#onResponseMotorAutoCorrection)

##### BoQunTreadmillFactory.stopAutoCorrection()



跑步机工厂监听器

##### BoQunTreadmillFactory.setOnTreadmillFactoryListener(OnTreadmillFactoryListener listener)



销毁跑步机工厂实例

##### BoQunTreadmillFactory.destroy()




<div id="OnTreadmillFactoryListener"/>
## OnTreadmillFactoryListener


<div id="onResponseFactoryInfo"/>
查询工厂信息回调

##### void onResponseFactoryInfo(TreadmillFactoryInfo info)

<div id="onResponseMotorAutoCal"/>
自动校正回调

##### void onResponseMotorAutoCorrection(@AutoCorrectionState int status, int speed, int adc, int inclineVR)




<div id="TreadmillConfigInfo"/>
## TreadmillConfigInfo



获取WATT 组别

##### getWattGroup()

| meta   | description |
| ------ | ----------- |
| return | int         |



获取最小扬升

##### getMinInclineLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



获取最大扬升

##### getMaxInclineLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



获取最小速度

##### getMinSpeedLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



获取最大速度

##### getMaxSpeedLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



获取速度增量，加减速度时，应该用当前加或减getChipSpeedLevel()

##### getChipSpeedLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



是否有扬升

##### hanIncline()

| meta   | description |
| ------ | ----------- |
| return | boolean     |



是否有风扇

##### hasFan()

| meta   | description |
| ------ | ----------- |
| return | boolean     |





<div id="TreadmillKeyCode"/>
## TreadmillKeyCode



开始或暂停

##### TreadmillKeyCode.KEY_START_PAUSE = 0x01



停止

##### TreadmillKeyCode.KEY_STOP = 0x02



风扇

##### TreadmillKeyCode.KEY_FAN = 0x03



速度加

##### TreadmillKeyCode.KEY_SPEED_UP = 0x04



速度减

##### TreadmillKeyCode.KEY_SPEED_DOWN = 0x05



扬升加

##### TreadmillKeyCode.KEY_INCLINE_UP = 0x06



扬升减

##### TreadmillKeyCode.KEY_INCLINE_DOWN = 0x07



COOL_DOWN

##### TreadmillKeyCode.KEY_COOL_DOWN = 0x08



音量加

##### TreadmillKeyCode.KEY_VOLUME_UP = 0x09



音量减

##### TreadmillKeyCode.KEY_VOLUME_DOWN = 0x10



速度调整快速键

##### TreadmillKeyCode.KEY_FAST_SPEED = 0x1A



扬升调整快速键

##### TreadmillKeyCode.KEY_FAST_INCLINE = 0x1B



旋钮正转

##### TreadmillKeyCode.KEY_TURN_KNOB_FORWARD = 0x1C



旋钮反转

##### TreadmillKeyCode.KEY_TURN_KNOB_REVERSE = 0x1D



返回键（可以自定义功能）

##### TreadmillKeyCode.KEY_BACK = 0x1E

