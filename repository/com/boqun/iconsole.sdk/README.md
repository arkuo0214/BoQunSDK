# 中文文檔:
https://arkuo0214.github.io/BoQunSDK/iCosnoleSdkManual/zh-CN/

# English document: 
https://arkuo0214.github.io/BoQunSDK/iCosnoleSdkManual/en/
&



# 使用說明(Instructions for use):  
增加(Increase)  
\build.gradle  


    allprojects {
    	repositories {
    		maven {
    			url 'https://raw.githubusercontent.com/arkuo0214/BoQunSDK/master/repository'
    		}
    	}
    }
    

增加(Increase)    
\app\build.gradle  


    dependencies {
    	implementation 'com.boqun:iconsole.sdk:2.0.2'
    }
    
如果出现 unable to resolve dependency for app@...... 看能不能访问https://raw.githubusercontent.com 不能就在C:\Windows\System32\drivers\etc路径下找到hosts文件  
添加 以下内容并保存即可访问 199.232.68.133 raw.githubusercontent.com  

If unable to resolve dependency for app@...... See if you can access https://raw.githubusercontent.com If you can't find the hosts file in the C:\Windows\System32\drivers\etc path
Add the following and save to access 199.232.68.133 raw.githubusercontent.com
