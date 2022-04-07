# 快速使用



在Android项目中快速使用iConsole SDK,具体使用方法参考示例以及[Demo](https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/screensender/BQScreenSenderDemo.rar)



## 示例



先创建一个类继承Application类或者在已有Application类下onCreate方法中添加如下代码：

```java
public class App extends Application {
    
    @Override
    public void onCreate() {
        super.onCreate();
        
        //APP_ID Need to apply
        BoQun.createInstance(APP_ID, this);

    }
}
```



在项目AndroidManifest.xml文件中application节点下添加`name="XXX"` (XXX为刚刚的Application类)

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    package="com.boqun.serialportdemo">

    <application
        android:name=".App"
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/AppTheme">

</manifest>
```



可在Activity或Service中使用

```java
public class RowerActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        //Initialize the instance
        BoQunRower.init();

        BoQunRower.queryConfigInfo();

        BoQunRower.queryMachineInfo(BoQunRower.TYPE_LOAD_LEVEL);

        BoQunRower.queryMachineInfo(BoQunRower.TYPE_SPORT_STATUS);

        BoQunRower.setOnRowerListener(new OnRowerListener() {

            @Override
            public void onResponseConfigInfo(RowerConfigInfo info) { 
               
            }

            @Override
            public void onResponseSportStatus(int status) {
              
            }

            @Override
            public void onResponseSportData(RowerSportData data) {
              
            }

            @Override
            public void onResponsePullAndPut(int progress, boolean isPull) {
               
            }

            @Override
            public void onResponseLoadLevel(int load) {
             
            }

            @Override
            public void onResponseFanLevel(int level) {
             
            }

            @Override
            public void onExternalKeyEvent(int keyCode) {
             
            }

            @Override
            public void onError(int errorCode) {
                
            }
        });

    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        //Destroy the instance
        BoQunRower.destroy();
    }
}

```



详细使用方法请下载[Demo]()和阅读[API文档](RowerApi.md)

