/*to import any packages, and/or classes
 * use import package.name.class or package.name.* to import all
 */
import java.util.*;

public class PackagesImport {
	public static void main(String[] args) {
		/*
		 * Java uses a file system to store packages
		 * so for example root > mypack > MyPackageClass.java
		 * 
		 * to create your own packages
		 * if you create a package in eclipse the package statement is auto added
		 * package mypack;
		 * class MyPackageClass {
		 * public static void main(String[] args) {
		 * System.out.println("This is my package!");
		 * }
		 * }
		 * 
		 * in this case save the file and then use javac MyPackageClass.java to compile
		 * then to compile the package use javac -d . MyPackageClass.java
		 * 
		 * this creates a new folder called mypack which is the name you gave the package
		 * now using java mypack.MyPackageClass would execute the SOP
		 */
	}
}
