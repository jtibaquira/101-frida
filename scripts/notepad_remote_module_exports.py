import frida
import sys
import readchar

HOST = "192.168.56.108"
PORT = "54321"

device = frida.get_device_manager().add_remote_device("192.168.56.108:54321")
#device = frida.get_device_manager().add_remote_device(
  #'{host}:{port}'.format(host=HOST, port=PORT))

session = device.attach("notepad.exe")
script = session.create_script("""
		Process.enumerateModules({
			onMatch: function(module){
                if(module.name == 'USER32.dll'){
                    console.log("[USER32.dll Found]");
                    console.log("[USER32.dll] Export list");
                        module.enumerateExports().forEach(function(item){
                            console.log("Exports: " + item.name + " -> (" + item.address + ")"); 
                        });
                }
            },
			onComplete: function(){}
		});
""")
script.load()
print("Press Key to deatach ...")
readchar.readkey()

session.detach()
print("Deatached")