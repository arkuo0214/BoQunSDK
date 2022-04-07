# 划船机API



<div id="BoQunRower"/>

## BoQunRower



实例化划船机

##### BoQunRower.init()



查询划船机配置信息阻力，风扇状态，等等,回调[onResponseConfigInfo](#onResponseConfigInfo)，读取失败回调[onError](ErrorCode.md)

##### BoQunRower.queryConfigInfo()



查询划船机信息

##### BoQunRower.queryMachineInfo(int type)

type：

- BoQunRower.TYPE_SPORT_STATUS    运动状态，回调[onResponseSportStatus](#onResponseSportStatus)
- BoQunRower.TYPE_LOAD_LEVEL         阻力等级，回调[onResponseLoadLevel](#onResponseLoadLevel)



开始运动，回调[onResponseSportStatus](#onResponseSportStatus)

##### BoQunRower.start()



暂停运动，回调[onResponseSportStatus](#onResponseSportStatus)

##### BoQunRower.pause()



停止运动，回调[onResponseSportStatus](#onResponseSportStatus)

##### BoQunRower.stop()



控制划船机车阻力级别,回调[onResponseLoadLevel](#onResponseLoadLevel)

##### BoQunRower.setLoadLevel(int level)

level数值越大阻力越大，level有范围限制，level范围参数读取 [RowerConfigInfo](#RowerConfigInfo)



控制风扇风力级别,回调[onResponseFanLevel](#onResponseFanLevel)

##### BoQunRower.setFanLevel(int level)

风力级别支持0-3段，机台没有风扇则不支持调整，获取机台是否有风扇状态[RowerConfigInfo](#RowerConfigInfo)



设置划船机下位机工作模式

##### BoQunRower.setWorkMode(@RowerWorkMode int mode)

mode:

- RowerWorkMode .NORMAL   TFT屏幕亮屏时应设置该状态,进入工作状态
- RowerWorkMode .SLEEP         TFT屏幕熄屏时应设置该状态,进入休眠模式
- RowerWorkMode .SHUT_DOWN     TFT关机时应设置该状态,释放资源



划船机监听器

##### BoQunRower.setOnRowerListener(OnRowerListener onRowerListener)



启用和禁用串口，默认是启用状态

##### BoQunRower.setSerialPortEnabled(boolean enable)

提供此方法是方便处理特殊情况，比如多个APP同时读取串口会造成互相干扰问题，使用此方法可避免

tips：并不会真正关闭串口，但绝对不会读取串口资料



销毁实例，释放资源

##### BoQunRower.destroy()






<div id="OnRowerListener"/>
## OnRowerListener




<div id="onResponseConfigInfo"/>

回复下控配置信息


##### void onResponseConfigInfo([RowerConfigInfo](#RowerConfigInfo) info)




<div id="onResponseSportStatus"/>

回复运动状态


##### void onResponseSportStatus(@RowerSportState int status)

status：

- RowerSportState .STOP   停止状态
- RowerSportState .START 开始状态
- RowerSportState .PAUSE 暂停状态




<div id="onResponseSportData"/>

回复运动资料

##### void onResponseSportData([RowerSportData](#RowerSportData) data)




<div id="onResponsePullAndPut"/>

回复拉放状态及进度值


##### void onResponsePullAndPut(@IntRange(from = 0, to = 100) int progress, boolean isPull)

progress：拉放行程百分比

isPull  = true   拉 ，isPull  = false   放 




<div id="onResponseLoadLevel"/>

回复阻力等级


##### void onResponseLoadLevel(int load)




<div id="onResponseFanLevel"/>

回复风扇风力级别


##### void onResponseFanLevel(int level)




<div id="onExternalKeyEvent"/>

面板外部键按下（UP,DOWN部分按钮可长按）触发回调，回复[RowerKeyCode](#RowerKeyCode) 


##### void onExternalKeyEvent(@RowerKeyCode int keyCode)





发生错误回调[ErrorCode](ErrorCode.md)

##### void onError(int errorCode)






<div id="BoQunRowerFactory"/>
## BoQunRowerFactory





实例化划船机工厂

##### BoQunRowerFactory.init()



查询划船机工厂信息，回调[onResponseFactoryInfo](#onResponseFactoryInfo)

##### BoQunRowerFactory.queryFactoryInfo()



查询马达行程，回调[onResponseLoadMotorStroke](#onResponseLoadMotorStroke)

##### BoQunRowerFactory.queryLoadMotorStroke(int load)



设置马达行程

##### BoQunRowerFactory.setLoadMotorStroke(int load, int adc)




<div id="setRepairDirection"/>
修复马达错误

##### BoQunRowerFactory.setRepairDirection(@RowerRepairDirection int direction)

direction：

- RowerRepairDirection.UP     修复上方
- RowerRepairDirection.DOWN  修复下方



修改划船机工厂信息

##### BoQunRowerFactory.setFactoryInfo(RowerFactoryInfo info)



划船机工厂监听器

##### BoQunRowerFactory.setOnRowerFactoryListener(OnRowerFactoryListener listener)



销毁工厂模式实例

##### BoQunRowerFactory.destroy()






<div id="OnRowerFactoryListener"/>
## OnRowerFactoryListener 



回复工厂信息

##### void onResponseFactoryInfo([RowerFactoryInfo](#RowerFactoryInfo ) info)



回复马达行程

##### void onResponseLoadMotorStroke(int load, int adc)



回复马达状态

##### void onResponseMotorStatus(int status)

status：

- RowerMotorStatus.NORMAL    正常
- RowerMotorStatus.ERROR_UP     上方错误
- RowerMotorStatus.ERROR_DOWN  下方错误

当发生错误时应使用 BoQunRowerFactory.[setRepairDirection](#setRepairDirection)(@RowerRepairDirection int direction) 修复错误





## RowerSportData



运动时间


getTime()

| meta   | description |
| ------ | ----------- |
| return | long        |



每分钟桨频

getSpm()

| meta   | description |
| ------ | ----------- |
| return | int         |



划桨次数

getStroke()

| meta   | description |
| ------ | ----------- |
| return | int         |



功率

getWatt()

| meta   | description |
| ------ | ----------- |
| return | int         |



运动距离，单位:（M）

getDistance()   

| meta   | description |
| ------ | ----------- |
| return | int         |



运动消耗卡路里

getCalories()

| meta   | description |
| ------ | ----------- |
| return | int         |



每500米多少时间

getTimePer500m()

| meta   | description |
| ------ | ----------- |
| return | long        |



心率

getHeartRate()

| meta   | description |
| ------ | ----------- |
| return | int         |



<div id="RowerConfigInfo"/>
## RowerConfigInfo



本地WATT模式

##### isLocalWattMode()

| meta   | description |
| ------ | ----------- |
| return | boolean     |



有风扇

##### hasFan()

| meta   | description |
| ------ | ----------- |
| return | boolean     |



手动控制

##### isManualControl()

| meta   | description |
| ------ | ----------- |
| return | boolean     |



最小阻力

##### getMinLoadLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



最大阻力

##### getMaxLoadLevel()

| meta   | description |
| ------ | ----------- |
| return | int         |



最小WATT

##### getMinWatt()

| meta   | description |
| ------ | ----------- |
| return | int         |



最大WATT

##### getMaxWatt()

| meta   | description |
| ------ | ----------- |
| return | int         |







<div id="RowerFactoryInfo"/>

## RowerFactoryInfo



直径

##### getDiameter()

| meta   | description |
| ------ | ----------- |
| return | int         |



磁石

##### getMagnet()

| meta   | description |
| ------ | ----------- |
| return | int         |



距离配比

##### getDistance()

| meta   | description |
| ------ | ----------- |
| return | int         |



卡路里配比

##### getCalories()

| meta   | description |
| ------ | ----------- |
| return | int         |



每500米多少时间配比

##### getTimePer500m()

| meta   | description |
| ------ | ----------- |
| return | int         |



<div id="RowerKeyCode"/>
## RowerKeyCode



开始或暂停

##### RowerKeyCode.KEY_START_PAUSE = 0x01



停止

##### RowerKeyCode.KEY_STOP = 0x02



阻力加

##### RowerKeyCode.KEY_LOAD_UP = 0x03



阻力减

##### RowerKeyCode.KEY_LOAD_DOWN = 0x04



风扇

##### RowerKeyCode.KEY_FAN = 0x05



