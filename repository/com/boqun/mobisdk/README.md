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
    	implementation 'com.boqun:mobisdk:1.0.2'
    }
    
如果出现 unable to resolve dependency for app@...... 看能不能访问https://raw.githubusercontent.com 不能就在C:\Windows\System32\drivers\etc路径下找到hosts文件  

添加 以下内容并保存即可访问 199.232.68.133 raw.githubusercontent.com  
  
  
# 接口及方法使用說明:  
## **(API使用詳情請參考MoBiSDKDemo.zip https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/mobisdk/MoBiSDKDemo.zip)**
    //初始化
    BoQunBike.init(this,PortDataCallback());
    
    //關閉
    BoQunBike.close();
    
    //銷毀
    BoQunBike.destroy();
    
    //傳輸資料(自動生成"偶检验和")
    BoQunBike.sendPortMessage("AB010000000000");
    
    //延遲傳輸資料(自動生成"偶检验和")
    BoQunBike.sendPortMessageDelay("AB010000000000",500);
    
    //資料回掉函數
    PortDataCallback();
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
    
