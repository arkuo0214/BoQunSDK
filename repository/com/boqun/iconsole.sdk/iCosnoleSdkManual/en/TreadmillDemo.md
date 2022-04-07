# Treadmill quick to use

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



Can be used in Activity or Service

```java
public class TreadmillActivity extends AppCompatActivity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        //Initialize the instance
        BoQunTreadmill.init();

        BoQunTreadmill.queryConfigInfo();

        BoQunTreadmill.queryMachineInfo(BoQunTreadmill.TYPE_SPORT_STATUS);

        BoQunTreadmill.queryMachineInfo(BoQunTreadmill.TYPE_SPEED_AND_INCLINE);

        BoQunTreadmill.setOnTreadmillListener(new OnTreadmillListener() {

            @Override
            public void onResponseConfigInfo(TreadmillConfigInfo info) {
                
            }

            @Override
            public void onResponseSportStatus(int state) {
              
            }

            @Override
            public void onResponseSportData(int state, int heartRate, int speed) {
              
            }

            @Override
            public void onResponseSpeedLevel(int speed) {
             
            }

            @Override
            public void onResponseInclineLevel(int incline) {
            
            }

            @Override
            public void onResponseFanLevel(int level) {
              
            }
            

            @Override
            public void onExternalKeyEvent(int keyCode, int value) {
               
             
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
        BoQunBike.destroy();
    }
}

```



For detailed usage, please download [Demo]() and read [API documentation](TreadmillApi.md)

