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
    	implementation 'com.boqun:serialport:1.0.0'
    }
    
如果出现 unable to resolve dependency for app@...... 看能不能访问https://raw.githubusercontent.com 不能就在C:\Windows\System32\drivers\etc路径下找到hosts文件  

添加 以下内容并保存即可访问 199.232.68.133 raw.githubusercontent.com  
  
  
# 接口及方法使用說明:  
## **(API使用詳情請參考SerialPortDemo.zip)**  
  
基本  
  


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

工廠設定  


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
	


