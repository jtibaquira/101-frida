Java.perform(function(){
    console.log("[+] Deteccion de SSL Pinning !");
    console.log("[+] OkHTTP 3.x Encontrado");
    var CertificatePinner = Java.use('okhttp3.CertificatePinner');
    CertificatePinner.check.overload('java.lang.String', 'java.util.List').implementation = function() {
        console.log("[+] OkHTTP 3.x check() called. Not throwing an exception.");
    };
});