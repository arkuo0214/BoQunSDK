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
    	implementation 'com.boqun:serialport:1.0.7'
    }
    
如果出现 unable to resolve dependency for app@...... 看能不能访问https://raw.githubusercontent.com 不能就在C:\Windows\System32\drivers\etc路径下找到hosts文件  

添加 以下内容并保存即可访问 199.232.68.133 raw.githubusercontent.com  
  
  
# 接口及方法使用說明:  
## **(API使用詳情請參考SerialPortDemo.zip https://github.com/arkuo0214/BoQunSDK/raw/master/repository/com/boqun/serialport/SerialPortDemo.zip)**  
  
單車系列(基本)  
  


    //初始化 
    BoQunBike.init(this, callback);
    
    //啟動 
    BoQunBike.start();
    
    //設定阻力
    BoQunBike.setLoadValue(currentLoad);
    //延遲設定阻力
    BoQunBike.setLoadValue(currentIncline, 50);
    
    //設定揚升 
    BoQunBike.setInclineValue(currentIncline); 
    //延遲設定揚升 
    BoQunBike.setInclineValue(currentIncline, 100);
    
    //設定風扇 
    BoQunBike.setFan(currentFanLevel);
    
    //暫停 
    BoQunBike.pause();
    
    //停止 
    BoQunBike.stop();
    
    //屏幕開關設定喚醒和睡眠(可參考SerialPortDemo.zip範例)
    ScreenBroadcast.getInstance().register(this).listener(new ScreenBroadcast.Listener() {
        @Override
        public void onScreenOn() {
            Log.e(TAG, "onScreenOn");
            BoQunBike.setSleepState(SleepState.WAKE);
        }

        @Override
        public void onScreenOff() {
            Log.e(TAG, "onScreenOff");
            BoQunBike.setSleepState(SleepState.SLEEP);
        }
    });

單車系列(工廠設定)  


    //初始化工廠設定
    BoQunBike.getFactory().init(FactoryDataCallback());
	
    //退出工廠設定
    BoQunBike.getFactory().exit();
	
    //保存輪徑
    BoQunBike.getFactory().saveWheelDiameter(wheelDiameter);
	
    //設定馬達行程
    BoQunBike.getFactory().setMotorStrokeLoad(motorStrokeLoadValue);
	
    //保存馬達行程
    BoQunBike.getFactory().saveMotorStroke(motorStrokeLoadValue, motorStrokeAdcValue);
	
    //設定揚升行程
    BoQunBike.getFactory().setInclineStrokeLoad(inclineStrokeLoadValue);
	
    //保存揚升行程
    BoQunBike.getFactory().saveInclineStroke(inclineStrokeLoadValue, inclineStrokeAdcValue);
	
    //開始自動校正
    BoQunBike.getFactory().startAutoCorrection(OnAutoCorrectListener());
	
    //強制停止自動校正
    BoQunBike.getFactory().stopAutoCorrection();
	

跑步機系列(基本)  
  


    //初始化 
    BoQunTreadmill.init(this, callback);
    
    //啟動 
    BoQunTreadmill.start();
    
    //設定速度
    BoQunTreadmill.setCurrentSpeed(currentLoad);
    //延遲設定速度
    BoQunTreadmill.setCurrentSpeed(currentIncline, 50);
    
    //設定揚升 
    BoQunTreadmill.setCurrentIncline(currentIncline); 
    //延遲設定揚升 
    BoQunTreadmill.setCurrentInline(currentIncline, 100);
    
    //設定風扇 
    BoQunTreadmill.setFan(currentFanLevel);
    
    //暫停 
    BoQunTreadmill.pause();
    
    //停止 
    BoQunTreadmill.stop();
    
    //屏幕開關設定喚醒和睡眠(可參考SerialPortDemo.zip範例)
    ScreenBroadcast.getInstance().register(this).listener(new ScreenBroadcast.Listener() {
        @Override
        public void onScreenOn() {
            Log.e(TAG, "onScreenOn");
            BoQunBike.setSleepState(SleepState.WAKE);
        }

        @Override
        public void onScreenOff() {
            Log.e(TAG, "onScreenOff");
            BoQunBike.setSleepState(SleepState.SLEEP);
        }
    });

跑步機系列(工廠設定)  


    //初始化工廠設定
    BoQunTreadmill.getFactory().init(FactoryDataCallback());
	
    //退出工廠設定
    BoQunTreadmill.getFactory().exit();
	
    //轮径
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.WHEEL_DIAMETER, wheelDiameter);

    //揚升VR最高值
    public void setMaxInclineVRValue(int maxInclineVRValue) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MAX_INCLINE_VR, maxInclineVRValue);
    }

    //揚升VR最低值
    public void setMinInclineVRValue(int minInclineVRValue) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MIN_INCLINE_VR, minInclineVRValue);
    }

    //最高速度
    public void setMaxSpeedValue(int maxSpeedValue) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MAX_SPEED, maxSpeedValue);
    }

    //最低速度
    public void setMinSpeedValue(int minSpeedValue) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MIN_SPEED, minSpeedValue);
    }

    //速度增量
    public void setSpeedIncrementValue(int speedIncrementValue) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.CHILD_SPEED, speedIncrementValue);
    }

    //揚升開關
    public void setInclineSwitch(int inclineSwitch) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.INCLINE_SWITCH, inclineSwitch);
    }

    //揚升最大段
    public void setMaxInclineValue(int maxInclineValue) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MAX_INCLINE, maxInclineValue);
    }

    //負揚升 /	揚升最低段
    public void setMinInclineValue(int minInclineValue) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MIN_INCLINE, minInclineValue);
    }

    //馬達起始 pulse
    public void setMotorStartPulse(int motorStartPulse) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MOTOR_INIT_PULSE, motorStartPulse);
    }

    //1公里電壓值
    public void setKm1VoltageValue(int km1VoltageValue) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.ONE_KM_VOLTAGE, km1VoltageValue);
    }

    //10公里電壓值
    public void setKm10VoltageValue(int km10VoltageValue) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.TEN_KM_VOLTAGE, km10VoltageValue);
    }

    //滾筒皮帶輪/馬達皮帶輪*50=光感配比
    public void setLightPerceptionRatio(int lightPerceptionRatio) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.LIGHT_PERCEPTION_RATIO, lightPerceptionRatio);
    }

    //扭力值
    public void setTorqueValue(int torqueValue) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.TORQUE, torqueValue);
    }

    //線電流值
    public void setLineCurrentValue(int lineCurrentValue) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.LINE_CURRENT, lineCurrentValue);
    }

    //馬達停止模式
    public void setMotorStopMode(int motorStopMode) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MOTOR_STOP_MODE, motorStopMode);
    }

    //揚升時間
    public void setInclineTime(int inclineTime) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.INCLINE_TIME, inclineTime);
    }

    //感應方式
    public void setInductionMethod(int inductionMethod) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.INDUCTION_METHOD, inductionMethod);
    }

    //公英里切換
    public void setMileSwitch(int mileSwitch) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MILE_SWITCH, mileSwitch);
    }

    //心跳接收優先參數
    public void setPA_PB(int PA_PB) {
        BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.PA_PB, PA_PB);
    }	
    //開始自動校正
    BoQunBike.getFactory().startAutoCorrection(OnAutoCorrectListener());
	
    //強制停止自動校正
    BoQunBike.getFactory().stopAutoCorrection();
	


