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
    	implementation 'com.boqun:mobisdk:1.0.6'
    }
    
如果出现 unable to resolve dependency for app@...... 看能不能访问https://raw.githubusercontent.com 不能就在C:\Windows\System32\drivers\etc路径下找到hosts文件  

添加 以下内容并保存即可访问 199.232.68.133 raw.githubusercontent.com  
  
  
# 接口及方法使用說明:  
## **(API使用詳情請參考MoBiSDKDemo.zip https://github.com/arkuo0214/BoQunSDK/raw/master/repository/com/boqun/mobisdk/MoBiSDKDemo.zip)**
    跑步機:
    //初始化(初始化完成後會自動開啟串口)
    MoBiTreadmill.init(context, callback);
    
    //設定速度及揚升
    MoBiTreadmill.setInclineAndSpeed();
    
    //設定運動狀態及模式
    MoBiTreadmill.setSportModeAndStatus();
    
    //銷毀
    MoBiBike.destroy();
    
    //資料回調函數
    OnTreadmillDataCallback();
        //按鍵
        onExternalKeyEvent(int action, int keyCode)
        //狀態及心跳
        onStateChange(boolean isRefueling, boolean isLackOil, boolean isECOStatus, boolean isFactoryMode, int heartbeat)
        //錯誤碼
        onError(int error)
        //版本
        onReadVersion(int downControlVersion, int transferBoardVersion)
        //跑步机加油的里程
        onFuelMileageChange(int fuelMileage)
        //跑步机加油时间
        onRefuelingTimeChange(int refuelingTime)
        //马达电流值
        onMotorCurrentValue(float value)
        //马达电压值
        onMotorVoltageValue(int value)
        //步数
        onStepCountChange(int stepCount)
        //工程模式设置信息
        onFactoryModeSettingInfo(boolean isAutomaticShutdownEnable)
    
    
    
    
    腳踏車/划船機/橢圓機:
    //初始化(初始化完成後會自動開啟串口)
    MoBiBike.init(context, callback);
    
    //傳輸資料
    BoQunBike.sendPortMessage();
    
    //延遲傳輸資料
    BoQunBike.sendPortMessageDelay();
    
    //启用读取串行数据
    MoBiBike.enableRead();
    
    //禁用读取串行数据
    MoBiBike.disableRead();

    //銷毀
    MoBiBike.destroy();
    
    
    //資料回調函數
    OnBikeDataCallback();
    	//運動數據
    	onSportData(PortDataBean bean)
    		//运动设备类型
    		int equipmentType = bean.getEquipmentType();
    		//运动设备子类型
    		int equipmentSubType = bean.getEquipmentSubType();
    		//電池電量
    		int battery = bean.getBattery();
    		//传感信号间隔
    		long rpm = bean.getRpm();
    		//信号采集计数
    		long count = bean.getCount();
    		//阻力等级
    		int load = bean.getLoad();
    		//心率
    		int pulse = bean.getPulse();
    
