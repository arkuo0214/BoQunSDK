# Operation guide:  
Add  
\build.gradle  


    allprojects {
    	repositories {
    		maven {
    			url 'https://raw.githubusercontent.com/arkuo0214/BoQunSDK/master/repository'
    		}
    	}
    }
    

Add  
\app\build.gradle  


    dependencies {
    	implementation 'com.boqun:xqportsdk:1.0.0'
    }
    
If appear “unable to resolve dependency for app@......”, please check have you can access “https://raw.githubusercontent.com”, if you cannot access, please find the hosts document in C:\Windows\System32\drivers\etc , then add “199.232.68.133 raw.githubusercontent.com” and save.
  
  
# Operation guide:  
## **(API operation guide refer XQPortSDKDemo.zip https://github.com/arkuo0214/BoQunSDK/raw/master/repository/com/boqun/xqportsdk/XQPortSDKDemo.zip)**
    //initialize
    XQBike.init(this, new OnBikeDataListener());
    
    //Data callback
    OnBikeDataListener() {
	
    	//initialize success
    	//s = Equipment number
    	public void onInitializationSuccess(String s)
	
    	//Workout data
		//i = watt : Bike Power
		//i1 = rpm : Bike RPM(Revolutions Per minute)
		//i2 = level : Bike Resistance
    	public void onDataChange(int i, int i1, int i2)
	}

