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
    	implementation 'com.boqun:serialport:1.0.9'
    }
    
如果出现 unable to resolve dependency for app@...... 看能不能访问https://raw.githubusercontent.com 不能就在C:\Windows\System32\drivers\etc路径下找到hosts文件  

添加 以下内容并保存即可访问 199.232.68.133 raw.githubusercontent.com  
  
  
# 接口及方法使用說明:  
## **(API使用詳情請參考SerialPortDemo.zip https://github.com/arkuo0214/BoQunSDK/raw/master/repository/com/boqun/serialport/SerialPortDemo.zip)**  
![image](https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/serialport/images/demo1.png)
  
單車系列(基本)  
![image](https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/serialport/images/demo1_bike.jpg)
  


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
    

單車系列(工廠設定)  
![image](https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/serialport/images/demo1_bike2.jpg)


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
![image](https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/serialport/images/demo1_treadmill.jpg)
  


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
    

跑步機系列(工廠設定)  
![image](https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/serialport/images/demo1_treadmill2.jpg)


    //初始化工廠設定
    BoQunTreadmill.getFactory().init(FactoryDataCallback());
	
    //退出工廠設定
    BoQunTreadmill.getFactory().exit();
	
    //轮径
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.WHEEL_DIAMETER, wheelDiameter);

    //揚升VR最高值
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MAX_INCLINE_VR, maxInclineVRValue);

    //揚升VR最低值
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MIN_INCLINE_VR, minInclineVRValue);

    //最高速度
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MAX_SPEED, maxSpeedValue);

    //最低速度
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MIN_SPEED, minSpeedValue);

    //速度增量
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.CHILD_SPEED, speedIncrementValue);

    //揚升開關
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.INCLINE_SWITCH, inclineSwitch);

    //揚升最大段
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MAX_INCLINE, maxInclineValue);

    //負揚升 /	揚升最低段
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MIN_INCLINE, minInclineValue);

    //馬達起始 pulse
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MOTOR_INIT_PULSE, motorStartPulse);

    //1公里電壓值
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.ONE_KM_VOLTAGE, km1VoltageValue);

    //10公里電壓值
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.TEN_KM_VOLTAGE, km10VoltageValue);

    //滾筒皮帶輪/馬達皮帶輪*50=光感配比
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.LIGHT_PERCEPTION_RATIO, lightPerceptionRatio);

    //扭力值
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.TORQUE, torqueValue);

    //線電流值
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.LINE_CURRENT, lineCurrentValue);

    //馬達停止模式
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MOTOR_STOP_MODE, motorStopMode);

    //揚升時間
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.INCLINE_TIME, inclineTime);

    //感應方式
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.INDUCTION_METHOD, inductionMethod);

    //公英里切換
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.MILE_SWITCH, mileSwitch);

    //心跳接收優先參數
    BoQunTreadmill.getFactory().setFactoryParams(FactoryParams.PA_PB, PA_PB);
    
    //開始自動校正
    BoQunTreadmill.getFactory().startAutoCorrection();
	
    //強制停止自動校正
    BoQunTreadmill.getFactory().stopAutoCorrection();
	

划船機系列(基本)  
![image](https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/serialport/images/demo1_rower.png)

    /**
     * You need to call this method to initialize when using the rowing machine,
     * otherwise the rowing machine cannot be used
     *
     * @param context
     * @param listener {@link OnRowerDataListener}
     * @throws Exception
     */
    BoQunRower.getInstance().init(Context context, OnRowerDataListener listener);

    /**
     * Notify the start of the control
     */
    BoQunRower.getInstance().start();

    /**
     * Notification of suspension of control
     */
    BoQunRower.getInstance().pause();

    /**
     * Notify the control stop
     */
    BoQunRower.getInstance().stop();

    /**
     * Ask the current load level
     */
    BoQunRower.getInstance().queryLoadLevel();

    /**
     * Delay asking the current resistance level
     *
     * @param delayMillis
     */
    BoQunRower.getInstance().queryLoadLevelDelay(long delayMillis);

    /**
     * Set resistance level
     *
     * @param level
     */
    BoQunRower.getInstance().setLoadLevel(int level);

    /**
     * Delay in setting the resistance level
     *
     * @param level       Load class
     * @param delayMillis
     */
    BoQunRower.getInstance().setLoadLevel(int level, long delayMillis);

    /**
     * Set fan level
     *
     * @param level
     */
    BoQunRower.getInstance().setFanLevel(int level);

    /**
     * Delay in setting the fan level
     *
     * @param level
     * @param delayMillis
     */
    BoQunRower.getInstance().setFanLevel(int level, long delayMillis);

    /**
     * Set down control working mode
     *
     * @param mode {@link RowerWorkMode}
     */
    BoQunRower.getInstance().setWorkMode(@RowerWorkMode int mode);


    /**
     * Enable serial port reading, the serial port will start to read data
     */
    BoQunRower.getInstance().enableRead();

    /**
     * Disable serial port reading, the serial port will stop reading
     */
    BoQunRower.getInstance().disableRead();

    /**
     * Destroy, close the serial port and clear the listener
     */
    BoQunRower.getInstance().destroy();
    

划船機系列(工廠設定)  
![image](https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/serialport/images/demo1_rower2.png)

    /**
     * Enter factory mode
     * <p>
     * Query various parameters of factory mode
     * <p>
     * Ask the ADC value of the first load
     *
     * @param listener {@link OnFactoryListener}
     */
    BoQunRowerFactory.getInstance().init(OnFactoryListener listener);

    /**
     * Query the specified load stroke of the motor
     *
     * @param load Specified load
     * @
     */
    BoQunRowerFactory.getInstance().queryMotorLoadStroke(int load);

    /**
     * Save motor stroke
     *
     * @param load
     * @param adc
     */
    BoQunRowerFactory.getInstance().saveMotorStroke(int load, int adc);

    /**
     * Query various parameters of factory mode
     */
    BoQunRowerFactory.getInstance().queryVariousParams();

    /**
     * Query various parameters of factory mode
     *
     * @param delayMillis Delayed query
     */
    BoQunRowerFactory.getInstance().queryVariousParams(long delayMillis);

    /**
     * Use this method to save parameters when modifying down control parameters
     *
     * @param diameter
     * @param magnet
     * @param distance
     * @param calories
     * @param per500mTime
     */
    BoQunRowerFactory.getInstance().saveParameters(int diameter, int magnet, int distance, int calories, int per500mTime);

    /**
     * Use this method to repair the motor when an E 2 error occurs
     *
     * @param direction
     */
    BoQunRowerFactory.getInstance().setRepairMotorDirection(@Direction int direction);

    /**
     * Exit factory mode to release resources
     */
    BoQunRowerFactory.getInstance().exit();


    @IntDef({Status.NORMAL, Status.E2})
    @Retention(RetentionPolicy.SOURCE)
    public @interface Status {

        int NORMAL = 0;

        /**
         * An error occurred in the lower control motor
         */
        int E2 = 1;

    }

    @IntDef({Direction.KEEP, Direction.UP, Direction.DOWN})
    @Retention(RetentionPolicy.SOURCE)
    public @interface Direction {
        /**
         * Stay the same, no need to fix
         */
        int KEEP = 0;

        /**
         * The motor has an error and repair it upwards
         */
        int UP = 1;

        /**
         * Motor error occurs downward repair
         */
        int DOWN = 2;

    }
