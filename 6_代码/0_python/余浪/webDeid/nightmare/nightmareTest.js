const Nightmare = require('nightmare');

//var url = "https://www.baidu.com";
var url = "https://firewallsecuritytest.58corp.com/webfp/index";


(function(url){
    const nightmare = Nightmare({
        waitTimeout: 10000000,
        show: false
    })
    // show 显示浏览器界面
    
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
    nightmare
        .on("console", (log, msg)=>{
            console.log(msg);
        })
        .goto(url)
        .end()
        .evaluate(()=>{
            console.log(document.title);
        })
        .wait(2000)
        .then(async function () {
            console.log('load success');
            nightmare.title(function(x){console.log(x);});
            while((await readlineSync("input `e` to exit: ")).readUInt8() != 101){
                continue;
            };
        })
        .catch(function (error) {
            console.error('Error:', error);
        });
})(url)
