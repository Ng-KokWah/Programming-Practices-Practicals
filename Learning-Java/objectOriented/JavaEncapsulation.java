package objectOriented;

/*
 * USES: Human.java file
 * 
 * Encapsulation is to make sure that sensitive data is hidden from the users
 * 
 * This is done by:
 * 1. declare class variables/attributes as private
 * 2. provide public get and set methods to access and update the value of a private variable
 * 
 * Why use it?
 * Better control of class attributes and methods
 * Class attributes can be made read-only (if you only use the get method), or write-only (if you only use the set method)
 * Flexible: the programmer can change one part of the code without affecting other parts
 * Increased security of data
 * 
 * To quickly generate getter and setters just click on the variable you want to generate for
 * then click on Source > Generate getters and setters...
 */

public class JavaEncapsulation {
	public static void main(String[] args) {
		Human myObj = new Human();
	    myObj.setName("John"); // Set the value of the name variable to "John"
	    System.out.println(myObj.getName()); //John
	}
}
