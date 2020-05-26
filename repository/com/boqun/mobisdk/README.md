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

    implementation 'com.boqun:mobisdk:x.x.x'
    
}

如果出现 unable to resolve dependency for app@......
看能不能访问https://raw.githubusercontent.com
不能就在C:\Windows\System32\drivers\etc路径下找到hosts文件

添加 以下内容并保存即可访问
199.232.68.133 raw.githubusercontent.com

API使用詳情請參考MoBiSDKDemo.zip
