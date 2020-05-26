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

