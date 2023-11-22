import frida
import sys
import readchar

HOST = "192.168.56.108"
PORT = "54321"

device = frida.get_device_manager().add_remote_device('{host}:{port}'.format(host=HOST, port=PORT))

session = device.attach("notepad.exe")
script = session.create_script("""
    console.log('[BEGIN] create_script');
    var user32dll = Module.getBaseAddress("user32.dll");
    console.log('[user32dll Base Address]:'+ user32dll);
    console.log('[user32dll BEFORE ensure init]:'+ user32dll);
    Module.ensureInitialized("user32.dll");
    console.log('[user32.dll AFTER ensure init]:'+ user32dll);
    console.log('[clipboard] going to open the clipboard with NativeFunction');
    var openClipboard_ptr = Module.findExportByName('user32.dll','OpenClipboard');
    console.log('[User32dll openClipboard_ptr] after Address:'+ openClipboard_ptr);
    var openClipboard = new NativeFunction(openClipboard_ptr, 'int64',['int64']);
    console.log('[openClipboard] NativeFunction set');
    var is_open = openClipboard(0);
    if(is_open !== 0){
        console.log('[CLIPBOARD] is open');
        var closeClipboard_ptr = Module.findExportByName('user32.dll','CloseClipboard');                       
        var closeClipboard = new NativeFunction(closeClipboard_ptr,'int64',[]);
        console.log('[CloseClipboard] NativeFunction Set');
        var getClipboardData_ptr = Module.findExportByName('user32.dll','GetClipboardData');
        var getClipboardData = new NativeFunction(getClipboardData_ptr,'uint64',['uint64']);
        console.log('[GetClipboardData] NativeFunction Set');
        console.log('[GetClipboardData] going to read data from the clipboard');
        var data = getClipboardData(1);
        var data_ptr = ptr(data);
        console.log(data);
        console.log('[getClipboardData] Data=['+data_ptr.readUft8String()+'].');
        closeClipboard()   
    }else{
        console.log('[Clipboard] is not open: ERROR,exit.');
    }
    console.log('[END] create_script');
""")
script.load()
print("Press Key to deatach ...")
readchar.readkey()

session.detach()
print("Detached.")