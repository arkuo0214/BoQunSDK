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
    	implementation 'com.boqun:screensender:1.0.0'
    }
    
如果出现 unable to resolve dependency for app@...... 看能不能访问https://raw.githubusercontent.com 不能就在C:\Windows\System32\drivers\etc路径下找到hosts文件  

添加 以下内容并保存即可访问 199.232.68.133 raw.githubusercontent.com 
  
  
# 接口及方法使用說明:  
## **(API使用詳情請參考VrRpmSerialPortDemo.zip https://github.com/arkuo0214/BoQunSDK/raw/master/repository/com/boqun/vrrpmserialport/VrRpmSerialPortDemo_v1.0.1_KK09O.zip)**
![image](https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/vrrpmserialport/images/demo.jpg)

AndroidManifest.xml 增加 Application

        <application
            android:name=".App"
        </application>
App.java 增加"RenderApplication.init(this)"初始化

        public class App extends Application {
            @Override
            public void onCreate() {
                super.onCreate();
                RenderApplication.init(this);
            }
        }


    
