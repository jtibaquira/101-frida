import frida

def on_message(message, data):
    print("[on_message] message:", message, "data:", data)

session = frida.attach("simple0_static")

script = session.create_script("""
rpc.exports.enumerateModules = function () {
  return Process.enumerateModules();
};
""")
script.on("message", on_message)
script.load()

print([m["name"] for m in script.exports_sync.enumerate_modules()]) 
