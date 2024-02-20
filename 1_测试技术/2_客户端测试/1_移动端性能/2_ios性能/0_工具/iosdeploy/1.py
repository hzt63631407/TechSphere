import subprocess

bundle_id = "com.xinanSDK.iphone"
command = ["ios-deploy", "--bundle_id", bundle_id, "--justlaunch"]
subprocess.run(command, check=True)