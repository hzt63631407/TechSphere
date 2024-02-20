package a_基础.f_异常;

public class a_ArrayIndexOutOfBoundsException {

    public static void main(String[] args) {
        String ids = "1,2,3,";
        String[] idArr = ids.split(",");
        String idA = idArr[0];
        String idB = idArr[1];
        String idC = idArr[2];
        String idD = idArr[3];

    }
}


//java.lang.ArrayIndexOutOfBoundsException: 3
//        at 异常.ArrayIndexOutOfBoundsException.main (ArrayIndexOutOfBoundsException.java:11)
//        at sun.reflect.NativeMethodAccessorImpl.invoke0 (Native Method)
//        at sun.reflect.NativeMethodAccessorImpl.invoke (NativeMethodAccessorImpl.java:62)
//        at sun.reflect.DelegatingMethodAccessorImpl.invoke (DelegatingMethodAccessorImpl.java:43)
//        at java.lang.reflect.Method.invoke (Method.java:498)
//        at org.codehaus.mojo.exec.ExecJavaMojo$1.run (ExecJavaMojo.java:282)
//        at java.lang.Thread.run (Thread.java:748)
