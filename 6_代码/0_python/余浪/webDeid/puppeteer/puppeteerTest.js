const puppeteer = require('puppeteer');

var i = 0 // 0-chromium,1-webkit,2-firefox
//var url = "https://www.baidu.com";
var url = "https://firewallsecuritytest.58corp.com/webfp/index";

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

(async (url) => {
    const browser = await puppeteer.launch({headless: false});
    const page = await browser.newPage();
    await page.goto(url);
    console.log(page.title());
    while((await readlineSync("input `e` to exit: ")).readUInt8() != 101){
        continue;
    }
    browser.close();
})(url)
