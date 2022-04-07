# Rower quick to use



Quickly use iConsole SDK in Android projects, refer to the example and [Demo](https://github.com/arkuo0214/BoQunSDK/blob/master/repository/com/boqun/screensender/BQScreenSenderDemo.rar)



## Example

First create a class that inherits the Application class or add the following code to the onCreate method under the existing Application class:

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



Add `name="XXX"` under the application node in the AndroidManifest.xml file of the project (XXX is the Application class just now)

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



an be used in Activity or Service

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



For detailed usage, please download [Demo]() and read [API documentation](RowerApi.md)

