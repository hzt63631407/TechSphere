package d_线程.多线程;

//Java 提供了三种创建线程的方法：
//
//通过实现 Runnable 接口；
//通过继承 Thread 类本身；
//通过 Callable 和 Future 创建线程。
//使用实现了Executor接口的ThreadPoolExecutor来创建线程池。（很少用）


//所以平时更推荐通过实现接口来实现多线程，也就是通过第二或第三种方式来实现，这样能保持代码灵活和解耦。


class RunnableDemo implements Runnable {
    private Thread t;
    private String threadName;

    RunnableDemo( String name) {
        threadName = name;
        System.out.println("构造方法 Creating " +  threadName );
    }

    public void run() {
        System.out.println("Running " +  threadName );
        try {
            for(int i = 4; i > 0; i--) {
                System.out.println("Thread: " + threadName + ", " + i);
                // 让线程睡眠一会
                Thread.sleep(50);
            }
        }catch (InterruptedException e) {
            System.out.println("Thread " +  threadName + " interrupted.");
        }
        System.out.println("Thread " +  threadName + " exiting.");
    }

    public void start () {
        System.out.println("Starting " +  threadName );
        if (t == null) {
            t = new Thread (this, threadName);
            t.start ();
        }
    }
}


public class a_TestThread {

    public static void main(String args[]) {
        RunnableDemo R1 = new RunnableDemo( "Thread-1");
        R1.start();

        RunnableDemo R2 = new RunnableDemo( "Thread-2");
        R2.start();
    }
}