[EN]:https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/iconsole.sdk/README_en.md
# 中文文檔:([EN]/中文)
https://arkuo0214.github.io/BoQunSDK/iCosnoleSdkManual/zh-CN/
<br/>
<br/>
<br/>
<br/>
<br/>
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
    	implementation 'com.boqun:iconsole.sdk:2.1.5'
    }
    
如果出现 unable to resolve dependency for app@...... 看能不能访问https://raw.githubusercontent.com 不能就在C:\Windows\System32\drivers\etc路径下找到hosts文件  
添加 以下内容并保存即可访问 199.232.68.133 raw.githubusercontent.com  
