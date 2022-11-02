[CN]:https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/iconsole.sdk/README_cn.md
# English document: (EN/[中文][CN])
https://arkuo0214.github.io/BoQunSDK/iCosnoleSdkManual/en/
<br/>
# Instructions for use:  
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
    	implementation 'com.boqun:iconsole.sdk:2.1.9'
    }
    
If unable to resolve dependency for app@...... See if you can access https://raw.githubusercontent.com If you can't find the hosts file in the C:\Windows\System32\drivers\etc path
Add the following and save to access 199.232.68.133 raw.githubusercontent.com
