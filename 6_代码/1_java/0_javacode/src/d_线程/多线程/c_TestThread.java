package d_线程.多线程;


import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;



class MyCallable implements Callable {
    private int i = 0;
    @Override
    public Object call() throws Exception {
        System.out.println(Thread.currentThread().getName()+"  i的值："+ i);
        return i++; //call方法可以有返回值
    }
}



public class c_TestThread {
    public static void main(String[] args) {
        Callable callable = new MyCallable();
        for (int i = 0; i < 10; i++) {
            FutureTask task = new FutureTask(callable);
            new Thread(task,"子线程"+ i).start();
            try {
                //获取子线程的返回值
                System.out.println("子线程返回值："+task.get() + "\n");
            }  catch (Exception e) {
                e.printStackTrace();
            }
        }
    }
}

