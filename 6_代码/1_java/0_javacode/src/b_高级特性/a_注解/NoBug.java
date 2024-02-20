package 注解;


// 没有main方法 单独运行测试不了
// 实际运行程序时 有时候方法没有被调用 需要单元测试

public class NoBug {
    @Jiecha
    public void suanShu() {
        System.out.println("1234567890");
    }

    @Jiecha
    public void jiafa() {
        System.out.println("1+1=" + 1 + 1);
    }

    @Jiecha
    public void jiefa() {
        System.out.println("1-1=" + (1 - 1));
    }

    @Jiecha
    public void chengfa() {
        System.out.println("3 x 5=" + 3 * 5);
    }

    @Jiecha
    public void chufa() {
        System.out.println("6 / 0=" + 6 / 0);
    }

    public void ziwojieshao() {
        System.out.println("我写的程序没有 bug!");
    }

}
