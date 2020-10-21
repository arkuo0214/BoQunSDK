# 使用說明:  
增加  
\build.gradle  


    allprojects {
    	repositories {
    		maven {
    			url 'https://raw.githubusercontent.com/arkuo0214/BoQunSDK/master/repository'
    		}
    	}
    }
    

增加  
\app\build.gradle  


    dependencies {
    	implementation 'com.boqun:mobisdk:1.0.9'
    }
    
如果出现 unable to resolve dependency for app@...... 看能不能访问https://raw.githubusercontent.com 不能就在C:\Windows\System32\drivers\etc路径下找到hosts文件  

添加 以下内容并保存即可访问 199.232.68.133 raw.githubusercontent.com  
  
  
# 接口及方法使用說明:  
## **(API使用詳情請參考MoBiSDKDemo.zip https://github.com/arkuo0214/BoQunSDK/raw/master/repository/com/boqun/mobisdk/MoBiSDKDemo.zip)**
            MoBiDevice.init(mContext, new OnDeviceDataCallback() {
                @Override
                public void onInitData(InitDataBean initData) {
                    manufacturerName = initData.getManufacturerName();  //厂家名称ID
                    modelNumber = initData.getModelNumber();    //型号编号
                    hardwareRevision = initData.getHardwareRevision();  //硬件版本号
                    firmwareRevision = initData.getFirmwareRevision();  //固件版本号
                }

                @Override
                public void onDeviceData(DeviceDataBean deviceData) {
                    dataReportingMethod = deviceData.getDataReportingMethod();  //上报数据方式
                    deviceType = deviceData.getDeviceType();    //运动设备类型
                    deviceSubType = deviceData.getDeviceSubType();  //运动设备子类型
                    deviceControlType = deviceData.getDeviceControlType();  //电控设备类型
                    sensorSignalScale = deviceData.getSensorSignalScale();  //感应信号采集刻度
                    numberOfMagnets = deviceData.getNumberOfMagnets();  //磁石等被感应器件数量
                    battery = deviceData.getBattery();  //设备电量
                    resistanceMax = deviceData.getResistanceMax();  //阻力最大值
                    resistanceMin = deviceData.getResistanceMin();  //阻力最小值
                    resistanceMode = deviceData.getResistanceMode();    //阻力调节方式
                    speedRange = deviceData.getSpeedRange();    //跑步机速度范围
                    inclineRange = deviceData.getInclineRange();    //跑步机坡度范围
                }

                @Override
                public void onMachineStatus(MachineStatusBeen machineStatus) {
                    status = machineStatus.getMachineStatus();  //设备当前状态 ( 0 ：停止 1 开 始； 2 暂 停 )
                    machineEnterStateMethod = machineStatus.getMachineEnterStateMethod();   //设备进入当前状态的方式(0:物理按键; 1:App控制; 2:急停按键)
                }

                @Override
                public void onResistanceData(ResistanceDataBean resistanceData) {
                    resistance = resistanceData.getResistance();    //阻力档位
                }

                @Override
                public void onSignalTimeData(SignalTimeDataBean signalTimeData) {
                    signalTimeInterval = signalTimeData.getSignalTimeInterval();    //信号时间间隔
                    signalCount = signalTimeData.getSignalCount();  //信号计数
                }

                @Override
                public void onTreadmillSportData(TreadmillSportDataBean sportData) {
                    speed = sportData.getSpeed();   //速度
                    incline = sportData.getIncline();   //坡度
                    step = sportData.getStep(); //步频
                    time = sportData.getTime(); //时间
                    distance = sportData.getDistance(); //里程
                    calories = sportData.getCalories(); //热量
                }

                @Override
                public void onErrorCode(ErrorCodeBean errorCode) {
                    errorCodeHi = errorCode.getErrorCodeHi();   //错误代码高位
                    errorCodeLow = errorCode.getErrorCodeLow(); //错误代码低位
                }

                @Override
                public void onFailure(String msg) {

                }
            });
    
