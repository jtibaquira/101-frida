Java.perform(function() {
    console.log("[+] Deteccion de Root !");
    var deteccion = Java.use("owasp.sat.agoat.RootDetectionActivity");
    deteccion.isRooted.implementation = function(){
        console.log("RootDetectionActivity.isRooted is called");
        return false;
    };
});
