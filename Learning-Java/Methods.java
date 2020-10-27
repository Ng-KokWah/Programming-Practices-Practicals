import java.util.Scanner;

/*
 * For classes the access modifiers can only be:
 * 1. public -> accessible by any other classes
 * 2. default (aka dont specify anything) -> only accessible by classes in the same package
 */
public class Methods {
	/*
	 * Access modifiers available to attributes, methods and constructors are:
	 * 1. public -> accessible in all classes
	 * 2. private -> only accessible within the declared class
	 * 3. default (aka dont specify anything) -> only accessible in the same package
	 * 4. protected -> accessible in the same package and subclasses
	 * 
	 * Non-access modifiers for attributes, methods and constructors:
	 * 1. final -> cannot be overridden/modified
	 * so if you declare attributes like final int a = 15 and later try to change the value by: x = 50, error occurs
	 * 2. static -> meaning it belongs to the class, rather than an object 
	 * (aka when calling/accessing it, you need not create an object of it)
	 * e.g. if it is a static method i can just call myMethod(); instead of
	 * MyClass c = new MyClass();
	 * c.myMethod();
	 * 
	 * 3. abstract -> can only be used in an abstract class, and can only be used on methods
	 * The method does not have a body, e.g. abstract void run();, the body is provided by the subclass (inherited from)
	 * 
	 * abstract class Person {
	 * 		public abstract void study();
	 * }
	 * 
	 *this is considered the subclass since it is inheriting from Person
	 * class Student extends Person {
	 * 		public void study() {
	 * 			SOP("Study");
	 * 		}
	 * } 
	 * 4. transient -> attributes and methods are skipped when serializing the object containing them
	 * 5. synchronized -> methods can only be accessed by one thread at a time
	 * 6. volatile -> value of an attribute is not cached thread-locally, and is always read from the "main memory"
	 */
	
	/*
	 * Method Overloading -> multiple methods can have the same name but with different parameters
	 * this is often seen in the creation of constructors, this means that
	 * int myMethod(int x, int y)
	 * double myMethod(double x, double y) works as well
	 */
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		System.out.println("Enter a number: ");
		int num1 = sc.nextInt();
		
		System.out.println("Enter an operator: ");
		String operator = sc.next();
		
		System.out.println("Enter another number: ");
		int num2 = sc.nextInt();
		
		String completed = "After ";
		switch(operator) {
			case "+":
				completed += "Adding: " + addition(num1, num2);
				break;
			case "-":
				completed += "Subtracting: " + subtraction(num1, num2);
				break;
			case "*":
				completed += "Multiplying: " + multiplication(num1, num2);
				break;
			case "/":
				completed += "Dividing: " + division(num1, num2);
				break;
			default:
				completed = "Error Invalid Operator!"; 
		}
		
		System.out.println(completed);
		sc.close();
	}
	
	public static int addition(int num1, int num2) {
		return num1 + num2;
	}
	
	public static int subtraction(int num1, int num2) {
		return num1 - num2;
	}
	
	public static int multiplication(int num1, int num2) {
		return num1 * num2;
	}
	
	public static int division(int num1, int num2) {
		return num1 / num2;
	}
}
