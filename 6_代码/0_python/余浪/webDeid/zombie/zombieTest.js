const Browser = require('zombie');

//var url = "https://www.baidu.com";
var url = "https://firewallsecuritytest.58corp.com/webfp/index";


(function(url){

    function readlineSync(tips) {
        process.stdout.write(tips);
        return new Promise((resolve, reject) => {
            process.stdin.resume();
            process.stdin.on('data', function (data) {
                process.stdin.pause();
                resolve(data);
            });
        });
    }
    
    const browser = new Browser();

    browser.on('console', (level, message) => {
        console.log(`${level}: ${message}`);
    });

    browser.visit(url, () => {
        console.log("load success");
    });
    setTimeout(async function(){
        while((await readlineSync("input `e` to exit: ")).readUInt8() != 101){
            continue;
        };
        browser.destroy();
        process.exit();
    }, 3000);
})(url)
