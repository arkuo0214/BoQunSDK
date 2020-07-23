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
    	implementation 'com.boqun:xqportsdk:1.0.0'
    }
    
如果出现 unable to resolve dependency for app@...... 看能不能访问https://raw.githubusercontent.com 不能就在C:\Windows\System32\drivers\etc路径下找到hosts文件  

添加 以下内容并保存即可访问 199.232.68.133 raw.githubusercontent.com  
  
  
# 接口及方法使用說明:  
## **(API使用詳情請參考XQPortSDKDemo.zip https://github.com/arkuo0214/BoQunSDK/raw/master/repository/com/boqun/xqportsdk/XQPortSDKDemo.zip)**
    //初始化
    XQBike.init(this, new OnBikeDataListener());
    
    //資料回調函數
    OnBikeDataListener();
    
    	//初始化成功
    	//s = 設備編碼
    	public void onInitializationSuccess(String s)
	
    	//運動數據
		//i = watt 單車功率
		//i1 = rpm 單車輪轉速
		//i2 = level 單車阻力
    	public void onDataChange(int i, int i1, int i2)
        

