// COMPILE: javac .\BI.java .\EBI.java .\iBI.java .\iEBI.java .\TestIsAssignableFrom.java
// RUN: java TestIsAssignableFrom

public class TestIsAssignableFrom{

     public static void main(String []args){
        System.out.println("Hello World");
        iBI ibi = new iBI();
        Class<?> classType = ibi.getClass();
        if( EBI.class.isAssignableFrom(classType) ){
            System.out.println("yes");
        }
        else{
            System.out.println("nope");
        }

        iEBI iebi = new iEBI();
        Class<?> classTypeE = iebi.getClass();
        if( EBI.class.isAssignableFrom(classTypeE) ){
            System.out.println("YES");
        }
        else{
            System.out.println("NO");
        }

     }
}
