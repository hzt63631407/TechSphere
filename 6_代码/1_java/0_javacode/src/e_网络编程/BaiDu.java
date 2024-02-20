package e_网络编程;

public class BaiDu {
    public static void main(String[] args) {
        String result;
        HttpClient httpclient = new HttpClient();
        result = httpclient.doPost("https://www.baidu.com","测试");
        System.out.println(result);

    }
}
