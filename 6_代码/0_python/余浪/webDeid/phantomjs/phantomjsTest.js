// a phantomjs example

//var url = "https://www.baidu.com";
var url = "https://firewallsecuritytest.58corp.com/webfp/index";

(function(){
    var page = require('webpage').create();
    page.settings.javascriptEnabled = true;
    page.settings.loadImages = true;
    page.settings.webSecurityEnabled = false;
    phantom.outputEncoding="gbk";
    page.onError = function(msg, trace){
        console.log(msg,trace);
    }
    page.onConsoleMessage = function(msg) {
        console.log('Page title is ' + msg);
    };
    page.onLoadFinished = function(){
        page.settings.javascriptEnabled = true;
    };
    page.open(url, function(status) {
        if ( status === "success" ) {
            console.log("page title: ", page.title);
            console.log("upload success");
        } else {
            console.log("Page failed to load.");
        }
    });
})(url)
